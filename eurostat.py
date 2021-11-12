def eurostat_dataframe(link):
    df_list = []
    years = ["2020","2019","2018"]
    for i in years:
        r = requests.get(link+i)
        json_dict = r.json()
        mapping_dict = json_dict["value"]

        dimensions_dict = {}
        for i,j in enumerate(json["dimension"]["cities"]["category"]["label"].values()):
            dimensions_dict[str(i)]=j
        
        df = pd.DataFrame.from_dict(mapping_dict,"index")
        df.reset_index(inplace=True)
        df.index=df["index"]
        df=df.reindex([str(i) for i in range(0,417)])
        df["index"].replace(dimensions_dict,inplace=True)
        df.name = list(json["dimension"]["indic_ur"]["category"]["label"].values())[0]
        df.columns = ["City","Value"]

        df_list.append(df)
        
    df = df_list[0]    
    for i in range(1,len(years)):
        df = df.fillna(df_list[i])
        
    return df[df.iloc[:,1].notna()]



def rank(dataframe, small_good = True):
    miestai = ["Vilnius","Kaunas","Alytus","Šiauliai","Marijampolė","Klaipeda","Siauliai","Panevezys"]
    nonna = len(dataframe)
    where=dataframe.City.isin(miestai)
    dataframe["Value"] = dataframe["Value"].rank(method="min",ascending = small_good)
    dataframe = dataframe[where]
    dataframe["Out of"] = nonna
    return dataframe

# Nuoroda rankiniu budu naudojant query builderi:
# https://ec.europa.eu/eurostat/web/json-and-unicode-web-services/getting-started/query-builder

df = eurostat_dataframe("http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/urb_ceduc?indic_ur=TE1001I&geoLevel=country&filterNonGeo=1&precision=1&time=")


ranked_df=rank(df)


json.loads(json.dumps(ranked_df.to_dict("list")))