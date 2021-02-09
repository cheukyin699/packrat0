import os
import uuid
from flask import Blueprint, jsonify, abort, request

from packrat0.models import db, Box, BoxImage
from packrat0.secrets import UPLOAD_FOLDER

api_blueprint = Blueprint('API blueprints', __name__, url_prefix='/api')

@api_blueprint.route('/boxes')
def get_boxes():
    page = int(request.args.get('page'))    # type: ignore
    return jsonify(Box.query.paginate(page=page, max_per_page=30))

@api_blueprint.route('/boxes/<int:box_id>')
def get_box(box_id):
    res = Box.query.filter(Box.id == box_id).all()
    if len(res) != 1:
        abort(404)
    else:
        return res[0]

@api_blueprint.route('/boxes', methods=['POST'])
def add_box():
    description = request.form.get('box_description', '')
    b = Box(description=description)

    for f in request.files.values():
        print(f)
        basename = str(uuid.uuid4())
        path = os.path.join(UPLOAD_FOLDER, basename)
        f.save(path)

        img = BoxImage(path=path)
        b.images.append(img)

    db.session.add(b)
    db.session.commit()

    return jsonify({
        'info': 'Added box with %d connected images.' % len(request.files.values())
    })
