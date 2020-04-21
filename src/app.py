from flask import Flask
from celery import Celery
from src.celery_task_registry import CELERY_TASK_LIST

# Blueprints
from src.blueprints.pages.views import page
from src.blueprints.api.views import api

# Extensions
from src.extensions import (db, marshmallow)


def make_celery(app=None):
    """
    Make Celery App
    :param app: flask app instance
    :return: celery
    """

    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'],
                    include=CELERY_TASK_LIST)

    celery.conf.update(app.config)
    task_base = celery.Task

    class ContextTask(task_base):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return task_base.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)
    app.register_blueprint(api)

    # Mutate the flask app
    apply_extensions(app)

    with app.app_context():
        db.create_all()

    return app


def apply_extensions(app):
    """
     Mutate the flask application with extensions
    :param app: flask instance
    :return: None
    """

    # SQL Alchemy
    db.init_app(app)

    # Marshmallow
    marshmallow.init_app(app)

    return None


flask_app = create_app()
celery_app = make_celery(flask_app)
