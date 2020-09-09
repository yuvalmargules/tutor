from .. import db
from datetime import datetime


class Model(db.Model):
    __tablename__ = 'models'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name
        }

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    #posts = db.relationship('Resources', backref='user', lazy=True)

    def __repr__(self):
        return "'id': {0}, 'username': {1}, 'email': {2}".format(self.id, self.username, self.email)

class LookupCategories(db.Model):
    #__tablename__ = 'lookupcategory'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    #value = db.relationship('LookupValues', backref='category', lazy=True)


class LookupValues(db.Model):
    #__tablename__ = 'lookupvalue'

    id = db.Column(db.Integer, primary_key=True)
    #category_id = db.Column(db.Integer, db.ForeignKey('lookupcategory.id') ,nullable=False)
    value = db.Column(db.String(255), nullable=False)


class Resources(db.Model):
    #__tablename__ = 'resource'

    id = db.Column(db.Integer, primary_key=True)
    #course_id = db.Column(db.Integer, db.ForeignKey('lookupvalue.id') ,nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #tags = db.Column(db.Integer, db.ForeignKey('lookupvalue.id'))
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return {
            'User': self.user_id, 
            'Content': self.content,
            'Timestamp': self.timestamp
        }

