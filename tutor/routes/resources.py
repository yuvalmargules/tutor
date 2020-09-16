from .. import app
from ..controllers import resources, forms


@app.route("/resource/new", methods=['GET', 'POST'])
def new_resource():
    return resources.newResource()
