import sys
import json
from flask import Flask, jsonify, make_response, request
from triangle import calculate_triangle_type
from flask_swagger_ui import get_swaggerui_blueprint
from flask_expects_json import expects_json

from helper import get_payload_dimensions

app = Flask(__name__)

# Swagger configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "triangle-type-api"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


def open_schema_file():
    """Open the schema file to validate the payload"""
    try:
        with open('schemas/dimensions_schema.json', 'r') as file:
            return json.load(file)
    except OSError:
        print('Could not open the schema file')
        sys.exit()


dimensions_schema = open_schema_file()


@app.route("/triangle-type", methods=["POST"])
@expects_json(dimensions_schema)
def triangle_type():
    """Calculates the triangle type based on the dimensions"""
    try:
        print('triangle-type endpoint Request: ', request.json)
        dimensions = get_payload_dimensions(request, 'dimensions')
        if dimensions:
            res = calculate_triangle_type(dimensions)
            return jsonify(message=res)

        return jsonify(message='Payload is invalid')
    except BaseException as e:
        print('Unknown error on triangle-type endpoint. Detail: ' + str(e))
        return jsonify(message='Unknown error')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.errorhandler(400)
def bad_request_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Bad request. Check the payload'}), 400)


@app.errorhandler(401)
def unauthorised_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def resource_not_found(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error':'Not found!'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)