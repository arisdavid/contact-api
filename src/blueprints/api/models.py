from src.extensions import (db,
                            marshmallow)

from marshmallow import fields


class Contact(db.Model):
    """ Contact Model """

    id = db.Column(db.Integer, unique=True,
                   primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime(), nullable=False)

    emails = db.relationship('Email',
                             backref='contact',
                             cascade='all, delete, delete-orphan',
                             single_parent=True)

    def __repr__(self):
        return f"<Contact(username='{self.username}')>"


class Email(db.Model):
    """ Email Model """
    id = db.Column(db.Integer, unique=True,
                   primary_key=True, autoincrement=True)
    email = db.Column(db.String(250), nullable=True, unique=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'))


class EmailSchema(marshmallow.Schema):
    """ Email Schema """
    email = fields.String(attribute='email')


# Contact Schema
class ContactSchema(marshmallow.Schema):
    """ Contact Schema """
    id = fields.String(attribute='id')
    username = fields.String(attribute='username')
    firstName = fields.String(attribute="first_name")
    lastName = fields.String(attribute="last_name")
    dateCreated = fields.DateTime(attribute="date_created")
    emails = fields.Nested(EmailSchema, many=True)


# Initialize Schema
contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)
