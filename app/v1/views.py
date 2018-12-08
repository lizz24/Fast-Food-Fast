from flask import Flask, jsonify, abort, make_response
from app.v1.orders import OrderAPI, OrderListAPI
from flask_restful import Api

app = Flask(__name__, static_url_path="")
api = Api(app)

api.add_resource(OrderListAPI, '/api/v1/orders', endpoint='orders')
api.add_resource(OrderAPI, '/api/v1/orders/<int:id>', endpoint='order')
