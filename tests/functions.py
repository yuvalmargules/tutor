from tutor import db, app
from tutor.models.course import Resource, Course
from tutor.models.users import Users
from flask_login import login_user



def create_test_user(username, email, password):
    user = Users(username=username, email=email, password=Users.hash_pass(password))
    db.session.add(user)
    db.session.commit()
    return user


def login_test_user(user):
    with app.app_context():
        with app.test_request_context():
            login_user(user)


def create_test_course(course_id, name):
    course = Course(id=course_id, name=name)
    db.session.add(course)
    db.session.commit()


def create_test_resource(title, content, link, course_id):
    resource = Resource(title=title, content=content, link=link, course_id=course_id)
    db.session.add(resource)
    db.session.commit()


def search_course_name(name):
    return Course.query.filter_by(name=name).first()


def search_user_name(username):
    return Users.query.filter_by(username=username).first()


def search_resource_title(title):
    return Resource.query.filter_by(title=title).first()
