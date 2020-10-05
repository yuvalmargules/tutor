from tutor.routes import home, course # noqa
from functions import login_test_user, create_test_user


def test_logout(client):
    # Test logout without user logged in
    response = client.get('/logout', follow_redirects=True)
    assert b'Tutor - Sharing Towards Excellence' in response.data
    # Login test user
    user = create_test_user(username="test", email="test@email.com", password="123")
    login_test_user(user)
    # Logout user
    response = client.get('/logout', follow_redirects=True)
    assert b'Tutor - Sharing Towards Excellence' in response.data
