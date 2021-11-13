from flask import Flask, request
import pandas as pd
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/kpi")
def kpi():
    df=pd.read_pickle("../kpi_category_ranks.pkl")
    #query=request.args.get("category")
    #return query
    df_dict = df.to_dict("list")
    return json.dumps(df_dict)
