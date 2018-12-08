
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, reqparse, fields, marshal

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'elizabeth':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access, please register first'}), 403)


def calculate_order_cost(order):
    """
        Helper function.
        Calculates the total cost of an order
    """
    order['total_cost'] = order['price'] * order['quantity']

#created sample data to be filled in our default orders
Orders = [
    {
        'id': 1,
        'order_name': u'pizza',
        'quantity': 1,
        'price': 15000,
        'order_status': u'pending'
        
    },
    {
        'id': 2,
        'order_name': u'chicken + chips',
        'quantity': 4,
        'price': 56000,
        'order_status': u'pending'
        
    }
]

order_fields = {
    'id': fields.Integer,
    'order_name': fields.String,
    'quantity':fields.Integer,
    'price':fields.Integer,
    'order_status': fields.String,
    'uri': fields.Url('order')
}


class OrderListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('order_name', type=str, required=True,
                                   help='No order order_name provided',
                                   location='json')
        self.reqparse.add_argument('quantity', type=int, required=True,
                                   help='please enter the quantity',
                                   location='json')
        self.reqparse.add_argument('price', type=int, required=True,
                                   help='please enter the price',
                                   location='json')
        self.reqparse.add_argument('order_status', type=str, default="",
                                   location='json')
        super(OrderListAPI, self).__init__()

    def get(self):
        return {'Orders': [marshal(order, order_fields) for order in Orders]}

    def post(self):
        args = self.reqparse.parse_args()
        order = {
            'id': Orders[-1]['id'] + 1,
            'order_name': args['order_name'],
            'quantity': args['quantity'],
            'price': args['price'],
            'order_status': args['order_status']
            
        }
        
        Orders.append(order)
        return {'status': 'order added successfully', 'order': marshal(order, order_fields)}, 201
      


class OrderAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('order_name', type=str, location='json')
        self.reqparse.add_argument('quantity', type=int, location='json')
        self.reqparse.add_argument('price', type=int, location='json')
        self.reqparse.add_argument('order_status', type=str, location='json')
        super(OrderAPI, self).__init__()

    def get(self, id):
        order = [order for order in Orders if order['id'] == id]
        if len(order) == 0:
            abort(404)
        return {'order': marshal(order[0], order_fields)}

    def put(self, id):
        order = [order for order in Orders if order['id'] == id]
        if len(order) == 0:
            abort(404)
        order = order[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                order[k] = v
        return {'message':'order changed successfully','order': marshal(order, order_fields)},201

    def delete(self, id):
        order = [order for order in Orders if order['id'] == id]
        if len(order) == 0:
            abort(404)
        Orders.remove(order[0])
        return {'result': 'Order deleted successfully'}



