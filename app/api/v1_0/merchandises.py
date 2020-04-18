
from flask import request, session, jsonify

import db.model as m
from db.db import SS
from app.api import api, caps, MyForm, Field, validators
from app.i18n import get_text as _
from . import api_1_0 as bp, InvalidUsage

_name = __file__.split('/')[-1].split('.')[0]


@bp.route(_name + '/', methods=['GET'])
@api
@caps()
def list_merchandises():
    merchandises = m.Merchandise.query.order_by(m.Merchandise.name).all()
    return jsonify({
        'value': m.Merchandise.dump(merchandises),
    })


@bp.route(_name + '/<int:merchandise_id>', methods=['GET'])
@api
@caps()
def get_merchandise(merchandise_id):
    merchandise = m.Merchandise.query.get(merchandise_id)
    if not merchandise:
        raise InvalidUsage(f'merchandise {merchandise_id} not found')
    return jsonify({
        'value': m.Merchandise.dump(merchandise),
    })


@bp.route(_name + '/', methods=['POST'])
@api
@caps()
def create_merchandise():
    data = MyForm(

    ).get_data()
    merchandise = m.Merchandise(**data)
    SS.add(merchandise)
    SS.commit()
    return jsonify({
        'value': m.Merchandise.dump(merchandise),
    })
