import xmltodict
import requests
import re
import json
import pandas as pd



def get_dataset_ids(list_of_table_names):
    r = requests.get("https://osp-rs.stat.gov.lt/rest_xml/dataflow/")
    metadata_dict = dict(xmltodict.parse(r.text))
    dataset_ids = []
    
    for i in metadata_dict["mes:Structure"]["mes:Structures"]["str:Dataflows"]["str:Dataflow"]:
        matches = []
        for j in list_of_table_names:
            j = j.lower()
            j = re.sub(r'[^\w\s]','',j)
            j = re.sub(' +', ' ',j)
            name = i["com:Name"][0]["#text"].lower()
            name = re.sub(r'[^\w\s]','',name)
            name = re.sub(' +', ' ',name)
            matches.append(j in name)
        if any(matches):
            dataset_ids.append(i["@id"])
            
    return dataset_ids

def construct_links(dataset_ids,start_period="2015-01"):
    links = []
    link_beginning = "https://osp-rs.stat.gov.lt/rest_json/data/"

    for i in dataset_ids:
        links.append(link_beginning + i + "/?startPeriod=" + start_period)
    
    return links



miestai = ["Kauno m. sav.","Vilniaus m. sav.","Klaipėdos m. sav.","Šiaulių m. sav.","Panevežio m. sav.","Alytaus m. sav."]

def dataset_to_dataframe(link):
    r = requests.get(link)
    json_dict = r.json()
    skip = False
    
    if not json_dict["dataSets"][0]["observations"]:
        skip = True
    for i in json_dict["structure"]["attributes"]["dataSet"]:
        if i["id"] == "DS_REGIONAL":
            if i["values"][0]["id"]=="N":
                skip = True
      #  if i["id"] == "DS_TIME_FORMAT":
      #      if i["values"][0]["name"] not in ["Metai","Mokymo metai"]:
      #          skip = True
    
    if not skip:
        dimensions_dict = {}

        for i in json_dict["structure"]["dimensions"]["observation"]:
            dimensions_dict[i["name"]] = i["keyPosition"]

            
      #  if list(dimensions_dict.keys())[0] != "Administracinė teritorija":
       #     return "This dataset has an unusual spatial dimension"
        list_of_mappings = []

        for i in json_dict["structure"]["dimensions"]["observation"]:
            mapping_dict = {}
            for ind,j in enumerate(i["values"]):
                mapping_dict[str(ind)] = j["name"]
            list_of_mappings.append(mapping_dict)   

        rows = []

        for i in json_dict["dataSets"][0]["observations"].keys():
            rows.append(i.split(":"))

        df = pd.DataFrame(rows)
        for i, j in enumerate(list_of_mappings):
            df[i].replace(j,inplace=True)

        df.columns = dimensions_dict.keys()

        
        values = []

        for i in json_dict["dataSets"][0]["observations"].values():
            values.append(i[0])
        
        df["Reikšmė"]=pd.Series(values)

        df=df[df["Administracinė teritorija"].isin(miestai)]
        
        df.name = json_dict["structure"]["name"]
        
        return df
    else:
        print("Skipped")



#####


table_names = ["Perdirbtos komunalinės atliekos","Aplinkosaugos ir aplinkai palankių prekių bendroji","Viešosios komunalinių atliekų tvarkymo",
            "Teršalų, išmestų į aplinkos orą iš stacionarių taršos šaltinių","Ūkio, buities ir gamybos nuotekų išleidimas į paviršinius vandenis",
              "Vandens sunaudojimas"]
table_ids=get_dataset_ids(table_names)

table_ids




links=construct_links(table_ids)


#r = requests.get(links[1])
#json_dict = r.json()
#json_dict



df_list = []
for i in links:
    df_list.append(dataset_to_dataframe(i))







###



table_names = ["Nuolatinių gyventojų skaičius liepos 1 d."]
table_ids=get_dataset_ids(table_names)

links=construct_links(table_ids)

population_df = dataset_to_dataframe(links[0])


population_df = population_df[df.iloc[:,1] == "Miestas ir kaimas"].iloc[:,[0,3,4]]



df_list2 = []
for i in [0,1,3]:
    x = pd.merge(df_list[0],population_df,on=["Laikotarpis","Administracinė teritorija"])
    x["per_capita"]= x["Reikšmė_x"]/x["Reikšmė_y"]
    df_list2.append(x)


df_list2[0].to_pickle("nuoteku_isvalimas.pkl")
df_list2[1].to_pickle("vandens_panaudojimas.pkl")
df_list2[2].to_pickle("tersalai.pkl")