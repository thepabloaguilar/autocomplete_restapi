import flask_restful

from flask import Blueprint
from .resource import patient

api_bp = Blueprint('patients', __name__)
api = flask_restful.Api(api_bp)

api.add_resource(patient.PatientsSearchResource, '/patients/search')
