from flask_login import logout_user, current_user
from flask import redirect, url_for


def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('index_route'))
