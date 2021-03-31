#%%
import pandas as pd 
l=[i for i in range(1,1154)]
data = pd.read_csv("La myriade de Totems de Montpellier.csv", sep=",", skiprows=l)
data # On prend en compte les données seulement de 2021
#%% 
data_velos = pd.read_excel("Classeur1.xlsx")
#On utilise un tablau qui contient le nombre de vélos pour une moyenne de 09:01:00 les jours de la semaine en 2021
print(data_velos)
#%%
import numpy as np 
np.mean(data_velos['Nbr vélos']) #On fait une moyenne du nombre de vélos obtenus ce qui nous donne le résultat de 252

