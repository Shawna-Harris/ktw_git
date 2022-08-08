from website import db
from flask_login import UserMixin
from datetime import datetime
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150), nullable = False)
    last_name = db.Column(db.String(150), nullable = False)
    course = db.Column(db.String(150))
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    notes = db.relationship('Note')

    #create a String
    def __repr__(self) -> str:
        return '<first_name %r>' % self.first_name