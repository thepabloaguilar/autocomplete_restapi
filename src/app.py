from flask import Flask

from api import customer

def create_app():
    app = Flask(__name__)

    app.register_blueprint(
        customer.api_bp,
        url_prefix=customer.CUSTOMER_PREFIX)

    return app
