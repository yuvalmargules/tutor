from tutor import app
from tutor.routes import home, course, resources # noqa
from tutor import db
from tutor.models.course import Resource, Course


def test_resource_create():
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['TESTING'] = True
    with app.test_client() as c:
        course_3 = Course(name='course_name')
        db.session.add(course_3)
        db.session.commit()
        resource = {
            'title': 'resource_name',
            'content': 'content',
            'link': 'www.google.com',
            'submit': 'Post'
        }
        c.post('/resource/new?id=3', data=resource, follow_redirects=True)
        test_resource = Resource.query.filter_by(title='resource_name').first()
        assert test_resource.title == 'resource_name'
        assert test_resource.content == 'content'
        assert test_resource.link == 'www.google.com'
    db.session.delete(test_resource)
    db.session.delete(course_3)
    db.session.commit()
