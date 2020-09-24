from tutor import app, db
from tutor.routes import home, course
from tutor.models.users import Users


def test_add_new_user():
    c = app.test_client()
    assert Users.query.all() == []
    user = {
        'username': 'test',
        'email': 'test@email.com',
        'password': '123',
        'confirm_password': '123',
        'submit': 'Sign Up'
    }
    c.post('/register', data=user, follow_redirects=True)
    assert Users.query.first().username == 'test_user'
