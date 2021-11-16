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


def form_json_by_city(data, change = False):
    if type(data) == "str":
        data = pd.read_csv(data)

    if change == True:
        
        test=pd.merge(data[data["x"]==2020],data[data["x"]==2019],on="city")
        
        if all(test["total_x"] == test["total_y"]):
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
        data["y_change"] = data["y_change"].replace(np.inf, 0).replace(np.nan,0)
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


category_data = None
iscores_data = None
total_ranks_data = None
transportas_data = None
oras_data = None
siuksles_data = None
vanduo_data = None
total_data = None

def extract_category(weights):
    global category_data
    global iscores_data
    global total_ranks_data
    global transportas_data
    global oras_data
    global siuksles_data
    global vanduo_data
    global total_data
    

    iscores = pd.read_csv("kpi/indicators_scores.csv")
    
    trans = [2,10]
    water = [3,8,9]
    air = [5,6,7]
    trash = [3]
    categories = [trans,water,air,trash]
    
    for i,j in zip(categories,weights):
        iscores.iloc[:,i] = iscores.iloc[:,i] * j / 25 * 100 / sum(weights)
    iscores = iscores.round(2)
    
    iscores.to_csv("kpi/indicatos_scores_2.csv", index = False)
    
    
    category_data = iscores.copy()
    for i,j in enumerate(categories):
         category_data["cat"+str(i)]=category_data.iloc[:,j].sum(axis=1)
         
    category_dict = {"cat0":"transportas","cat1":"vanduo","cat2":"oras","cat3":"šiukšles"}
    category_data = category_data.rename(columns=category_dict).round(1)
    indices = [0,1]
    indices.extend(list(range(len(iscores.columns),len(iscores.columns)+len(categories)+1)))
    category_data["total"]= category_data.iloc[:,[2,3,4,5]].sum(axis=1)
    category_data = category_data.iloc[:,indices]


    total_ranks_data = category_data.copy()
    total_ranks_data.iloc[:,2:] = total_ranks_data.iloc[:,1:].groupby("x").rank(ascending=False)
    total_ranks_data = total_ranks_data[total_ranks_data["x"] == 2020]
    total_ranks_data = total_ranks_data[["city", "total"]].rename({'total': 'y'}, axis=1)

    vanduo_data = category_data[["city","vanduo","x"]].rename({'vanduo': 'y'}, axis=1)
   
    transportas_data = category_data[["city","transportas","x"]].rename({'transportas': 'y'}, axis=1)

    oras_data = category_data[["city","oras","x"]].rename({'oras': 'y'}, axis=1)

    siuksles_data = category_data[["city","šiukšles","x"]].rename({'šiukšles': 'y'}, axis=1)

    total_data = category_data[["city","total","x"]].rename({'total': 'y'}, axis=1)

"""
        CUSTOM
"""

class updateweights(Resource):
    def post(self):
        w = request.args.get('text', default=0, type=int)
        strw = str(w)
        weights = [int(strw[:2]), int(strw[2:4]), int(strw[4:6]), int(strw[6:8]) ]
        extract_category(weights)
        return 200

api.add_resource(updateweights, '/uw')

class lycatbar(Resource):
    def get(self):
        data = category_data
        data = data[data["x"] == 2020]
        data = data[["city", "transportas", "vanduo", "oras", "šiukšles"]]
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
        data = total_ranks_data
        result = {}
        for city in set(data["city"]):
            temp = data[data["city"] == city].to_dict(orient = "list")
            result[city] = {"y":temp["y"]}
        return result

api.add_resource(totalranks, '/totalranks')

class indicator_scores(Resource):
    def get(selfs):
        data = iscores_data
        data = data[data["x"] == 2020]
        cols = [col for col in data.columns if col not in ["city","x"]]
        result = {}
        for city in data.city:
            result[city] = [{col:list(data[data["city"] == city].loc[:,col])[0]} for col in cols]
        return result

api.add_resource(indicator_scores, '/indicator_scores')

"""
        NORMAL
"""
class nuotekos(Resource):
    def get(self):
        return form_json_by_city("modified/nuotekos.csv")

class kelioniu_kiekis(Resource):
    def get(self):
        return form_json_by_city("modified/kelioniu_kiekis.csv")

class tersalai_co(Resource):
    def get(self):
        return form_json_by_city("modified/oro_tersalai_co.csv")

class tersalai_no(Resource):
    def get(self):
        return form_json_by_city("modified/oro_tersalai_no.csv")

class tersalai_kietosios(Resource):
    def get(self):
        return form_json_by_city("modified/oro_tersalai_kietosios.csv")

class vandens_buiciai(Resource):
    def get(self):
        return form_json_by_city("modifed/vandens_sunaudojimas_buiciai.csv")

class vandens_pozeminis(Resource):
    def get(self):
        return form_json_by_city("modified/vandens_sunaudojimas_pozeminis.csv")

class viesojo_rida(Resource):
    def get(self):
        return form_json_by_city("modified/viesojo_rida.csv")

class vanduo(Resource):
    def get(self):
        return form_json_by_city(vanduo_data)

class transportas(Resource):
    def get(self):
        return form_json_by_city(transportas_data)

class oras(Resource):
    def get(self):
        return form_json_by_city(oras_data)

class siuksles(Resource):
    def get(self):
        return form_json_by_city(siuksles_data)

class total(Resource):
    def get(self):
        return form_json_by_city(total_data)

class kpi(Resource):
    def get(self):
        return form_json_by_city(total_data)



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
        return form_json_by_city("modified/nuotekos.csv", change= True)

class kelioniu_kiekis_change(Resource):
    def get(self):
        return form_json_by_city("modified/kelioniu_kiekis.csv", change= True)

class tersalai_co_change(Resource):
    def get(self):
        return form_json_by_city("modified/oro_tersalai_co.csv", change= True)

class tersalai_no_change(Resource):
    def get(self):
        return form_json_by_city("modified/oro_tersalai_no.csv", change= True)

class tersalai_kietosios_change(Resource):
    def get(self):
        return form_json_by_city("modified/oro_tersalai_kietosios.csv", change= True)

class vandens_buiciai_change(Resource):
    def get(self):
        return form_json_by_city("modified/vandens_sunaudojimas_buiciai.csv", change= True)

class vandens_pozeminis_change(Resource):
    def get(self):
        return form_json_by_city("modified/vandens_sunaudojimas_pozeminis.csv", change= True)

class viesojo_rida_change(Resource):
    def get(self):
        return form_json_by_city("modified/viesojo_rida.csv", change= True)

class vanduo_change(Resource):
    def get(self):
        return form_json_by_city(vanduo_data, change= True)

class transportas_change(Resource):
    def get(self):
        return form_json_by_city(transportas_data, change= True)

class oras_change(Resource):
    def get(self):
        return form_json_by_city(oras_data, change= True)

class siuksles_change(Resource):
    def get(self):
        return form_json_by_city(siuksles_data, change= True)

class total_change(Resource):
    def get(self):
        return form_json_by_city(total_data, change= True)

class kpi_change(Resource):
    def get(self):
        return form_json_by_city(total_data, change= True)

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

extract_category(weights)

if __name__ == '__main__':
    app.run(debug = True)