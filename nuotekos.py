from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd

def form_json_by_city(filepath):
    nuotekos = pd.read_csv(filepath)
    result = {}
    for city in set(nuotekos["city"]):
        temp = nuotekos[nuotekos["city"] == city]
        result[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

    return result

app = Flask(__name__)
CORS(app)
api = Api(app)


class nuotekos(Resource):
    def get(self):
        return form_json_by_city("kpi/nuotekos.csv")

api.add_resource(nuotekos, '/nuotekos')

if __name__ == '__main__':
    app.run(debug = True)
