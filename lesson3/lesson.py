class Car:
    wheels = 0
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self._voltage = 12


    @property
    def voltage(self):
        return self._voltage


    @voltage.setter
    def voltage(self, volts):
        print("Warning: this can cause problems!")
        self._voltage = volts


    @voltage.deleter
    def voltage(self):
        print("Warning: the radio will stop working!")
        del self._voltage



my_car = Car("yellow", "Beetle", "1966")
my_other_car = Car("red", "corvette", "1999")

print(f"My car is {my_car.color}")
print(f"It has {my_car.wheels} wheels")
print(f"My other car is {my_other_car.color}")
print(f"It has {my_other_car.wheels} wheels")
Car.wheels = 4
print(f"My car has {my_car.wheels} wheels")
print(f"My other car has {my_other_car.wheels} wheels")
my_car.wheels = 5
print(f"My car has {my_car.wheels} wheels")
print(f"My other car has {my_other_car.wheels} wheels")
print(f"My car uses {my_car.voltage} volts")
my_car.voltage = 6
print(f"My car now uses {my_car.voltage} volts")
del my_car.voltage

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/<name>')
def hello_name(name):
    app.logger.info("***************************")
    app.logger.info(request.headers)
    app.logger.info(request.args)
    app.logger.info("***************************")
    return jsonify({
        "body": f"Hello {name}"
    })

app.run(debug=True)
