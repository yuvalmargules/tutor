from tutor import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from tutor.routes import home
from tutor.routes import model


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)

db.create_all()
=======
    manager.run()
    # app.run(debug=True)
>>>>>>> 954fd4845105b46bba7652256e5eb32bc5f1648a
