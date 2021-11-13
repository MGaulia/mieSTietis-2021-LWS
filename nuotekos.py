from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)
api = Api(app)

nuotekos = pd.read_csv("kpi/nuotekos.csv")

result_nuotekos = {}
for city in set(nuotekos["city"]):
    temp = nuotekos[nuotekos["city"] == city]
    result_nuotekos[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

class nuotekos(Resource):
    def get(self):
        return result_nuotekos

api.add_resource(nuotekos, '/nuotekos')

if __name__ == '__main__':
    app.run(debug = True)
