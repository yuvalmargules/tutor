from .. import app
from ..controllers import course


@app.route('/course/<id>')
def get_course_info_route(id):
    return course.showCoursePage(id)
