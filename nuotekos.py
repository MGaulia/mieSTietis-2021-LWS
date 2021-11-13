from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd



app = Flask(__name__)
CORS(app)
api = Api(app)



nuotekos = pd.read_csv("kpi/nuotekos.csv")
kelioniu_kiekis = pd.read_csv("kpi/kelioniu_kiekis.csv")
tersalai_co = pd.read_csv("kpi/oro_tersalai_co.csv")
tersalai_kietosios = pd.read_csv("kpi/oro_tersalai_kietosios.csv")
tersalai_no = pd.read_csv("kpi/oro_tersalai_no.csv")
vandens_buiciai = pd.read_csv("kpi/vandens_sunaudojimas_buiciai.csv")
vandens_energetikai = pd.read_csv("kpi/vandens_sunaudojimas_energetikai.csv")
viesoji_rida = pd.read_csv("kpi/viesojo_rida.csv")






result_nuotekos = {}
for city in set(nuotekos["city"]):
    temp = nuotekos[nuotekos["city"] == city]
    result_nuotekos[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

class nuotekos(Resource):
    def get(self):
        return result_nuotekos

api.add_resource(nuotekos, '/nuotekos')








result_kelioniu_kiekis = {}
for city in set(kelioniu_kiekis["city"]):
    temp = kelioniu_kiekis[kelioniu_kiekis["city"] == city]
    result_kelioniu_kiekis[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

class kelioniu_kiekis(Resource):
    def get(self):
        return result_kelioniu_kiekis

api.add_resource(kelioniu_kiekis, '/kelioniu_kiekis')






result_tersalai_co = {}
for city in set(tersalai_co["city"]):
    temp = tersalai_co[tersalai_co["city"] == city]
    result_tersalai_co[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

class tersalai_co(Resource):
    def get(self):
        return result_tersalai_co

api.add_resource(tersalai_co, '/tersalai_co')





result_tersalai_no = {}
for city in set(tersalai_no["city"]):
    temp = tersalai_no[tersalai_no["city"] == city]
    result_tersalai_no[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

class tersalai_no(Resource):
    def get(self):
        return result_tersalai_no

api.add_resource(tersalai_no, '/tersalai_no')





result_tersalai_kietosios = {}
for city in set(tersalai_kietosios["city"]):
    temp = tersalai_kietosios[tersalai_kietosios["city"] == city]
    result_tersalai_kietosios[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

class tersalai_kietosios(Resource):
    def get(self):
        return result_tersalai_kietosios

api.add_resource(tersalai_kietosios, '/tersalai_kietosios')





result_vandens_buiciai = {}
for city in set(vandens_buiciai["city"]):
    temp = vandens_buiciai[vandens_buiciai["city"] == city]
    result_vandens_buiciai[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

class vandens_buiciai(Resource):
    def get(self):
        return result_vandens_buiciai

api.add_resource(vandens_buiciai, '/vandens_buiciai')





result_vandens_energetikai = {}
for city in set(vandens_energetikai["city"]):
    temp = vandens_energetikai[vandens_energetikai["city"] == city]
    result_vandens_energetikai[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

class vandens_energetikai(Resource):
    def get(self):
        return result_vandens_energetikai

api.add_resource(vandens_energetikai, '/vandens_energetikai')






result_viesoji_rida = {}
for city in set(viesoji_rida["city"]):
    temp = viesoji_rida[viesoji_rida["city"] == city]
    result_viesoji_rida[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

class viesoji_rida(Resource):
    def get(self):
        return result_viesoji_rida
    
    

api.add_resource(nuotekos, '/nuotekos')
api.add_resource(tersalai_co, '/tersalai_co')
api.add_resource(tersalai_no, '/tersalai_no')
api.add_resource(tersalai_kietosios, '/tersalai_kietosios')
api.add_resource(tersalai_no, '/tersalai_no')
api.add_resource(kelioniu_kiekis, '/kelioniu_kiekis')
api.add_resource(viesoji_rida, '/viesoji_rida')



if __name__ == '__main__':
    app.run(debug = True)
