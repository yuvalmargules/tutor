from tutor import db
from tutor.models.course import Resource, Course
from tutor.models.users import Users


def create_test_user(username, email, password):
    user = Users(username=username, email=email, password=Users.hash_pass(password))
    db.session.add(user)
    db.session.commit()
    return search_user_name(username)


def login_test_user(client, email, password):
    login_user = {
        'email': email,
        'password': password,
        'submit': 'Login'
    }
    client.post('/login', data=login_user, follow_redirects=True)


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


def register_and_login(client):
    create_test_user(username="test", email="test@email.com", password="123")
    login_test_user(client, "test@email.com", "123")
