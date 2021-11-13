from flask import Flask, jsonify
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)

nuotekos = pd.read_csv("nuotekos.csv")
nuotekos = nuotekos.drop(['Rodiklis', "Matavimo vienetai"], 1)
nuotekos = nuotekos.replace("Sostinės regionas", "Vilniaus apskiritis")
nuotekos = pd.merge(
    nuotekos[nuotekos["Išvalymas"] == "Išleista išvalytų iki normos nuotekų"],
    nuotekos[nuotekos["Išvalymas"] == "Iš viso išleista nuotekų"],
    on=["Administracinė teritorija", "Laikotarpis"])
nuotekos["y"] = nuotekos["Reikšmė_y"]/nuotekos["Reikšmė_x"]
nuotekos = nuotekos.drop(['Išvalymas_x', "Išvalymas_y", "Reikšmė_x", "Reikšmė_y"], 1)
nuotekos = nuotekos.rename({'Laikotarpis': 'x', 'Administracinė teritorija': 'city'}, axis=1)
nuotekos

class population_by_cities(Resource):
    def get(self):
        return jsonify(nuotekos.to_dict(orient="records"))

api.add_resource(population_by_cities, '/nuotekos')  # www.linktoapi.com/populations

if __name__ == '__main__':
    app.run()
