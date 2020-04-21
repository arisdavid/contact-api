# Development settings.py
import os
from pathlib import Path
from celery.schedules import crontab

DEBUG = True

# Secret key
SECRET_KEY = os.urandom(24)

SERVER_NAME = 'localhost:8000'

# Celery Config - Redis does not exist at the moment
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

CELERYBEAT_SCHEDULE = {
    'add_random_contact': {
        'task': 'src.blueprints.api.tasks.add_record',
        # Every 15 seconds insert random record
        'schedule': 15.0,
    },

    'remove_contact': {
        'task': 'src.blueprints.api.tasks.delete_record',
        # Every 60 seconds poll the delete_record to check records older than 1 minute
        'schedule': 60.0,
    }
}


# Database configuration
"""DB_PATH = os.path.join(Path(__file__).parent.parent, 'database.sqlite3')
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
SQLALCHEMY_TRACK_MODIFICATIONS = False"""

db_uri = 'postgresql://dev:devpassword@postgres:5432/contact_management_db'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

