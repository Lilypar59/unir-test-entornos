import http.client

from flask import Flask

from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.substract(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route('/calc/multiply/<op_1>/<op_2>', methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(Calculator().multiply(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
@api_application.route('/calc/divide/<op_1>/<op_2>', methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(Calculator().divide(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
    
    
    # Nuevas operaciones
    
@api_application.route('/calc/power/<op_1>/<op_2>', methods=["GET"])
def power(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(Calculator().power(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
    
@api_application.route('/calc/mod/<op_1>/<op_2>', methods=["GET"])
def mod(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(Calculator().mod(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
    
@api_application.route('/calc/sqrt/<op_1>', methods=["GET"])
def sqrt(op_1):
    try:
        num_1= util.convert_to_number(op_1)
        return ("{}".format(Calculator().sqrt(num_1)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route('/calc/log10/<op_1>', methods=["GET"])
def log10(op_1):
    try:
        num_1= util.convert_to_number(op_1)
        return ("{}".format(Calculator().log10(num_1)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
    
@api_application.route('/calc/abs_value/<op_1>', methods=["GET"])
def abs_value(op_1):
    try:
        num_1= util.convert_to_number(op_1)
        return ("{}".format(Calculator().absValue(num_1)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
    
@api_application.route('/calc/avg/<numbers>', methods=["GET"])
def avg(numbers):
    try:
        nums = [float(n) for n in numbers.split(',')]
        return ("{}".format(Calculator().avg(nums)), http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route('/calc/max_value/<numbers>', methods=["GET"])
def max_value(numbers):
    try:
        nums = [float(n) for n in numbers.split(',')]
        return ("{}".format(Calculator().max_value(nums)), http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route('/calc/min_value/<numbers>', methods=["GET"])
def min_value(numbers):
    try:
        nums = [float(n) for n in numbers.split(',')]
        return ("{}".format(Calculator().min_value(nums)), http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route('/calc/factorial/<op_1>', methods=["GET"])
def factorial(op_1):
    try:
        num_1= util.convert_to_number(op_1)
        return ("{}".format(Calculator().factorial(num_1)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route('/calc/percent/<op_1>/<op_2>', methods=["GET"])
def percent(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(Calculator().percent(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
    
@api_application.route('/calc/inverse/<op_1>', methods=["GET"])
def inverse(op_1):
    try:
        num_1 = util.convert_to_number(op_1)
        return ("{}".format(Calculator().inverse(num_1)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)