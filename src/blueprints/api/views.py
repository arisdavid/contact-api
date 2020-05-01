from datetime import datetime

from flask import Blueprint, jsonify, render_template, request
from sqlalchemy.exc import IntegrityError
from src.extensions import db

from .models import Contact, Email, contact_schema, contacts_schema

api = Blueprint("api", __name__, template_folder="templates")


@api.route("/contact", methods=["POST"])
def add_contact():
    """ Create a contact"""

    if request.method == "POST":

        username = request.json["username"]
        first_name = request.json["firstName"]
        last_name = request.json["lastName"]

        if "emails" in request.json:
            emails = request.json["emails"]
        else:
            emails = None

        try:
            new_contact = Contact(
                username=username,
                first_name=first_name,
                last_name=last_name,
                date_created=datetime.utcnow(),
            )
            if emails:
                for email in emails:
                    new_contact.emails.append(Email(email=email.get("email")))
            db.session.add(new_contact)
            db.session.commit()

            return contact_schema.jsonify(new_contact), 201

        except IntegrityError:
            db.session.rollback()
            return {"message": f"User already exists. Use unique username or email."}


@api.route("/contact", methods=["GET"])
def get_contacts():
    """ Get All Contacts """
    if request.method == "GET":
        all_contacts = Contact.query.all()
        out = contacts_schema.dump(all_contacts)

        if out:
            return jsonify(out)
        else:

            return {"message": "empty database"}, 404


@api.route("/contact/<id>", methods=["GET"])
def get_contact(id):
    """ Get a contact by id """
    if request.method == "GET":

        contact = Contact.query.get(id)
        out = contact_schema.dump(contact)
        if out:
            return jsonify(out)
        else:
            return {"message": f"record {id} not found"}, 404


@api.route("/contact/<id>", methods=["PUT"])
def update_contact(id):
    """ Update a contact """
    if request.method == "PUT":

        contact = Contact.query.get(id)

        username = request.json["username"]
        first_name = request.json["firstName"]
        last_name = request.json["lastName"]

        if "emails" in request.json:
            emails = request.json["emails"]
        else:
            emails = None
        try:
            contact.name = username
            contact.first_name = first_name
            contact.last_name = last_name

            if emails:
                for email in emails:
                    contact.emails.append(Email(email=email.get("email")))

            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": f"Email already exists."}

        return contact_schema.jsonify(contact)


@api.route("/contact/<id>", methods=["DELETE"])
def delete_contact(id):
    """ Delete a contact """
    if request.method == "DELETE":
        contact = Contact.query.get(id)
        db.session.delete(contact)
        db.session.commit()
        return contact_schema.jsonify(contact)


@api.route("/api-documentation")
def api_doc():
    """
    API Documentation
    :return: html
    """
    # TODO: Use Swagger from Flask-RESTPlus
    return render_template("api-doc.html", title="API-Documentation")
