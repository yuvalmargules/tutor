from flask import render_template
from flask import Flask, Response, render_template, request, redirect, url_for
from .forms import resourceForm

# TODO: need to be handled by backend
def getCourseResources(id):
    pass


# TODO: need to be handled by backend
def getCourseName(id):
    pass


def showCoursePage(id):
    # name = getCourseName(id)
    # resources = getCourseResources(id)
    # Use dummy data, for now
    name = 'Python Workshop'
    resources = [
        {'id': 1, 'name': 'resource1', 'description': 'blala1', 'link': 'https://google.com'},
        {'id': 2, 'name': 'resource2', 'description': 'blala2', 'link': 'https://google.com'},
        {'id': 3, 'name': 'resource3', 'description': 'blala3', 'link': 'https://google.com'},
    ]
    return render_template('course.html', name=name, resources=resources)

def newResource():
    form = resourceForm()
    if form.validate_on_submit():
        return redirect(url_for('index_route'))
    return render_template('resource.html', form=form)
