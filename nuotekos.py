from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import pandas as pd



def form_json_by_city(filepath):
    kelioniu_kiekis = pd.read_csv(filepath)
    result = {}
    for city in set(kelioniu_kiekis["city"]):
        temp = kelioniu_kiekis[kelioniu_kiekis["city"] == city]
        result[city] = [{"x":x, "y":y} for x,y in zip(temp.x, temp.y)]

    return result


app = Flask(__name__)
CORS(app)
api = Api(app)


class nuotekos(Resource):
    def get(self):
        return form_json_by_city("kpi/nuotekos.csv")

api.add_resource(nuotekos, '/nuotekos')



class kelioniu_kiekis(Resource):
    def get(self):
        return form_json_by_city("kpi/kelioniu_kiekis.csv")

api.add_resource(kelioniu_kiekis, '/kelioniu_kiekis')



class tersalai_co(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_co.csv")

api.add_resource(tersalai_co, '/tersalai_co')



class tersalai_no(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_no.csv")

api.add_resource(tersalai_no, '/tersalai_no')


class tersalai_kietosios(Resource):
    def get(self):
        return form_json_by_city("kpi/oro_tersalai_kietosios.csv")

api.add_resource(tersalai_kietosios, '/tersalai_kietosios')


class vandens_buiciai(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_buiciai.csv")

api.add_resource(vandens_buiciai, '/vandens_buiciai')


class vandens_energetikai(Resource):
    def get(self):
        return form_json_by_city("kpi/vandens_sunaudojimas_energetikai.csv")

api.add_resource(vandens_energetikai, '/vandens_energetikai')


class viesojo_rida(Resource):
    def get(self):
        return form_json_by_city("kpi/viesojo_rida.csv")

api.add_resource(viesojo_rida, '/viesojo_rida')





if __name__ == '__main__':
    app.run(debug = True)
