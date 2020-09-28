from tutor import app, db, bcrypt
from tutor.routes import home, course
from tutor.models.users import Users


def test_logout():
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['TESTING'] = True
    with app.test_client() as c:
        # Test logout without user logged in
        response = c.get('/logout', follow_redirects=True)
        assert b'Tutor - Sharing Towards Excellence' in response.data
        # Create test user
        register_user = {
            'username': 'test',
            'email': 'test@email.com',
            'password': '123',
            'confirm_password': '123',
            'submit': 'Sign Up'
        }
        c.post('/register', data=register_user, follow_redirects=True)
        # Login test user
        login_user = {
            'email': 'test@email.com',
            'password': '123',
            'submit': 'Login'
        }
        response = c.get('/logout', follow_redirects=True)
        assert b'Tutor - Sharing Towards Excellence' in response.data
    Users.query.delete()
    db.session.commit()
