from .. import app
from ..controllers import resources
from flask import request


@app.route("/resource/new", methods=['GET', 'POST'])
def new_resource():
    id = request.args.get('id')
    return resources.newResource(id)
