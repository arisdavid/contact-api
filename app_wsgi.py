from src.app import (flask_app,
                     celery_app)

app = flask_app
celery = celery_app

if __name__ == "__main__":
    app.run()
