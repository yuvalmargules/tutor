from flask import render_template, redirect, url_for
from .forms import RegistrationForm
from ..models.users import Users
from .. import db, bcrypt


def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = Users.hash_pass(form.password.data)
        user = Users(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login_route'))
    return render_template('register.html', form=form)
