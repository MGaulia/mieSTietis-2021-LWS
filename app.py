from __future__ import division
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd
import numpy as np
from flask import request

def safe_div(x,y):
    if y == 0:
        return 0
    return x / y

def form_json_by_city(filepath, change = False):
    data = pd.read_csv(filepath)

    if change == True:
        if filepath == "kpi/siuksles.csv":
            year1 = 2019
            year2 = 2018
        else:
            year1 = 2020
            year2 = 2019
        data = pd.merge(
            data[data["x"] == year1],
            data[data["x"] == year2],
            on=["city"])
        data["y_change"] = round(100*round((data["y_x"]/data["y_y"])- 1,2),1)
        data["y_change"] = data["y_change"].replace(np.inf, 0)
        data["y_change"] = data["y_change"].replace(np.nan, 0)
        data["y_lastyear"] = data["y_x"]
        data = data.drop(["x_x", "y_x", "x_y", "y_y"], 1)
        result = {}
        for city in set(data["city"]):
            temp = data[data["city"] == city]
            result[city] = [{"y_lastyear":yly, "y_change": yc} for yly, yc in  zip(temp.y_lastyear, temp.y_change)]

        return result


    result = {}
    for city in set(data["city"]):
        temp = data[data["city"] == city].to_dict(orient = "list")
        result[city] = {"x":temp["x"], "y":temp["y"]}

    return result

app = Flask(__name__)
CORS(app)
api = Api(app)

def extract_categories(weights):
    cat = pd.read_csv("kpi/categories.csv")

    cat.iloc[:,[2,3,4,5]] = cat.iloc[:,[2,3,4,5]] * pd.Series(weights,index = cat.columns[[2,3,4,5]]) / 25 * 100 / sum(weights)
    cat["total"]= cat.iloc[:,[2,3,4,5]].sum(axis=1)
    cat = cat.round(2)

    cat.to_csv("kpi/categories_2.csv", index = False)

    iscores = pd.read_csv("kpi/indicators_scores.csv")

    trans = [2,10]
    water = [3,8,9]
    air = [4,5,6]
    trash = [7]
    categories = [trans,water,air,trash]
    for i,j in zip(categories,weights):
        iscores.iloc[:,i] = iscores.iloc[:,i] * j / 25 * 100 / sum(weights)

    iscores = iscores.round(2)
    iscores.to_csv("kpi/indicators_scores_2.csv", index = False)

    df_ranks = cat.copy()
    df_ranks.iloc[:,2:] = df_ranks.iloc[:,1:].groupby("x").rank(ascending=False)
    df_ranks = df_ranks[df_ranks["x"] == 2020]
    df_ranks = df_ranks[["city", "total"]]
    df_ranks = df_ranks.rename({"total":"y"}, axis = 1)
    df_ranks.to_csv("kpi/totalranks.csv", index = False)

    vanduo = cat[["city","vanduo","x"]]
    vanduo = vanduo.rename({'vanduo': 'y'}, axis=1)
    vanduo.to_csv("kpi/vanduo.csv", index = False)

    transportas = cat[["city","transportas","x"]]
    transportas = transportas.rename({'transportas': 'y'}, axis=1)
    transportas.to_csv("kpi/transportas.csv", index = False)

    oras = cat[["city","oras","x"]]
    oras = oras.rename({'oras': 'y'}, axis=1)
    oras.to_csv("kpi/oras.csv", index = False)

    siuksles = cat[["city","??iuk??les","x"]]
    siuksles = siuksles.rename({'??iuk??les': 'y'}, axis=1)
    siuksles.to_csv("kpi/siuksles.csv", index = False)

    total = cat[["city","total","x"]]
    total = total.rename({'total': 'y'}, axis=1)
    total.to_csv("kpi/total.csv", index = False)
    total.to_csv("kpi/kpi.csv", index = False)

"""
        CUSTOM
"""

class updateweights(Resource):
    def post(self):
        w = request.args.get('text', default=0, type=int)
        strw = str(w)
        weights = [int(strw[:2]), int(strw[2:4]), int(strw[4:6]), int(strw[6:8]) ]
        extract_categories(weights)
        return 200

api.add_resource(updateweights, '/uw')

class lycatbar(Resource):
    def get(self):
        data = pd.read_csv("kpi/categories_2.csv")
        #data["??iuk??les"] = list(data[data["x"] == 2019]["??iuk??les"])*6
        data = data[data["x"] == 2020]
        data = data[["city", "transportas", "vanduo", "oras", "??iuk??les"]]
        cols = [col for col in data.columns if col not in ["city", "x"]]
        result = {}
        for city in data.city:
            temp = {}
            for col in cols:
                temp[col] = list(data[data["city"] == city].loc[:,col])[0]
            result[city] = temp
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
        iscores = pd.read_csv("kpi/indicators_scores_2.csv")
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

class vandens_pozeminis(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_pozeminis.csv")

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
api.add_resource(vandens_pozeminis, '/vandens_pozeminis')
api.add_resource(viesojo_rida, '/viesojo_rida')
api.add_resource(vanduo, '/vanduo')
api.add_resource(transportas, '/transportas')
api.add_resource(oras, '/oras')
api.add_resource(siuksles, '/siuksles')
api.add_resource(total, '/total')
api.add_resource(kpi, '/kpi')

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

class vandens_pozeminis_change(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_pozeminis.csv", change= True)

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

class kpi_change(Resource):
    def get(self):
        return form_json_by_city("kpi/kpi.csv", change= True)

api.add_resource(nuotekos_change, '/nuotekos_change')
api.add_resource(kelioniu_kiekis_change, '/kelioniu_kiekis_change')
api.add_resource(tersalai_co_change, '/tersalai_co_change')
api.add_resource(tersalai_no_change, '/tersalai_no_change')
api.add_resource(tersalai_kietosios_change, '/tersalai_kietosios_change')
api.add_resource(vandens_buiciai_change, '/vandens_buiciai_change')
api.add_resource(vandens_pozeminis_change, '/vandens_pozeminis_change')
api.add_resource(viesojo_rida_change, '/viesojo_rida_change')
api.add_resource(vanduo_change, '/vanduo_change')
api.add_resource(transportas_change, '/transportas_change')
api.add_resource(oras_change, '/oras_change')
api.add_resource(siuksles_change, '/siuksles_change')
api.add_resource(total_change, '/total_change')
api.add_resource(kpi_change, '/kpi_change')

weights = [25, 25, 25, 25]
extract_categories(weights)

if __name__ == '__main__':
    app.run(debug = True)