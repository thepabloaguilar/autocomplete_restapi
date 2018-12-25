from flask_restful import Resource
from ..parsers import customer_get_parser


class CustomerSearchResource(Resource):

    def get(self):
        args = customer_get_parser.parse_args()
        return {'query': args.q}
