import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from src.blueprints.api.models import Contact as ContactModel
from src.blueprints.api.models import Email as EmailModel


class Contact(SQLAlchemyObjectType):
    class Meta:
        model = ContactModel
        interfaces = (graphene.relay.Node, )


class Email(SQLAlchemyObjectType):
    class Meta:
        model = EmailModel
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    contacts = graphene.List(Contact)
    emails = graphene.List(Email)

    def resolve_contacts(self, info):
        query = Contact.get_query(info)
        return query.all()

    def resolve_emails(self, info):
        query = Email.get_query(info)
        return query.all()

    node = graphene.relay.Node.Field()
    all_contacts = SQLAlchemyConnectionField(Contact)
    contact = graphene.relay.Node.Field(Contact)


schema = graphene.Schema(query=Query)
