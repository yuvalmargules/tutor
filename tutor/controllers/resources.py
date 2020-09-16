from flask import Flask, Response, render_template, request, redirect, url_for
from .forms import resourceForm


def newResource():
    form = resourceForm()
    if form.validate_on_submit():
        return redirect(url_for('index_route'))
    return render_template('resource.html', form=form)
