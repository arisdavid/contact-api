# Development settings.py
import os

DEBUG = True

# Secret key
SECRET_KEY = os.urandom(24)

# Celery Config
CELERY_BROKER_URL = f"redis://:devpassword@redis-service.rqmp.svc.cluster.local:6379/0"
CELERY_RESULT_BACKEND = (
    f"redis://:devpassword@redis-service.rqmp.svc.cluster.local:6379/0"
)
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_REDIS_MAX_CONNECTIONS = 5


CELERYBEAT_SCHEDULE = {
    "add_random_contact": {
        "task": "src.blueprints.api.tasks.add_record",
        # Every 15 seconds insert random record
        "schedule": 15.0,
    },
    "remove_contact": {
        "task": "src.blueprints.api.tasks.delete_record",
        # Every 60 seconds poll the delete_record to check records older than 1 minute
        "schedule": 60.0,
    },
}

db_uri = f"postgresql://admin:admin123@postgres-service.rqmp.svc.cluster.local:5432/contact_db"
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
