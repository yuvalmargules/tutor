from .. import app
from ..controllers import model

# example to get all models
@app.route('/models')
def models_route():
    return model.getAllModels()


# example of a route with different methods
# This method create a new model object, and return a JSON with its details
@app.route('/model/store', methods=['GET', 'POST'])
def store_book_route():
    return model.createNewModel(modelName='model')
