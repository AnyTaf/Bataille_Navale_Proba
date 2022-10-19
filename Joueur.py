import pdb
import numpy as np
from Bataille import *
from Grille import *

class Joueur():
    def __init__ (self):
            self.coups = 0
            self.grille = Grille()
    
    def reset(self):
        self.coups = 0
        self.grille = Grille()
    
    def joue_aleatoire(self, bataille):
        positions=[] #liste contenant les positions des cases qui ont étaient déja touchées
        while (not bataille.victoire()) :
            position =np.random.randint(10) , np.random.randint(10) #tirer une position aleatoire
            while (positions.count(position) > 0) : #verifier si la position a deja été tirée
                position =np.random.randint(10) , np.random.randint(10)
            res , p =bataille.joue(position)
            self.coups+=1
            positions.append(position)
        return self.coups

    def joue_heuristique(self,bataille):
        case_conexes = [] #cette liste contient les positions des cases adjacentes d'une case touchée
        positions =[]   #cette liste contient les positions des cases déja touchées
        while not bataille.victoire():
            if(len(case_conexes)==0): 
                position =np.random.randint(10) , np.random.randint(10) 
                while (positions.count(position) > 0) : 
                    position =np.random.randint(10) , np.random.randint(10)
            else:
                position = case_conexes.pop()
            res = bataille.joue(position)
            self.coups+=1
            positions.append(position)
            if res[0] == 3:
                x , y = position
                if x+1>=0 and x+1<10 : 
                    pos = x+1, y
                    if(positions.count(pos) == 0):
                       case_conexes.append(pos)
                if x-1>=0 and x-1<10 : 
                    pos = x-1, y
                    if(positions.count(pos) == 0):
                        case_conexes.append(pos)
                if y+1>=0 and y+1<10 : 
                    pos = x, y+1
                    if(positions.count(pos) == 0):
                        case_conexes.append(pos)
                if y-1>=0 and y-1<10 : 
                    pos = x, y-1
                    if(positions.count(pos) == 0):
                        case_conexes.append(pos)
        return self.coups

    def joue_simplifie(self, bataille):

        positions=[] #liste contenant les positions des cases deja parcourues
        while (not bataille.victoire()) :#while on a pas encore victoire
            position =np.random.randint(10) , np.random.randint(10) #tirer une position aleatoire
            while (positions.count(position) > 0) : #verifier si la position a deja été tirée
                position =np.random.randint(10) , np.random.randint(10) #tirer une autre position aleatoire
            x,y=position
            matrice_proba = self.proba_grille(bataille)
            for i in range(bataille.grille.N):
                   for j in range(bataille.grille.N):
                       if positions.count((i,j)) == 0 and matrice_proba[x][y]< matrice_proba[i][j]:
                           x  , y = i , j
            position = x , y
            positions.append(position)
            res , pos = bataille.joue(position)
            if res == 1 :
                self.grille.matrice[x][y][0] = 1
            elif res == 2 :
                for p in pos :
                   self.grille.matrice[p[0]][p[1]][0] = 1 
            self.coups+=1
        return self.coups

    def proba_grille(self,bataille):
        """
            Cette fonction return une matrice qui contient dans chaque case le nombre de possibilitée
            de la présence d'un des bateaux restant dans une case de la grille qui a les meme coordonées
        """
        matrice = np.zeros((self.grille.N,self.grille.N)).astype(int)
        for b in  bataille.bateaux_non_coule :
           for i in range(bataille.grille.N):
               for j in range(bataille.grille.N):
                    position = i , j
                    if self.grille.peut_placer(b[0], position, 1) :
                        for k in range(b[1]):
                            matrice[i][j+k] +=1
                    elif self.grille.peut_placer(b[0], position, 2) :
                        for k in range(b[1]):
                            matrice[i+k][j] +=1
                            
        return matrice 

"""les graphiques de distribution de la version aleatoire du jeux"""


#les graphiques de distribution de la version aleatoire du jeux
distribution_aleatoire=[]
"""
on cree une liste vide on la remplie a chaque fois qu'on joue pour former la distibution
on calcule la distribution pour 1000 fois joué
"""
for i in range(1,1001):
    joueur1 = Joueur()
    bataille1=Bataille()
    nb_coup=joueur1.joue_aleatoire(bataille1)
    distribution_aleatoire.append(nb_coup)
plt.hist(distribution_aleatoire)
plt.xlabel('nombre de coup')
plt.ylabel("nombre d'occurence de jouer aleatoirement")
plt.show()





#les graphiques de distribution de la version heuristique du jeux
distribution_heuristique=[]
""" 
on cree une liste vide on la remplie a chaque fois qu'on joue pour former la distibution
on calcule la distribution pour 1000 fois joué
"""
for i in range(1,1001):
    joueur1 = Joueur()
    bataille1=Bataille()
    nb_coup=joueur1.joue_heuristique(bataille1)
    distribution_heuristique.append(nb_coup)
plt.hist(distribution_heuristique)
plt.xlabel('nombre de coup')
plt.ylabel("nombre d'occurence de jouer à la version heuristique")
plt.show()


#les graphiques de distribution de la version simplifiée du jeux
distribution_simplifie=[]
"""
on cree une liste vide on la remplie a chaque fois qu'on joue pour former la distibution
on calcule la distribution pour 1000 fois joué
"""
for i in range(1,1001):
    joueur1 = Joueur()
    bataille1=Bataille()
    nb_coup=joueur1.joue_simplifie(bataille1)
    distribution_simplifie.append(nb_coup)
plt.hist(distribution_simplifie)
plt.xlabel('nombre de coup')
plt.ylabel("nombre d'occurence de jouer à la version simplifiée")
plt.show()


print ("nombre de coups avec les differentes versions ")
b = Bataille()
j = Joueur()
print("nb coup version aleatoire",j.joue_aleatoire(b))

b.reset()
j.reset()
print("nb coup version heuristique",j.joue_heuristique(b))

b.reset()
j.reset()

print("nb coup version simplifié",j.joue_simplifie(b))

