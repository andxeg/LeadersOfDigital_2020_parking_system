import time
import ujson
import random
import datetime

from app_worker import celery_app, SqlAlchemyTask, context

from db.ids_db import ParkingsRecordsTbl


@celery_app.task(base=SqlAlchemyTask, bind=True, time_limit=1200)
def parkings_photo_analysis(self, data):
    task_id = self.request.id.__str__()

    print("Doing parkings_photo_analysis [task_id: %s] START" % str(task_id))

    try:        
        total, free = context.rospark_model.predict(data["photo"])

        print("Photo were successfully analyzed. Save result.")

        qs = context.rospark_db_session()
        record_db = ParkingsRecordsTbl(
            created_date=datetime.datetime.utcnow(),
            longitude=data["longitude"],
            latitude=data["latitude"],
            total=total,
            free=free,
            photo=data["photo"])

        qs.add(records_db)
        qs.commit()

    except Exception as e:
        print("Cannot analyze records: %s" % str(e))
        raise Exception("Cannot analyze records: %s" % str(e))

    print("Doing ids_record_analysis [task_id: %s] END" % str(task_id))
