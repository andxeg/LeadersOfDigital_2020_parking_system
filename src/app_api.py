#!/usr/bin/env python3.8

import os
import yaml
import logging
import connexion
from celery import Celery
from flask_cors import CORS
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

from db import rospark_db
from config import MYSQL_ROSPARK_DB, CELERY_REDIS, TASKS_PREFIX


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)


def connexion_register_blueprint(app, swagger_file, **kwargs):
    env = Environment(loader=FileSystemLoader("."))
    swagger_string = env.get_template(swagger_file).render(**kwargs)
    specification = yaml.safe_load(swagger_string)
    app.add_api(specification, **kwargs)

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

class MyCelery(Celery):
    def gen_task_name(self, name, module):
        return TASKS_PREFIX + "." + super(MyCelery, self).gen_task_name(name, module)

celery_app = MyCelery(broker=CELERY_REDIS, backend=CELERY_REDIS)
celery_app.conf.timezone = 'UTC'
celery_app.conf.broker_connection_max_retries = 5
celery_app.conf.result_backend_max_retries = 5
celery_app.conf.task_track_started = True

application = app.app
application.context = AttrDict()
rospark_db.make_session_context(application, "rospark_db_session", MYSQL_ROSPARK_DB)
application.context["celery_app"] = celery_app


CORS_RESOURCES = {r"/*": {"origins": "*", "supports_credentials":True, "allow_headers": ["X-Auth", "Cookie", "Content-Type"]}}
CORS(app.app, resources=CORS_RESOURCES)

connexion_register_blueprint(app, "openapi3.yml", validate_responses=True, strict_validation=True)

if __name__ == '__main__':
    HOST = os.environ.get("HOST", "127.0.0.1")
    PORT = int(os.environ.get("PORT", 8080))
    app.run(host=HOST, port=PORT)
