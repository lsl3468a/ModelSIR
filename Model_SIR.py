# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:45:57 2021

@author: Ludivine Lsr
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import datetime

#fonction qui calcule la dérivé de S,I,R en fonction du temps
def derive_dt(U,t):
    dS = -alpha*U[0]*U[1]
    dI = alpha*U[0]*U[1] - mu*U[1]
    dR = mu*U[1]
    return[dS,dI,dR]

# Nombre de personnes saines dans la population à t=0
S0 = input("Entrez le nombre de personnes saines dans la population à t=0 \n")

# Nombre de personnes infectées dans la population à t=0
I0 = input("Entrez le nombre de personnes infectées dans la population à t=0 \n")

# Nombre de personnes rétablies dans la population à t=0
R0 = 0
U0=[S0,I0,R0]

#alpha représente la probabilité d'infection
alpha = float(input("Entrez la probabilité d'infection : \n"))

#mu représente la probabilité de guérison 
mu = float(input("Entrez la probabilité de guérison : \n"))

#Vecteur du temps
ts=np.arange(0,100,0.01)

#Appel à la fonction derive_dt qui va calculer les résultats
Us = odeint(derive_dt,U0,ts)
S = Us[:,0]
I = Us[:,1]
R = Us[:,2]

#Création du diagramme
plt.rcParams["figure.figsize"] = (12,10)
plt.title("Modélisation d'un modèle SIR")
plt.plot(ts,S,linewidth=2.5,label="Sains")
plt.plot(ts,I,linewidth=2.5,label="Infectés")
plt.plot(ts,R,linewidth=2.5,label="Rétablis")
plt.legend()
plt.show()

#On crée le nom du fichier et on sauvegarde notre courbe dans une image .png
nom = "SIR"+str(datetime.datetime.now())+".png"
plt.savefig(nom)
plt.close()