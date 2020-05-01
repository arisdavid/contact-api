FROM python:3.7

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN ["chmod", "+x", "./start_celery.sh"]

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "app_wsgi:app"


