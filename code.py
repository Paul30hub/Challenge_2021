#%%
import pandas as pd 
l=[i for i in range(1,1154)]
data = pd.read_csv("La myriade de Totems de Montpellier.csv", sep=",", skiprows=l)
data # On prend en compte les données seulement de 2021
#%% 
data_velos = pd.read_excel("Classeur1.xlsx")
#On utilise un tablau qui contient les observations aux alentours de 9h les jours de la semaine
print(data_velos)
#%%
import datetime as dt 
d1 = dt.time(12, 56, 42)
# %%
import numpy as np 
np.mean(data_velos['Nbr vélos'])
# %%
