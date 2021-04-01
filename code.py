#%%
import pandas as pd 
l=[i for i in range(1,1154)]
data = pd.read_csv("La myriade de Totems de Montpellier.csv", sep=",", skiprows=l)
data # On prend en compte les données seulement de 2021
#%% 
data_velos = pd.read_excel("Classeur1.xlsx")
#On utilise un tableau qui contient les observations aux alentours de 9h les jours de la semaine
print(data_velos)
# %%
import numpy as np 
np.mean(data_velos['Nbr vélos']) # On prend la moyenne du nombre de vélos par jour entre 00h00 et 09h00
#Cette moyenne est 313,36, je fais la prédiction qu'il y aura donc 313 vélos le 02 avril 2021
#au compteur d'Albert 1er entre 00h00 et 09h00
# %%
