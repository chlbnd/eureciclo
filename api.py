from flask import Flask, request

from Bottle import Bottle
from Gallon import Gallon

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '<p style="font-family:arial;font-size:35">eu<b>reciclo</b>: Teste para backend</h1><p style="font-family:arial">Informe seus galões e garrafas por JSON.</p>'

@app.route('/gallon/fill', methods=['POST'])
def fill_gallons():
    json = request.get_json()

    gallon = Gallon(json.get('gallon'))
    bottles = Bottle(json.get('bottle'))

    while gallon.liters >= bottles.smaller():
        gallon.fill(bottles)

    print(f" foram utilizadas as garrafas de {bottles.used} litros\n")

    return "ok"

app.run()