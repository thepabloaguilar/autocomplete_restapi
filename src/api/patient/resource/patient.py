from flask import current_app
from flask_restful import Resource
from ..parsers import patients_search_get_parser


class PatientsSearchResource(Resource):

    def _get_results(self, query):
        names = current_app.search_engine(query.lower().strip())
        return [name.title() for name in names]

    def get(self):
        args = patients_search_get_parser.parse_args()
        result = self._get_results(args.q)
        _return = {
            'query': args.q,
            'patients': result,
            'patients_count': len(result)
        }
        return _return
