import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from src.blueprints.api.models import Contact as ContactModel
from src.blueprints.api.models import Email as EmailModel


class Contact(SQLAlchemyObjectType):
    class Meta:
        model = ContactModel


class Email(SQLAlchemyObjectType):
    class Meta:
        model = EmailModel


class Query(graphene.ObjectType):
    contacts = graphene.List(Contact)
    emails = graphene.List(Email)

    def resolve_contacts(self, info):
        query = Contact.get_query(info)
        return query.all()

    def resolve_emails(self, info):
        query = Contact.get_query(info)
        return query.all()


schema = graphene.Schema(query=Query)
