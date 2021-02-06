import numpy as np
import pandas as pd
import pickle
import re

df_bilboard = pd.read_csv("test.csv", sep=",")

df = df_bilboard['title'].unique()
liste = []
dic_final = {}

for i in range(len(df)):
    for j in range(len(df_bilboard['title'])):
        if df[i] == df_bilboard['title'][j]:
            liste.append((df_bilboard['date'][j],df_bilboard['rank'][j]))
    
    print('nom de la musique {}, place dans la liste {} sur {}'.format(df[i], i, df.shape))
    dic_final[str(df[i])] = liste
    liste[:] = []

print(dic_final)

a_file = open("data.pkl", "wb")
pickle.dump(dic_final, a_file)
a_file.close()

# df_b_cleared = df_bilboard.fillna("")

# print(df_b_cleared.head())

# for i in range(len(df_b_cleared['artist'])):
#     df_b_cleared['artist'][i] = re.sub(r"Featuring ", "",df_b_cleared['artist'][i])
#     df_b_cleared['artist'][i] = re.sub(r"(\w*[!@#$%^&*]+\w*)", "",df_b_cleared['artist'][i])
#     df_b_cleared['title'][i] = re.sub(r"(\w*[!@#$%^&*]+\w*)", "",df_b_cleared['title'][i])

# print(df_b_cleared['title'][4857]) 



# df_b_cleared.to_csv('test.csv',index=False)