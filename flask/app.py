from flask import Flask, request
import pandas as pd
import json

app = Flask(__name__)

cities = ["Vilnius","Kaunas","Alytus","Šiauliai","Marijampolė","Klaipeda","Siauliai","Panevezys"]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/kpi")
def kpi():
    df=pd.read_pickle("../kpi_category_ranks.pkl")
    query=request.args.get("category")
    query_split = query.split("-")
    df["rank"]=df.loc[:,query_split].apply(sum,axis=1)
    df["rank"]=df["rank"].rank()
    df = df[df["city"].isin(cities)]
    df=df.loc[:,["city","rank"]]
    df_dict = df.to_dict("list")
    return json.dumps(df_dict)
