from flask import Flask, Response, render_template, request, redirect, url_for
from forms import RegistrationForm, LoginForm

def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', form=form)