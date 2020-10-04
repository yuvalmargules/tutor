from tutor import db
from tutor.routes import home, course # noqa
from tutor.models.users import Users


def test_logout(client):
    # Test logout without user logged in
    response = client.get('/logout', follow_redirects=True)
    assert b'Tutor - Sharing Towards Excellence' in response.data
    # Create test user
    register_user = {
        'username': 'test',
        'email': 'test@email.com',
        'password': '123',
        'confirm_password': '123',
        'submit': 'Sign Up'
    }
    client.post('/register', data=register_user, follow_redirects=True)
    # Login test user
    login_user = {
        'email': 'test@email.com',
        'password': '123',
        'submit': 'Login'
    }
    client.post('/login', data=login_user, follow_redirects=True)
    # Logout user
    response = client.get('/logout', follow_redirects=True)
    assert b'Tutor - Sharing Towards Excellence' in response.data
    Users.query.delete()
    db.session.commit()
