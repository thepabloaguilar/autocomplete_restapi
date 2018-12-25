from flask_restful import reqparse

customer_get_parser = reqparse.RequestParser()
customer_get_parser.add_argument('q', type=str, required=True)
