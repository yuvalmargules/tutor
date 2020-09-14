from .. import app
from ..controllers import home, register, login, course


@app.route('/')
@app.route("/home")
def index_route():
    return home.home()


@app.route("/register", methods=[ 'GET', 'POST']) 
def register_route():
    return register.register()

@app.route("/login", methods=['GET', 'POST'])
def login_route():
    return login.login()

@app.route("/courses", methods=['GET', 'POST'])
def courses_route():
    return course.showCourses()

@app.route("/addcourse", methods=['GET', 'POST'])
def addCourse_route():
    return course.addCourse()