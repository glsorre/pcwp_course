class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

class CarsOrchestrator:
    def __init__(self):
        self.cars = []
        self.cars.append(Car("Red", "Beetle", 1966))

    def append(self, color, model, year):
        self.cars.append(Car(color, model, year))

    def get(self):
        return self.cars

    def delete(self, index):
        self.cars.pop(index)


from base64 import b64encode
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

cars = CarsOrchestrator()

authorized_users = [
    {
        'username': "gsorrentino",
        'password': "password"
    }
]

def check_user_auth(header):
    encoded = header.split()[-1].encode("utf-8")
    if encoded in [b64encode((user['username'] + ":" + user['password']).encode("utf-8")) for user in authorized_users]:
        return True

def login_required(f):
    def decorated(*args, **kwargs):
        authorization_header = request.headers.get('Authorization')
        if authorization_header and check_user_auth(authorization_header):
            return f(*args, **kwargs)
        else:
            response = jsonify ({
                "401": "Unauthorized"
            })
            return response, 401
    return decorated  

def json_converter(o):
    if isinstance(o, Car):
        response = {}
        response['color'] = o.color
        response['model'] = o.model
        response['year'] = o.year
        return response

@app.route('/')
def hello():
    return jsonify({
        "status": 200,
        "data": json.loads(json.dumps(cars.get(), default=json_converter))
    })

@app.route('/append', methods=['POST'])
def append():
    body = request.get_json()
    cars.append(body['color'], body['model'], body['year'])

    return jsonify({
        "status": 200,
        "data": "OK"
    })

@app.route('/delete/<index>', methods=['DELETE'])
@login_required
def delete(index):
    cars.delete(int(index))

    return jsonify({
        "status": 200,
        "data": "OK"
    })

app.run(debug=True)
