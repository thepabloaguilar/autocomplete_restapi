from flask import Flask

from autocomplete import get_tree
from api import patient

def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config['TESTING'] = True

    app.register_blueprint(patient.api_bp)
    
    app.search_engine = get_tree()

    return app
