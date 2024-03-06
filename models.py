from mongoengine import Document, EmbeddedDocument, StringField, ListField, ReferenceField, DateTimeField, EmbeddedDocumentField
from datetime import datetime

class Tag(EmbeddedDocument):
    name = StringField()

class Author(Document):
    fullname = StringField(required=True)
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()

class Quotes(Document):
    author = ReferenceField(Author, required=True)
    tags = ListField(EmbeddedDocumentField(Tag))
    quote = StringField()


