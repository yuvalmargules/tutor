from tutor import db
from tutor.routes import home, course # noqa
from tutor.models.course import Course


def test_addcourse(client):
    assert Course.query.all() == []
    course1 = {'name': 'Open Source'}
    client.post('/addcourse', data=course1, follow_redirects=True)
    test_course = Course.query.first()
    assert test_course.name == 'Open Source'
    Course.query.delete()
    db.session.commit()
