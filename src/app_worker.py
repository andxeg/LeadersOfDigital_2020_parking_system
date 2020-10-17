import os
import sys
import logging

from celery import Celery
from celery.signals import task_prerun, after_setup_logger
from sqlalchemy.orm import scoped_session, sessionmaker

from db import rospark_db
from core import parkings_recognition
from config import TASKS_PREFIX, CELERY_REDIS, MYSQL_ROSPARK_DB


class MyCelery(Celery):
    def gen_task_name(self, name, module):
        return TASKS_PREFIX + "." + super(MyCelery, self).gen_task_name(name, module)

celery_app = MyCelery(backend=CELERY_REDIS, broker=CELERY_REDIS, include=[
    "tasks.parkings_photo_analysis"
])

celery_app.conf.timezone = 'UTC'
celery_app.conf.broker_connection_max_retries = 5
celery_app.conf.result_backend_max_retries = 5
celery_app.conf.task_track_started = True

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

context = AttrDict()
context.rospark_db_session = scoped_session(sessionmaker(bind=rospark_db.make_engine(MYSQL_ROSPARK_DB)))
context.rospark_model = parkings_recognition.prepare_model()


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    logger.addHandler(logging.StreamHandler(sys.stdout))

class SqlAlchemyTask(celery_app.Task):
    abstract = True
    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        context.rospark_db_session.remove()
