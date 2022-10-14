#%%
from re import S
from tkinter import N
from unittest.util import _PLACEHOLDER_LEN
import numpy as np
import  matplotlib.pyplot as plt

bateaux = [(1,5),(2,4),(3,3),(4,3),(5,2)]
"""
    bateaux représente la liste des couples (identifiant d'un bateau b ,nombre de cases du bateau b)
    Les bateaux sont codés par des identifiant
    1 pour le porte-avions qui est sur 5 cases 
    2 pour le croiseur qui sur 4 cases
    3 pour le contre-torpilleurs qui est sur 4 cases
    4 pour le sous-marin qui est sur 3 cases
    5 pour le torpilleur qui est sur 2 cases
"""



class Grille():

    def __init__ (self , N=10):
        """
            Création d'une grille vide
        """
        self.N= N 
        self.matrice = np.zeros((N,N,4)).astype(int)
            
    """
        Dans ce code : 
            1) une case de la grille contient :
                0 si elle est vide
                -1 si elle a était touché
                sinon un entier qui représente l'identifiant du bateau qui l'occupe
            2) la direction est codée par un entier :
                1 pour horizentale
                2 pour verticale
    """
    def peut_placer(self, bateau, position, direction):
            x , y = position  
            if bateau < 1 or bateau > 5 :
                print("Mauvaise entrée pour le bateau")
                return False
            if (x not in range(10)) or (y not in range(10)):
                print("Mauvaise entrée pour la position")
                return False
            if direction not in [1,2]:
                print("Mauvaise entrée pour la direction")
                return False
            nb_case = bateaux[bateau-1][1]
            for i in range (nb_case) :
                if direction==1 : 
                    if y+i>=10 or self.matrice[x][y+i][0] != 0 :
                        return False
                else:
                    if x+i>=10 or self.matrice[x+i][y][0] != 0 :
                        return False
            return True 

    def place(self, bateau, position, direction) : 
        if (self.peut_placer( bateau, position, direction) ):
            x , y = position 
            nb_case = bateaux[bateau-1][1]
            for i in range (nb_case) :
                if direction==1 : 
                    self.matrice[x][y+i][0] = bateau
                    self.matrice[x][y+i][3] = i
                    self.matrice[x][y+i][2] = direction

                else:
                    self.matrice[x+i][y][0] = bateau
                    self.matrice[x+i][y][3] = i
                    self.matrice[x+i][y][2] = direction
            return True 
        else : 
            return False

    def place_alea(self, bateau) :
        position=np.random.randint(10) , np.random.randint(10)
        direction=np.random.randint(1,3)
        while not self.place( bateau, position, direction) :
            position=np.random.randint(10) , np.random.randint(10)
            direction=np.random.randint(1,3)

    def affiche(self) : 
        plt.imshow(self.matrice, cmap = 'Greens')

    @staticmethod
    def eq (grilleA, grilleB) :
        return np.array_equal(grilleA.matrice ,grilleB.matrice)

    @staticmethod
    def genere_grille() :
        grille = Grille()
        for i in range (1,6) :
           grille.place_alea(i)
        return grille

    def nb_places(self, bateaux ):
        if len(bateaux)==0 :
            return 1
        else :
            nb_config = 0
            nb_case = bateaux[bateaux[0]-1][1]
            for i in range(self.N):
                for j in range(self.N):
                    for k in range(1,3):
                        pos = i , j
                        sauv_grille = np.array(self.matrice)
                        if (self.place(bateaux[0],pos,k)) :
                            nb_config += self.nb_places(bateaux[1:])
                        self.matrice = np.array(sauv_grille)
                        
            return nb_config



# %%
