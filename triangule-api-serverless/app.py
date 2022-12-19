from flask import Flask, jsonify, make_response, request
from triangle import calculate_triangle_type
from helper import get_values_from_request
app = Flask(__name__)


@app.route("/triangle-type", methods=["POST"])
def triangle_type():
    # TODO: validation of post body
    print('Request: ', request.json)
    dimensions = get_values_from_request(request, 'dimensions')
    res = 'Error!'
    if dimensions:
        res = calculate_triangle_type(dimensions)

    return jsonify(message=res)


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
