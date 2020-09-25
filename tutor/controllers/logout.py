from flask_login import logout_user
from flask import redirect, url_for


def logout():
    logout_user()
    return redirect(url_for('index_route'))
