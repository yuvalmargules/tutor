from tutor.models.model import Model
from tutor import db

def test_add_new_model():
    model = Model(name='tester')
    assert model.name == 'tester'
    db.session.add(model)
    db.session.commit()
    assert Model.query.filter_by(name='tester').first().name == 'tester'
    db.session.delete(model)
    db.session.commit()
    assert Model.query.filter_by(name='tester').all() == []
    