import numpy as np
import random

def genere_grille1():
    res=np.zeros((10,10))
    #zone2
    for x in range(10):
        for y in range(10):
            res[x][y]=1/200
    #zone3
    for x in range(4,6):
        for y in range(4,6):
            res[x][y]=1/40
    #zone1
    for i in range(10):
        res[0][i]=1/60
        res[i][0]=1/60
        res[9][i]=1/60
        res[i][9]=1/60
    return res
    
def genere_grille2():
    res=np.zeros((10,10))
    #zone2
    for x in range(10):
        for y in range(10):
            res[x][y]=1/410
    #zone1
    for x in range(1,9):
        if x>6 :
            for y in range(1,7):
                res[x][y] = 2/45
        else :
             res[x][1] = 2/45
    return res

def max_proba(grille):
#trouver la probabilité maximale
    n=-1
    i_max=0
    j_max=0
    for x in range(10):
        for y in range(10):
            if(grille[x][y]>n):
                n=grille[x][y]
                x_max=x
                y_max=y
    return [x_max,y_max]

def trouve(case,case_objet,ps):
    #cette fonction dit si le senseur a détecté qqch
    #s'il n'ya pas l'objet, le senseur ne detecte rien
    if(case!=case_objet):
        return False
    #sinon il detecte avec une proba ps 
    if(random.random()<ps):
        return True
    return False
    
#ps est la probabilité de détéction du senseur
def trouve_objet_perdu(ps,grille):
    #l'objet a été perdu à la case [5,5]
    case_objet=[5,5]
    case=max_proba(grille)
    nb_essais=1
    while(not trouve(case,case_objet,ps)):
        pco=grille[case[0]][case[1]]
        for x in range(10):
            for y in range(10):
                pc=grille[x][y]
                #mise à jour de la proba des case
                if([x,y]!=case):
                    grille[x][y]=pc/(1-ps*pco)
                if([x,y]==case):
                    grille[x][y]=((1-ps)*pco)/(1-ps*pco)
        case=max_proba(grille)
        nb_essais+=1
    return nb_essais
    
### main
print(trouve_objet_perdu(0.9,genere_grille1()))
print(trouve_objet_perdu(0.9,genere_grille2()))
