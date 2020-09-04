from flask import Flask, request

from bottle import Bottle
from gallon import Gallon
from response import Response

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '<p style="font-family:arial;font-size:35">eu<b>reciclo</b>: ' \
           'Teste para backend</h1><p style="font-family:arial">Informe seus galões e garrafas por JSON.</p>'


@app.route('/gallon/fill', methods=['POST'])
def fill_gallons():
    json = request.get_json()

    gallons = Gallon(json.get('gallons'))
    bottles = Bottle(json.get('bottles'))
    bottles_used = []

    while gallons.liters > 0:
        dump = gallons.fill(bottles)
        bottles_used.append(dump)

    response = Response(gallons.gallons, bottles_used)
    return response.build_response()

app.run()
