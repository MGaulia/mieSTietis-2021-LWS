from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd

def form_json_by_city(filepath, lastyear = False, change = False):
    data = pd.read_csv(filepath)

    if change == True:
        data = pd.merge(
            data[data["x"] == 2020],
            data[data["x"] == 2019],
            on=["city"])
        data["y"] = round(data["y_x"]/data["y_y"],5)
        data = data.drop(["x_x", "y_x", "x_y", "y_y"], 1)
        result = {}
        for city in set(data["city"]):
            temp = data[data["city"] == city]
            result[city] = [{"y":y} for y in  temp.y]
        return result

    if lastyear:
        data = data[data["x"] == 2020]

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

class kelioniu_kiekis(Resource):
    def get(self):
        return form_json_by_city("kpi/kelioniu_kiekis.csv")

class tersalai_co(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_co.csv")

class tersalai_no(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_no.csv")

class tersalai_kietosios(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_kietosios.csv")

class vandens_buiciai(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_buiciai.csv")

class vandens_energetikai(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_energetikai.csv")

class viesojo_rida(Resource):
    def get(self):
        return form_json_by_city("kpi/viesojo_rida.csv")

api.add_resource(nuotekos, '/nuotekos')
api.add_resource(kelioniu_kiekis, '/kelioniu_kiekis')
api.add_resource(tersalai_co, '/tersalai_co')
api.add_resource(tersalai_no, '/tersalai_no')
api.add_resource(tersalai_kietosios, '/tersalai_kietosios')
api.add_resource(vandens_buiciai, '/vandens_buiciai')
api.add_resource(vandens_energetikai, '/vandens_energetikai')
api.add_resource(viesojo_rida, '/viesojo_rida')


if __name__ == '__main__':
    app.run(debug = True)
