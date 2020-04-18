
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
def list_products():
    products = m.Product.query.all()
    return jsonify({
        'value': m.Product.dump(products),
    })
    

@bp.route(_name + '/', methods=['POST'])
@api
@caps()
def create_product():
    data = MyForm(

    ).get_data()
    merchandise = m.Merchandise(**data)
    SS.add(merchandise)
    SS.commit()
    return jsonify({
        'value': m.Merchandise.dump(merchandise),
    })


@bp.route(_name + '/<int:product_id>', methods=['GET'])
@api
@caps()
def get_merchandise(product_id):
    product = m.Product.query.get(product_id)
    if not product:
        raise InvalidUsage(f'product {product_id} not found')
    return jsonify({
        'value': m.Merchandise.dump(product),
    })


