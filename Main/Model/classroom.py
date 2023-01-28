from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Classroom(db.Model):
     #__tablename__ = "class"

     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
     student_id = db.Column(db.Integer, db.ForeignKey('user.id'))