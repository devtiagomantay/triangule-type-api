from flask import Flask, jsonify, make_response, request
from triangle import calculate_triangle_type
from helper import get_values_from_request

app = Flask(__name__)


@app.route("/triangle-type", methods=["POST"])
def triangle_type():
    # TODO: validation of post body
    print('Request: ', request.json)
    dimensions = get_values_from_request(request, 'dimensions')
    res = '
    if dimensions:
        res = calculate_triangle_type(dimensions)

    return jsonify(message=res)


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def resource_not_found(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify(error='Not found!'), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)