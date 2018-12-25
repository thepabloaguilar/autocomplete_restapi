import flask_restful

from flask import Blueprint
from .resource import customer

api_bp = Blueprint('customer', __name__)
api = flask_restful.Api(api_bp)

CUSTOMER_PREFIX = '/customer'

api.add_resource(customer.CustomerSearchResource, '/search')
