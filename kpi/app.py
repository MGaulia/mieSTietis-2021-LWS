from __future__ import division
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd
import numpy as np

def safe_div(x,y):
    if y == 0:
        return 0
    return x / y

def form_json_by_city(filepath, lastyear = False, change = False):
    data = pd.read_csv(filepath)

    if change == True:
        if 2020 not in data.x:
            year1 = 2019
            year2 = 2018
        else:
            year1 = 2020
            year2 = 2019
        data = pd.merge(
            data[data["x"] == year1],
            data[data["x"] == year2],
            on=["city"])
        data["y_change"] = round(100*round(data["y_x"]/data["y_y"] - 1,5),1)
        data["y_change"] = data["y_change"].replace(np.inf, 0)
        data["y_lastyear"] = data["y_x"]
        data = data.drop(["x_x", "y_x", "x_y", "y_y"], 1)
        result = {}
        for city in set(data["city"]):
            temp = data[data["city"] == city]
            result[city] = [{"y_lastyear":yly, "y_change": yc} for yly, yc in  zip(temp.y_lastyear, temp.y_change)]

        return result

    if lastyear:
        if 2020 not in data.x:
            year = 2019
        else:
            year = 2020

        data = data[data["x"] == year]

    result = {}
    for city in set(data["city"]):
        temp = data[data["city"] == city].to_dict(orient = "list")
        result[city] = {"x":temp["x"], "y":temp["y"]}

    return result

app = Flask(__name__)
CORS(app)
api = Api(app)


"""
        CUSTOM
"""
class lycatbar(Resource):
    def get(self):
        data = pd.read_csv("kpi/lycatbar.csv")
        cols = [col for col in data.columns if col not in ["city", "x"]]
        result = {}
        for city in data.city:
            result[city] = [{col:list(data[data["city"] == city].loc[:,col])[0]} for col in cols]
        return result

api.add_resource(lycatbar, '/catbar')

class totalranks(Resource):
    def get(self):
        data = pd.read_csv("kpi/totalranks.csv")
        result = {}
        for city in set(data["city"]):
            temp = data[data["city"] == city].to_dict(orient = "list")
            result[city] = {"y":temp["y"]}
        return result

api.add_resource(totalranks, '/totalranks')

class indicator_scores(Resource):
    def get(selfs):
        iscores = pd.read_csv("kpi/indicators_scores.csv")
        iscores["siuksles_surinktos"] = list(iscores[iscores["x"] == 2019]["siuksles_surinktos"])*6
        iscores = iscores[iscores["x"] == 2020]
        cols = [col for col in iscores.columns if col not in ["city","x"]]
        result = {}
        for city in iscores.city:
            result[city] = [{col:list(iscores[iscores["city"] == city].loc[:,col])[0]} for col in cols]
        return result

api.add_resource(indicator_scores, '/indicator_scores')

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

class vanduo(Resource):
    def get(self):
        return form_json_by_city("kpi/vanduo.csv")

class transportas(Resource):
    def get(self):
        return form_json_by_city("kpi/transportas.csv")

class oras(Resource):
    def get(self):
        return form_json_by_city("kpi/oras.csv")

class siuksles(Resource):
    def get(self):
        return form_json_by_city("kpi/siuksles.csv")

class total(Resource):
    def get(self):
        return form_json_by_city("kpi/total.csv")

class kpi(Resource):
    def get(self):
        return form_json_by_city("kpi/kpi.csv")


api.add_resource(nuotekos, '/nuotekos')
api.add_resource(kelioniu_kiekis, '/kelioniu_kiekis')
api.add_resource(tersalai_co, '/tersalai_co')
api.add_resource(tersalai_no, '/tersalai_no')
api.add_resource(tersalai_kietosios, '/tersalai_kietosios')
api.add_resource(vandens_buiciai, '/vandens_buiciai')
api.add_resource(vandens_energetikai, '/vandens_energetikai')
api.add_resource(viesojo_rida, '/viesojo_rida')
api.add_resource(vanduo, '/vanduo')
api.add_resource(transportas, '/transportas')
api.add_resource(oras, '/oras')
api.add_resource(siuksles, '/siuksles')
api.add_resource(total, '/total')
api.add_resource(kpi, '/kpi')

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

