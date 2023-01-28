import uuid
import datetime

from Main.Model.student import db
from Main.Model.student import Student
from typing import Dict, Tuple


def save_new_student(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    student = Student.query.filter_by(number=data['number']).first()
    if not student:
        new_user = Student(
            name=data['name'],
            number=data['number'],
        )
        save_changes(new_user)
        return new_user
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_student():
    return Student.query.all()


def get_a_student(number):
    return Student.query.filter_by(number=number).first()


def save_changes(data: Student) -> None:
    db.session.add(data)
    db.session.commit()
