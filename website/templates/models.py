"""  from website import db """
from flask_login import UserMixin
from sqlalchemy.sql import func


""" class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    contact_number = (db.Integer(9))
    password = db.Column(db.String(150))

    student = db.relationship('Student') """

""" class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)"""
