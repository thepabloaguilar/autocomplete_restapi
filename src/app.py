from flask import Flask

from autocomplete import get_tree
from api import customer

def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config['TESTING'] = True

    app.register_blueprint(
        customer.api_bp,
        url_prefix=customer.CUSTOMER_PREFIX)
    
    app.search_engine = get_tree()

    return app
