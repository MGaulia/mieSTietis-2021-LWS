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
        data["y"] = round(100*round(data["y_x"]/data["y_y"] - 1,5),3)
        data = data.drop(["x_x", "y_x", "x_y", "y_y"], 1)
        result = {}
        for city in set(data["city"]):
            temp = data[data["city"] == city]
            result[city] = [{"y":y} for y in  temp.y]
        return result

    if lastyear:
        data = data[data["x"] == 2020]

    result = {}
    for city in set(data["city"]):
        temp = data[data["city"] == city]
        result[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

    return result

app = Flask(__name__)
CORS(app)
api = Api(app)

"""
        NORMAL
"""
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
"""
        LAST-YEAR
"""
class nuotekos_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/nuotekos.csv", lastyear= True)

class kelioniu_kiekis_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/kelioniu_kiekis.csv", lastyear= True)

class tersalai_co_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_co.csv", lastyear= True)

class tersalai_no_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_no.csv", lastyear= True)

class tersalai_kietosios_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_kietosios.csv", lastyear= True)

class vandens_buiciai_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_buiciai.csv", lastyear= True)

class vandens_energetikai_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_energetikai.csv", lastyear= True)

class viesojo_rida_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/viesojo_rida.csv", lastyear= True)

api.add_resource(nuotekos_lastyear, '/nuotekos_lastyear')
api.add_resource(kelioniu_kiekis_lastyear, '/kelioniu_kiekis_lastyear')
api.add_resource(tersalai_co_lastyear, '/tersalai_co_lastyear')
api.add_resource(tersalai_no_lastyear, '/tersalai_no')
api.add_resource(tersalai_kietosios_lastyear, '/tersalai_kietosios_lastyear')
api.add_resource(vandens_buiciai_lastyear, '/vandens_buiciai_lastyear')
api.add_resource(vandens_energetikai_lastyear, '/vandens_energetikai_lastyear')
api.add_resource(viesojo_rida_lastyear, '/viesojo_rida_lastyear')
"""
        CHANGE
"""
class nuotekos_change(Resource):
    def get(self):
        return form_json_by_city("kpi/nuotekos.csv", change= True)

class kelioniu_kiekis_change(Resource):
    def get(self):
        return form_json_by_city("kpi/kelioniu_kiekis.csv")

class tersalai_co_change(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_co.csv")

class tersalai_no_change(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_no.csv")

class tersalai_kietosios_change(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_kietosios.csv")

class vandens_buiciai_change(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_buiciai.csv")

class vandens_energetikai_change(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_energetikai.csv")

class viesojo_rida_change(Resource):
    def get(self):
        return form_json_by_city("kpi/viesojo_rida.csv")

api.add_resource(nuotekos_change, '/nuotekos_change')
api.add_resource(kelioniu_kiekis_change, '/kelioniu_kiekis_change')
api.add_resource(tersalai_co_change, '/tersalai_co_change')
api.add_resource(tersalai_no_change, '/tersalai_no_change')
api.add_resource(tersalai_kietosios_change, '/tersalai_kietosios_change')
api.add_resource(vandens_buiciai_change, '/vandens_buiciai_change')
api.add_resource(vandens_energetikai_change, '/vandens_energetikai_change')
api.add_resource(viesojo_rida_change, '/viesojo_rida_change')

if __name__ == '__main__':
    app.run(debug = True)
