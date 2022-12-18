import boto3

from flask import Flask, jsonify, make_response, request
from triangle import calculate_triangle_type

REQUEST_HISTORY_TABLE_NAME = 'requests-history'

app = Flask(__name__)
client = boto3.client('dynamodb')


@app.route("/triangle-type", methods=["POST"])
def triangle_type():
    # TODO: validation of post body
    dimensions = request.json.get('dimensions')
    return jsonify(message=calculate_triangle_type(dimensions))


@app.route("/requests-history")
def get_requests_history():
    return jsonify(message='result')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
