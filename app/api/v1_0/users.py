
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
def list_users():
    users = m.User.query.all()
    return jsonify({
        'value': m.User.dump(users),
    })
    

@bp.route(_name + '/', methods=['POST'])
@api
@caps()
def create_user():
    data = MyForm(

    ).get_data()
    user = m.User(**data)
    SS.add(user)
    SS.commit()
    return jsonify({
        'value': m.User.dump(user),
    })


@bp.route(_name + '/<int:user_id>', methods=['GET'])
@api
@caps()
def get_merchandise(user_id):
    user = m.User.query.get(user_id)
    if not user:
        raise InvalidUsage(f'user {user_id} not found')
    return jsonify({
        'value': m.User.dump(user),
    })


