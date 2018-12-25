from flask import Flask
from flasgger import Swagger

from autocomplete import get_tree
from api import patient

def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config['TESTING'] = True

    app.register_blueprint(patient.api_bp)
    
    app.search_engine = get_tree()

    app.config['SWAGGER'] = {
        'uiversion': 3,
        'swagger_version': '3.0',
        'title': 'Autocomplete RESTApi',
        'specs_route': '/docs/',
        'description': 'Documentação para a API de Busca de Pacientes',
    }

    Swagger(app)

    return app
