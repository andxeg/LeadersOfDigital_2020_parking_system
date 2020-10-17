import math
import json
import uuid
import celery
import logging
import datetime
import connexion
import collections
from collections import OrderedDict
from sqlalchemy import asc, and_, func
from celery.result import AsyncResult
from flask import current_app, jsonify


from config import TASKS_QUEUE
from db.rospark_db import ParkingsRecordsTbl


LOG  = logging.getLogger(__name__)


def get_all_parkings():
    try:
        qs = current_app.context.rospark_db_session()
        rows = (qs.query(
                        ParkingsRecordsTbl
                    ).order_by(
                        asc(ParkingsRecordsTbl.created_date)
                    ))

        result = []
        for row in rows.all():
            result.append(row.serialize())

    except Exception as e:
        LOG.exception("Error: %s" % str(e))
        return jsonify(dict(status="error")), 500

    return jsonify(dict(status="ok",
                        result=result)), 200

def get_parkings_custom():
    try:
        data = json.loads(connexion.request.data, object_pairs_hook=collections.OrderedDict)
        longitude = data["longitude"]
        latitude  = data["latitude"]
        radius    = data["radius"]

        kmInLongitudeDegree = 111.320 * math.cos( latitude / 180.0 * math.pi)

        delta_lat = radius / 111.1;
        delta_long = radius / kmInLongitudeDegree;

        qs = current_app.context.rospark_db_session()
        rows = (qs.query(
                        ParkingsRecordsTbl
                    ).filter(and_(func.abs(ParkingsRecordsTbl.latitude - latitude) < delta_lat,
                                  func.abs(ParkingsRecordsTbl.longitude - longitude) < delta_long)))
        result = []
        for row in rows.all():
            result.append(row.serialize())

    except Exception as e:
        LOG.exception("Error: %s" % str(e))
        return jsonify(dict(status="error")), 500

    return jsonify(dict(status="ok",
                        result=result)), 200

def detect_parking():
    try:
        data = json.loads(connexion.request.data, object_pairs_hook=collections.OrderedDict)

        task_id = str(uuid.uuid4())

        task_name = "rospark_async.tasks.parkings_photo_analysis.parkings_photo_analysis"
        sig = current_app.context.celery_app.signature(task_name,
                                                       args=(data,),
                                                       immutable=True).set(queue=TASKS_QUEUE)

        sig.apply_async(expires=1200, task_id=task_id)

    except Exception as e:
        LOG.exception("Error: %s" % str(e))
        return jsonify(dict(status="error")), 500

    return jsonify(dict(status="ok")), 200

def save_parkings_info():
    try:
        data = json.loads(connexion.request.data, object_pairs_hook=collections.OrderedDict)
        
        qs = current_app.context.rospark_db_session()
        record_db = ParkingsRecordsTbl(
            created_date=datetime.datetime.utcnow(),
            longitude=data["longitude"],
            latitude=data["latitude"],
            total=data["total"],
            free=data["free"],
            photo=str.encode(data["photo"]))

        qs.add(record_db)
        qs.commit()

    except Exception as e:
        LOG.exception("Error: %s" % str(e))
        return jsonify(dict(status="error")), 500

    return jsonify(dict(status="ok")), 200

def delete_all_parkings_info():
    try:
        qs = current_app.context.rospark_db_session()

        delete_q = ParkingsRecordsTbl.__table__.delete().where(True)
        qs.execute(delete_q)
        qs.commit()

    except Exception as e:
        LOG.exception("Error: %s" % str(e))
        return jsonify(dict(status="error")), 500

    return jsonify(dict(status="ok")), 200
