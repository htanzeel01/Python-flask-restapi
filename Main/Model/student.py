from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
     #__tablename__ = "student"

     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
     name = db.Column(db.String(255), nullable=False)
     number = db.Column(db.String(255), unique=True, nullable=False)
     deleted_at = db.Column(db.DateTime)
     classroom = db.relationship("Classroom", backref = "student")

     def __repr__(self):
        return "<Student '{}'>".format(self.name)
