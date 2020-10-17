import os

MODEL_WEIGTHS_PATH = os.environ.get("MODEL_WEIGTHS_PATH", "./core/models/best.py")

MYSQL_ROSPARK_DB = os.environ.get("MYSQL_ROSPARK_DB", "mysql://msu_team:msu_team_password@rospark_mysql:3306/db_rospark")

CELERY_REDIS = os.environ.get("CELERY_REDIS","redis://127.0.0.1:6380")
TASKS_QUEUE = os.environ.get("TASKS_QUEUE", "rospark_async")
TASKS_PREFIX = os.environ.get("TASKS_PREFIX", "rospark_async")
