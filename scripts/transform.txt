# Specify the tables that I want

table_names = ["Teršalų, išmestų į aplinkos orą iš stacionarių taršos šaltinių","Ūkio, buities ir gamybos nuotekų išleidimas į paviršinius vandenis",
              "Vandens sunaudojimas","Autobusų rida","Vidutiniškai vienam gyventojui tenka kelionių autobusais"]

table_ids=get_dataset_ids(table_names)

table_ids


links=construct_links(table_ids)

df_list = []
for i in links:
    df_list.append(dataset_to_dataframe(i))
    
df_list = [i for i in df_list if i is not None]



# I will also need the population data

table_names = ["Nuolatinių gyventojų skaičius liepos 1 d."]
table_ids=get_dataset_ids(table_names)

links=construct_links(table_ids)

population_df = dataset_to_dataframe(links[0])

population_df = population_df[population_df.iloc[:,1] == "Miestas ir kaimas"].iloc[:,[0,3,4]]



# Merging the tables with the population data

df_list_population = []
for i in df_list:
    x = pd.merge(i,population_df,on=["Laikotarpis","Administracinė teritorija"])
    x["per_thousand"]= x["Reikšmė_x"]/x["Reikšmė_y"]*1000
    x = x.replace("Klaipėdos m. sav.", "Klaipėda").replace("Kauno m. sav.", "Kaunas").replace("Vilniaus m. sav.", "Vilnius").replace("Panevėžio m. sav.", "Panevėžys").replace("Šiaulių m. sav.", "Šiauliai").replace("Alytaus m. sav.", "Alytus")
    x.drop(["Matavimo vienetai"], inplace = True,axis=1)
    df_list_population.append(x)


###

for i,j in enumerate(df_list_population):
    if i != 3:
        j.drop(["Reikšmė_x","Reikšmė_y"],axis=1,inplace=True)
        j.rename(columns={"Administracinė teritorija": "city","Laikotarpis":"x","per_thousand":"y"},inplace=True)


df_list_population[3] = df_list_population[3][df_list_population[3].iloc[:,1]=="Autobusai"]

df_list_population[3].drop(columns=["Reikšmė_y","per_thousand","Transporto rūšis (Autobusai)"],inplace=True)
df_list_population[3] = df_list_population[3].round(1)
df_list_population[3].rename(columns={"Administracinė teritorija": "city","Laikotarpis":"x","Reikšmė_x":"y"},inplace=True)

df_list_population[3].to_csv("modified/kelioniu_kiekis.csv",index=False)



###

grouped=df_list_population[4][df_list_population[4]["Teršalai"].isin(["Azoto oksidai, tonos","Anglies monoksidas, tonos","Kietosios medžiagos"])].round(1).groupby("Teršalai")

l=[grouped.get_group(x) for x in grouped.groups]
l=[i.iloc[:,[0,2,3]] for i in l]


l[0].to_csv("modified/tersalai_co.csv",index=False)
l[1].to_csv("modified/tersalai_no.csv",index=False)
l[2].to_csv("modified/tersalai_kietosios.csv",index=False)


###

grouped=df_list_population[1][df_list_population[1].iloc[:,0].isin(["Sunaudota požeminio vandens","Sunaudota vandens ūkio ir buities reikmėms"])].round(1).groupby("Vandens naudojimo paskirtis")

l=[grouped.get_group(x) for x in grouped.groups]
l=[i.iloc[:,[1,2,3]] for i in l]

l[1].to_csv("vandens_sunaudojimas_pozeminis.csv",index=False)
l[0].to_csv("vandens_sunaudojimas_buiciai.csv",index=False)


###

df_list_population[2] = df_list_population[2][df_list_population[2]["Reiso tipas"]=="Reguliarus reisas"].iloc[:,[1,2,3]].round(1)
df_list_population[2].to_csv("modified/viesojo_rida.csv",index=False)


###

nuotekos = df_list_population[0]
nuotekos = pd.merge(
    nuotekos[nuotekos["Išvalymas"] == "Išleista išvalytų iki normos nuotekų"],
    nuotekos[nuotekos["Išvalymas"] == "Iš viso išleista nuotekų"],
    on=["city", "x"])
nuotekos["y"] = round(100*nuotekos["y_x"]/nuotekos["y_y"],2)
nuotekos = nuotekos.drop(['Išvalymas_x', "Išvalymas_y", "y_x", "y_y"], 1)
nuotekos.to_csv("modified/nuotekos.csv", index = False)



# I also need a table from eurostat



waste = pd.read_csv("csv/urb_cenv_1_Data.csv",encoding = "ISO-8859-1",na_values=":")

miestai = ["Klaipeda","Siauliai","Vilnius","Kaunas","Panevezys","Alytus"]

waste = waste[waste["CITIES"].isin(miestai)][(waste["TIME"]>=2015)].iloc[:,[0,1,3]]

l = []
for i in waste["Value"]:
    l.append(float(i))

waste["Value"] = l

waste.rename(columns={"TIME":"x","CITIES":"city","Value":"y"},inplace=True)
waste.replace({"Panevezys":"Panevėžys","Siauliai":"Šiauliai","Klaipeda":"Klaipėda"},inplace=True)

population_df_2 = population_df.replace("Klaipėdos m. sav.", "Klaipėda").replace("Kauno m. sav.", "Kaunas").replace("Vilniaus m. sav.", "Vilnius").replace("Panevėžio m. sav.", "Panevėžys").replace("Šiaulių m. sav.", "Šiauliai").replace("Alytaus m. sav.", "Alytus")
population_df_2.rename(columns={"Administracinė teritorija":"city","Laikotarpis":"x","Reikšmė":"y"},inplace=True)
population_df_2["x"]=pd.to_numeric(population_df_2["x"])

waste = pd.merge(waste,population_df_2,on=["x","city"])
waste["y"]= waste["y_x"]/waste["y_y"]*1000

waste = waste.loc[:,["x","city","y"]]
waste.dropna().round(2).to_csv("modified/siuksles_surinktos.csv",index=False)