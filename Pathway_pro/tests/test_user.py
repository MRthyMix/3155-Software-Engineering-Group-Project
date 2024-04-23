from flask import Flask
from models.user import User
from db import *
from app import app
import pytest


@pytest.fixture(scope='module')
def create_user():
    user = User(
        id_= '1', 
        name='John Smith', 
        email='john.smith@gmail.com', 
        profile_pic='https://www.google.com', 
        major='Computer Science', 
        year='2023', 
        gpa='3.5', 
        advisor='Dr. Smith', 
        Enrollment_Status='Freshman', 
        level='Undergraduate', 
        program='Bachelors', 
        college='Engineering'
    )
    return user

def test_create_user(create_user):
    with app.app_context():
        assert User.get("1") is None
        User.create(create_user.id, create_user.name, create_user.email, create_user.profile_pic)
        user_in_database = User.get("1")
        assert user_in_database.id == create_user.id
        User.delete("1")
    
def test_update_user(create_user):
    with app.app_context():
        assert User.getAllAttributesByUserID("1") is None
        User.createUsingALlAttributes(
            create_user.id, 
            create_user.name, 
            create_user.email, 
            create_user.profile_pic, 
            create_user.major, 
            create_user.year, 
            create_user.gpa, 
            create_user.advisor, 
            create_user.Enrollment_Status, 
            create_user.level, 
            create_user.program, 
            create_user.college
        )
        assert User.getAllAttributesByUserID("1") is not None
        User.update("1", "Computer Engineering", "2024", "3.7", "Dr. Johnson", "Sophomore", "Graduate", "Masters", "Engineering")
        updated_user = User.getAllAttributesByUserID("1")
        assert updated_user.major == "Computer Engineering" and create_user.major != updated_user.major
        assert updated_user.year == "2024" and create_user.year != updated_user.year
        assert updated_user.gpa == "3.7" and create_user.gpa != updated_user.gpa
        assert updated_user.advisor == "Dr. Johnson" and create_user.advisor != updated_user.advisor
        assert updated_user.Enrollment_Status == "Sophomore" and create_user.Enrollment_Status != updated_user.Enrollment_Status
        assert updated_user.level == "Graduate" and create_user.level != updated_user.level
        assert updated_user.program == "Masters" and create_user.program != updated_user.program
        User.delete(create_user.id)

def test_delete_user(create_user):
    with app.app_context():
        assert User.get("1") is None
        User.createUsingALlAttributes(
            create_user.id, 
            create_user.name, 
            create_user.email, 
            create_user.profile_pic, 
            create_user.major, 
            create_user.year, 
            create_user.gpa, 
            create_user.advisor, 
            create_user.Enrollment_Status, 
            create_user.level, 
            create_user.program, 
            create_user.college
        )
        assert User.get("1") is not None
        User.delete("1")
        assert User.get("1") is None

    
