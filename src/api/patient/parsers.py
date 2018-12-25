from flask_restful import reqparse

patients_search_get_parser = reqparse.RequestParser()
patients_search_get_parser.add_argument('q', type=str, required=True)
