import logging
from datetime import datetime, timedelta

import faker
from src.app import celery_app
from src.blueprints.api.models import Contact, Email
from src.extensions import db

celery = celery_app

logging.basicConfig(level=logging.INFO)


@celery.task()
def add_record():

    """ Celery Task to add random records """
    f = faker.Faker()

    new_contact = Contact(
        username=f.user_name(),
        first_name=f.first_name(),
        last_name=f.last_name(),
        date_created=datetime.utcnow(),
    )

    emails = [{"email": f.email()}, {"email": f.email()}]

    for email in emails:
        new_contact.emails.append(Email(email=email.get("email")))

    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception:
        logging.error(f"Unable to insert data for {new_contact.username}.")
    else:
        logging.info(f"New contact {new_contact.username} inserted into the database.")


@celery.task()
def delete_record():

    """ Celery Task to delete record older than 1 minute """

    current_time = datetime.utcnow()
    one_minute_ago = current_time - timedelta(minutes=1)

    contacts = db.session.query(Contact).filter(Contact.date_created < one_minute_ago)
    for contact in contacts:
        db.session.delete(contact)
        db.session.commit()
