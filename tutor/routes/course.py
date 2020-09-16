from .. import app
from ..controllers import course


@app.route("/courses", methods=['GET', 'POST'])
def courses_route():
    return course.showCourses()

@app.route("/addcourse", methods=['GET', 'POST'])
def addCourse_route():
    return course.addCourse()

@app.route('/course/<id>')
def get_course_info_route(id):
    return course.showCoursePage(id)
