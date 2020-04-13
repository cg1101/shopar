#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship, backref, synonym, deferred, column_property, object_session
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import case, text, func
from sqlalchemy.types import Integer, String
from marshmallow import Schema, fields

from . import database, mode
from .db import SS
from .db import database as db
from .schema import *


def set_schema(cls, schema_class, schema_key=None):
    if not issubclass(schema_class, Schema):
        raise TypeError('schema must be subclass of Schema')
    registry = cls.__dict__.get('_schema_registry', None)
    if registry is None:
        cls._schema_registry = {}
    cls._schema_registry[schema_key] = schema_class


def dump(cls, obj, use=None, extra=None, only=(), exclude=(),
        prefix=u'', strict=False, context=None, load_only=(), **kwargs):
    try:
        schema_class = cls._schema_registry.get(use, None)
    except:
        schema_class = None
    if schema_class is None:
        raise RuntimeError('schema class not found for {0}: key {1}'\
            .format(cls.__name__, use))
    s = schema_class(extra=extra, only=only, exclude=exclude,
            prefix=prefix, strict=strict, context=context)
    if isinstance(obj, list):
        many = True
    else:
        many = False
    marshal_result = s.dump(obj, many=many, **kwargs)
    return marshal_result.data

if mode == 'app':
    Base = database.Model
else:
    class MyBase(object):
        pass
    Base = declarative_base(cls=MyBase, metadata=metadata)
    Base.query = SS.query_property()

Base.set_schema = classmethod(set_schema)
Base.dump = classmethod(dump)


_names = set(locals().keys()) | {'_names'}


#
# Define model class and its schema (if needed) below
#
##########################################################################

# Language
class Language(Base):
    __table__ = t_languages

class LanguageSchema(Schema):
    class Meta:
        fields = ('language_id', 'language')


# Merchandise
class Merchandise(Base):
    __table__ = t_merchandises

class MerchandiseSchema(Schema):
    class Meta:
        fields = ('merchandise_id', 'inactive', 'brands_brand_id', 'categories_category_id')


# Order
class Order(Base):
    __table__ = t_orders

class OrderSchema(Schema):
    class Meta:
        fields = ('order_id', 'order_date', 'users_user_id', 'order_statuses_order_status_id',
            'is_paid_in_full', 'paid_amount', 'total_amount_include_tax', 'total_tax_amount',
            'discount_code', 'addresses_address_id', 'addresses_users_user_id')


# Product
class Product(Base):
    __table__ = t_products

class ProductSchema(Schema):
    class Meta:
        fields = ('product_id', 'sku', 'price_exclude_tax',
        'merchandises_merchandise_id', 'taxes_tax_id', 'quantity')


# Supplier
class Supplier(Base):
    __table__ = t_supplier

class SupplierSchema(Schema):
    class Meta:
        fields = ('supply_id', 'supplier_name', 'supplier_no', 'supplier_address',
            'supplier_suburb_city', 'supplier_state_area', 'supplier_contact_name',
            'supplier_contact_no', 'inactive')


# User
class User(Base):
    __table__ = t_users

class UserSchema(Schema):
    class Meta:
        fields = ('user_id', 'email', 'mobile', 'phone', 'password',
            'failed_login_attempts', 'last_failed_login', 'password_reset_hash',
            'password_request_at', 'external_source', 'external_id', 'inactive',
            'last_login')


##########################################################################
#
# Define model class and its schema (if needed) above
#

__all__ = list(set(locals().keys()) - _names)

for schema_name in [i for i in __all__ if i.endswith('Schema')]:
    klass_name = schema_name[:-6]
    if klass_name.find('_') >= 0:
        klass_name, schema_key = klass_name.split('_', 1)
        schema_key = schema_key.lower()
    else:
        schema_key = ''
    assert klass_name
    klass = locals()[klass_name]
    schema = locals()[schema_name]
    klass.set_schema(schema, schema_key or None)
