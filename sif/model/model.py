from sif.model import db


class Imdb(db.EmbeddedDocument):
    imdb_id = db.StringField()
    rating = db.DecimalField()
    votes = db.IntField()


class Movie(db.Document):
    title = db.StringField(required=True)
    year = db.IntField()
    rated = db.StringField()
    director = db.StringField()
    actors = db.ListField()
    imdb = db.EmbeddedDocumentField(Imdb)
    added_by = db.ReferenceField('User')

