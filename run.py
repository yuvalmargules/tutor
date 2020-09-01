from tutor import app, db
from tutor.models import model


db.create_all()


from tutor.routes import home, model


if __name__ == "__main__":
    app.run(debug=True)
