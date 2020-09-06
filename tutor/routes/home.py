from .. import app
from ..controllers import home, register, login, forms


@app.route('/')
def index_route():
    return home.home()

@app.route("/home")
def home():
    return home.home()

@app.route("/register", methods=[ 'GET', 'POST']) 
def register():
    return register.register()

@app.route("/login", methods=['GET', 'POST'])
def login():
    return login.login()