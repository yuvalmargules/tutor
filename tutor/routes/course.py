from .. import app
from ..controllers import course


@app.route('/course/<id>')
def get_course_info_route(id):
    return course.showCoursePage(id)

@app.route("/resource/new", methods=['GET', 'POST'])
def new_resource():
    return course.newResource()

