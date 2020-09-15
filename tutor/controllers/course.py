from flask import render_template
from flask import Flask, Response, render_template, request, redirect, url_for
from ..models.course import Course


def showCoursePage(id):
    course = Course.query.filter_by(id=id).first()
    name = course.name
    resources = course.resources
    courseId = id
    return render_template('course.html', name=name, resources=resources, id=courseId)
