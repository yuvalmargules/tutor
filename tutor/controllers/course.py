from flask import render_template, redirect, url_for
from .forms import AddCourse


def addCourse():
    form = AddCourse()
    if form.validate_on_submit():
        return redirect(url_for('courses_route'))
    return render_template('addcourse.html', form=form)



# TODO: need to be handled by backend
def getCourseResources(id):
    pass


# TODO: need to be handled by backend
def getCourseName(id):
    pass


def showCourses():
    # get courses from data base into a list
    courses = [
        {'id': 1, 'title': 'Course 1' },
        {'id': 2, 'title': 'Course 2' },
        {'id': 3, 'title': 'Course 3' }
    ]
    return render_template('courses.html', courses=courses)


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
