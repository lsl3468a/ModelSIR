import random
import matplotlib.pyplot as plt
import numpy as np

NB_ITER = 1000
TAILLE_MONDE = 100
NBAG =  1000
PROB_INF = 0.003
DIST_INF = 10
DEPLACEMENT = 8
PROB_REC = 0.012
PROB_MORT = 0.001

def effectifs(L):
    return (len(list(filter(lambda x:x['s']==0,L))),
    len(list(filter(lambda x:x['s']==1,L))),
    len(list(filter(lambda x:x['s']==2,L))),
    len(list(filter(lambda x:x['s']==3,L))))

def init(L):
    for i in range(NBAG):
        L.append({'id':i,'x':random.randint(0,TAILLE_MONDE),'y':random.randint(0,TAILLE_MONDE),'s':0})

def deplacement(L):
    for a in L:
        a['x'] += (DEPLACEMENT//2 - random.randrange(DEPLACEMENT))
        a['y'] += (DEPLACEMENT//2 - random.randrange(DEPLACEMENT))
        a['x'] %= TAILLE_MONDE
        a['y'] %= TAILLE_MONDE
    
def recuperation(L):
    for a in filter(lambda x:x['s']==1,L):
        if (random.random()<PROB_REC):
            a['s']=2
def mort(L):
    for a in filter(lambda x:x['s']==1,L):
        if(random.random()<PROB_MORT):
            a['s']=3

def infection(L):
    for a in filter(lambda x:x['s']==0,L):
        L2 = filter(lambda agent: agent['s']==1 and (abs(agent['x']-a['x']) + abs(agent['y']-a['y'])) < DIST_INF,L)
        #print(a,list(L2))
        for b in L2:
            if (random.random()<PROB_INF):
                LP[a['id']]['s'] = 1
                break

def resultat(L):
    print("Population de départ : ",NBAG,"\n")
    print("Après ",NB_ITER," itérations :\n")
    print("Nombre de sains : ",len(list(filter(lambda x:x['s']==0,L))),"\n");
    print("Nombre d'infectés : ",len(list(filter(lambda x:x['s']==1,L))),"\n");
    print("Nombre de rétablis : ",len(list(filter(lambda x:x['s']==2,L))),"\n")
    print("Nombre de morts : ",len(list(filter(lambda x:x['s']==3,L))),"\n");
    
L = []
T = np.array(0)
NB_S = np.array(NBAG)
NB_I = np.array(0)
NB_R = np.array(0)
NB_M = np.array(0)


init(L)
L[random.randrange(NBAG)]['s'] = 1
#Création du diagramme
plt.rcParams["figure.figsize"] = (12,10)
plt.title("Modélisation d'un modèle SIR")

for t in range(NB_ITER):
    deplacement(L)
    recuperation(L)
    LP = list(L)
    infection(L)
    L = list(LP)
    mort(L)
    L=list(LP)
    #print(t,effectifs(L))
    T = np.append(T,t)
    St = (len(list(filter(lambda x:x['s']==0,L))))
    NB_S = np.append(NB_S,St)
    It = (len(list(filter(lambda x:x['s']==1,L))))
    NB_I = np.append(NB_I,It)
    Rt = (len(list(filter(lambda x:x['s']==2,L))))
    NB_R = np.append(NB_R,Rt)
    Mt = (len(list(filter(lambda x:x['s']==3,L))))
    NB_M = np.append(NB_M,Mt)

plt.plot(T, NB_S,linewidth=2.5,label="Sains")
plt.plot(T,NB_I, linewidth=2.5,label="Infectés")
plt.plot(T,NB_R,linewidth=2.5,label="Rétablis")
plt.plot(T,NB_M,linewidth=2.5,label="Morts")
plt.legend()
plt.show()
resultat(L)