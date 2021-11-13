ids = ["EN3003V","EN3013V","EN4008V","EN5207V","EN5205V","TT1080V","TT1057I","TT1079V"]


import time

def eurostat_dataframe(link):
    time.sleep(2)
    df_list = []
    years = ["2020","2019","2018","2017","2016","2015","2014","2013","2012","2011"]
    
    continue_count = 0
    for i in years:
        time.sleep(1)

        try:
            r = requests.get(link+i)
        except Error:
            continue
        json_dict = r.json()
        try:
            mapping_dict = json_dict["value"]
        except Error:
            continue

        dimensions_dict = {}
        for i,j in enumerate(json_dict["dimension"]["cities"]["category"]["label"].values()):
            dimensions_dict[str(i)]=j
        
        df = pd.DataFrame.from_dict(mapping_dict,"index")
        if len(df) == 0:
            continue_count = continue_count+1
            continue
        df.reset_index(inplace=True)
        df.index=df["index"]
        df=df.reindex([str(i) for i in range(0,len(json_dict["dimension"]["cities"]["category"]["index"]))])
        df["index"].replace(dimensions_dict,inplace=True)
        value_name = list(json_dict["dimension"]["indic_ur"]["category"]["label"].values())[0]
        df.columns = ["city",value_name]

        df_list.append(df)
        
    df = df_list[0]    
    for i in range(1,len(years)-continue_count):
        df = df.fillna(df_list[i])
        
    return df[df.iloc[:,1].notna()]


links =  ["http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/urb_cenv?indic_ur=" + i + "&geoLevel=city&filterNonGeo=1&precision=1&time=" for i in ids[0:5]]
links.extend(["http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/urb_ctran?indic_ur=" + i + "&geoLevel=city&filterNonGeo=1&precision=1&time=" for i in ids[5:]])


df_list = []

for i in links:
    df_list.append(eurostat_dataframe(i))



def rank(dataframe):
    cities = ["Vilnius","Kaunas","Alytus","Šiauliai","Marijampolė","Klaipeda","Siauliai","Panevezys"]
    where=dataframe.city.isin(cities)
    small_good = [1,2,6,7]
    for i,j in enumerate(dataframe):
        if i in small_good:
            dataframe[j] = dataframe[j].rank(method="min",ascending = True)
        elif i > 0:
            dataframe[j] = dataframe[j].rank(method="min",ascending = True)
    dataframe = dataframe[where]
    return dataframe



df_list[2] = df_list[2].append({"city":"Vilnius",df_list[2].columns[1]:df_list[2].iloc[:,1].mean()},ignore_index=True)
df_list[4] = df_list[4].append({"city":"Vilnius",df_list[4].columns[1]:df_list[4].iloc[:,1].mean()},ignore_index=True)



import numpy as np

cities = df_list[0]["city"]
for i in df_list[1:]:
    cities = np.intersect1d(cities,i["city"])



population = eurostat_dataframe("http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/urb_cpop1?indic_ur=DE1001V&geoLevel=city&filterNonGeo=1&precision=1&time=")

population = population[population.city.isin(cities)]

df_list2 = list(range(0,len(df_list)))

for i in [0,1,7]:
    df_list2[i] = pd.merge(df_list[i],population,on="city")
    df_list2[i].iloc[:,1] = df_list2[i].iloc[:,1] / df_list2[i].iloc[:,2]
    df_list2[i].drop([df_list2[i].columns[2]],axis=1,inplace=True)
    
    
for i in [0,1,7]:
    df_list[i] = df_list2[i]


final = df_list[0][df_list[0].city.isin(cities)]
for i in df_list[1:]:
    final = pd.merge(final,i[i.city.isin(cities)],on="city")



ranked = rank(final)

ranked.to_pickle("kpi.pkl")






###


def rank(dataframe):
    #cities = ["Vilnius","Kaunas","Alytus","Šiauliai","Marijampolė","Klaipeda","Siauliai","Panevezys"]
    #where=dataframe.city.isin(cities)
    small_good = [1,2,6,7]
    for i,j in enumerate(dataframe):
        if i in small_good:
            dataframe[j] = dataframe[j].rank(method="min",ascending = True)
        elif i > 0:
            dataframe[j] = dataframe[j].rank(method="min",ascending = True)
    #dataframe = dataframe[where]
    return dataframe

ranked = rank(final)


ranked["waste"]=ranked.iloc[:,1:4].apply(sum,axis=1)
ranked["greenery"]=ranked.iloc[:,4:6].apply(sum,axis=1)
ranked["transport"]=ranked.iloc[:,6:].apply(sum,axis=1)


for i in [9,10,11]:
        ranked.iloc[:,i] = ranked.iloc[:,i].rank(method="min",ascending = True)
        ranked.iloc[:,i] = ranked.iloc[:,i].rank(method="min",ascending = True)
ranked = ranked.iloc[:,[0,9,10,11]]



ranked.to_pickle("category_ranks.pkl")