class vanduo_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/vanduo.csv", lastyear= True)

class transportas_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/transportas.csv", lastyear= True)

class oras_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/oras.csv", lastyear= True)

class siuksles_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/siuksles.csv", lastyear= True)

class total_lastyear(Resource):
    def get(self):
        return form_json_by_city("kpi/total.csv", lastyear= True)

api.add_resource(nuotekos_lastyear, '/nuotekos_lastyear')
api.add_resource(kelioniu_kiekis_lastyear, '/kelioniu_kiekis_lastyear')
api.add_resource(tersalai_co_lastyear, '/tersalai_co_lastyear')
api.add_resource(tersalai_no_lastyear, '/tersalai_no')
api.add_resource(tersalai_kietosios_lastyear, '/tersalai_kietosios_lastyear')
api.add_resource(vandens_buiciai_lastyear, '/vandens_buiciai_lastyear')
api.add_resource(vandens_energetikai_lastyear, '/vandens_energetikai_lastyear')
api.add_resource(viesojo_rida_lastyear, '/viesojo_rida_lastyear')
api.add_resource(vanduo_lastyear, '/vanduo_lastyear')
api.add_resource(transportas_lastyear, '/transportas_lastyear')
api.add_resource(oras_lastyear, '/oras_lastyear')
api.add_resource(siuksles_lastyear, '/siuksles_lastyear')
api.add_resource(total_lastyear, '/total_lastyear')
"""
        CHANGE
"""
class nuotekos_change(Resource):
    def get(self):
        return form_json_by_city("kpi/nuotekos.csv", change= True)

class kelioniu_kiekis_change(Resource):
    def get(self):
        return form_json_by_city("kpi/kelioniu_kiekis.csv", change= True)

class tersalai_co_change(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_co.csv", change= True)

class tersalai_no_change(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_no.csv", change= True)

class tersalai_kietosios_change(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_kietosios.csv", change= True)

class vandens_buiciai_change(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_buiciai.csv", change= True)

class vandens_energetikai_change(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_energetikai.csv", change= True)

class viesojo_rida_change(Resource):
    def get(self):
        return form_json_by_city("kpi/viesojo_rida.csv", change= True)

class vanduo_change(Resource):
    def get(self):
        return form_json_by_city("kpi/vanduo.csv", change= True)

class transportas_change(Resource):
    def get(self):
        return form_json_by_city("kpi/transportas.csv", change= True)

class oras_change(Resource):
    def get(self):
        return form_json_by_city("kpi/oras.csv", change= True)

class siuksles_change(Resource):
    def get(self):
        return form_json_by_city("kpi/siuksles.csv", change= True)

class total_change(Resource):
    def get(self):
        return form_json_by_city("kpi/total.csv", change= True)

api.add_resource(nuotekos_change, '/nuotekos_change')
api.add_resource(kelioniu_kiekis_change, '/kelioniu_kiekis_change')
api.add_resource(tersalai_co_change, '/tersalai_co_change')
api.add_resource(tersalai_no_change, '/tersalai_no_change')
api.add_resource(tersalai_kietosios_change, '/tersalai_kietosios_change')
api.add_resource(vandens_buiciai_change, '/vandens_buiciai_change')
api.add_resource(vandens_energetikai_change, '/vandens_energetikai_change')
api.add_resource(viesojo_rida_change, '/viesojo_rida_change')
api.add_resource(vanduo_change, '/vanduo_change')
api.add_resource(transportas_change, '/transportas_change')
api.add_resource(oras_change, '/oras_change')
api.add_resource(siuksles_change, '/siuksles_change')
api.add_resource(total_change, '/total_change')

if __name__ == '__main__':
    app.run(debug = True)