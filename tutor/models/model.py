from .. import db


class Model(db.Model):
    __tablename__ = 'models'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        return db.session.commit() 
    
    @staticmethod
    def getFirstById(id):
        return Model.query.filter_by(id=id).first()
    
    @staticmethod
    def getFirstByName(name):
        return Model.query.filter_by(name=name).first()
    
    @staticmethod
    def getAllById(id):
        return Model.query.filter_by(id=id).all()
    
    @staticmethod
    def getAllByName(name):
        return Model.query.filter_by(name=name).all()
