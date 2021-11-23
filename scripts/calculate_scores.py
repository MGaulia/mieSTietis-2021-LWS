import os

files = os.listdir("modified")
files_main = [i.split(".")[0] for i in files]

df = pd.read_csv("modified/"+files[0]).rename(columns={"y":files_main[0]})
for i,j in enumerate(files[1:]):
    df = pd.merge(df,pd.read_csv("modified/"+j),on=["x","city"],how="outer").rename(columns={"y":files_main[i+1]})



# match categories to a column


trans = [2,10]
water = [3,8,9]
air = [5,6,7]
trash = [4]

categories = [trans,water,air,trash]

# To correctly handle indicators that we want to maximise

df.iloc[:,[2,3,10]] =  -1 * df.iloc[:,[2,3,10]]
df = df.groupby(['city'], sort=False).apply(lambda x: x.ffill())


grouped = df.groupby("x")
l=[grouped.get_group(x) for x in grouped.groups]



# Calculating the scores

df_scores = []

for df in l:
    df_min_max = df.iloc[:,2:]
    df.iloc[:,2:] = abs(((df_min_max-df_min_max.min())/(df_min_max.max()-df_min_max.min()))-1)
    for j,i in enumerate(categories):
        df.iloc[:,i] = df.iloc[:,i] * (25/len(i))
    df = df.round(2)
    df_scores.append(df.iloc[:,0:11])


pd.concat(df_scores).to_csv("kpi/indicator_scores.csv",index=False)