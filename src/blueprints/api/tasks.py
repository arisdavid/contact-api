# Model
from src.blueprints.api.models import (Contact, Email)
from src.extensions import db
from datetime import (datetime,
                      timedelta)

# Celery
from src.app import celery_app
import faker

celery = celery_app


@celery.task(bind=True)
def add_record(self):

    """ Celery Task to add random records """
    f = faker.Faker()

    new_contact = Contact(username=f.user_name(),
                          first_name=f.first_name(),
                          last_name=f.last_name(),
                          date_created=datetime.utcnow())

    emails = [{'email': f.email()},
              {'email': f.email()}]

    for email in emails:
        new_contact.emails.append(Email(
            email=email.get('email')
        ))

    db.session.add(new_contact)
    db.session.commit()


@celery.task(bind=True)
def delete_record(self):

    """ Celery Task to delete record older than 1 minute """

    current_time = datetime.utcnow()
    one_minute_ago = current_time - timedelta(minutes=1)

    contacts = db.session.query(Contact).filter(Contact.date_created < one_minute_ago)
    for contact in contacts:
        db.session.delete(contact)
        db.session.commit()


