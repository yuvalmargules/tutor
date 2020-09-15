from .. import app
from ..controllers import course, resources
from flask import request


@app.route('/course')
def get_course_info_route():
    id = request.args.get('id')
    return course.showCoursePage(id)
