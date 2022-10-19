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
        self.matrice = np.zeros((N,N,3)).astype(int)
            
    """
        Dans ce code : 
            1) Chaque case d'une  grille est représentée par un 3-uplet:
                    le premier élèment contient :
                        0 si la case est vide
                        -1 si elle a était touché
                        sinon un entier qui représente l'identifiant du bateau qui l'occupe
                    le deuxiéme élèment conient :
                        0 si la case est vide
                        sinon la direction du bateau placé dans cette case (1 ou 2)
                    le troisième élèment contient :
                        0 si la case est vide
                        sinon l'entier i qui représente la iéme case du bateau placé dans cette case
            2) la direction est codée par un entier :
                1 pour horizentale
                2 pour verticale
    """
    def peut_placer(self, bateau, position, direction):
            """
                cette fonction return True si le bateau peut etre placé sur la grille dans position avec une certaine direction, False sinon
            """
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
        """
            cette fonction permet de placer un bateau sur la grille si on peut et retourne True, False sinon
        """
        if (self.peut_placer( bateau, position, direction) ):
            x , y = position 
            nb_case = bateaux[bateau-1][1]
            for i in range (nb_case) :
                if direction==1 : 
                    self.matrice[x][y+i][0] = bateau
                    self.matrice[x][y+i][1] = direction
                    self.matrice[x][y+i][2] = i

                else:
                    self.matrice[x+i][y][0] = bateau
                    self.matrice[x+i][y][1] = direction
                    self.matrice[x+i][y][2] = i
            return True 
        else : 
            return False

    def place_alea(self, bateau) :
        """
            cette fonction permet de placer un bateau aléatoirement sur la grille
        """
        position=np.random.randint(10) , np.random.randint(10)
        direction=np.random.randint(1,3)
        while not self.place( bateau, position, direction) :
            position=np.random.randint(10) , np.random.randint(10)
            direction=np.random.randint(1,3)

    def affiche(self) :
        """
            cette fonction permet d'afficher la grille
        """ 
        mat = [[self.matrice[i][j][0] for i in range(self.N)] for j in range(self.N)]
        mat = np.array(mat).astype(int)
        plt.imshow(mat, cmap = 'Greens')

    @staticmethod
    def eq (grilleA, grilleB) :
        """
            cette fonction return true su grilleA=grilleB, false sinon
        """
        return np.array_equal(grilleA.matrice ,grilleB.matrice)

    @staticmethod
    def genere_grille() :
        """
            cette fonction retourne une grille avec les bateaux placés aléatoirement 
        """
        grille = Grille()
        for i in range (1,6) :
           grille.place_alea(i)
        return grille
    
    def denombrement_bateau(self, bateau):
        """
            cette fonction return le nombre de dispositions possibles pour un bateau dans une grille
        """
        cpt=0
        for i in range(self.N):
            for j in range(self.N):
                for k in range(1,3):
                    if self.peut_placer(bateau,(i,j),k):
                        cpt+=1
        return cpt

    def nb_places(self, bateaux ):
        """
            cette fonction retourne le nombre de configurations possibles d'une grille 
        """
        if len(bateaux)==0 :
            return 1
        else :
            nb_config = 0
            for i in range(self.N):
                for j in range(self.N):
                    for k in range(1,3):
                        pos = i , j
                        sauv_grille = np.array(self.matrice)
                        if (self.place(bateaux[0],pos,k)) :
                            nb_config += self.nb_places(bateaux[1:])
                        self.matrice = np.array(sauv_grille)
                        
            return nb_config

    def eq_grille_donnee_grille_genere (self):
        Grilleg= Grille.genere_grille()
        nb_grilleg=1
        while (not(self.eq(self,Grilleg))) :
            nb_grilleg+=1
            Grilleg= Grille.genere_grille()

        return nb_grilleg 

 

    @staticmethod
    def genere_grille_de_bateau(bateaux) :
        np.random.seed(1)
        grille = Grille()
        for bateau in bateaux :
           grille.place_alea(bateau)
        return grille


    def approximer_nb_grille(self,bateaux) :
        nb_grille=1
        grille_compare = Grille.genere_grille_de_bateau(bateaux)
        while (not(self.eq(self,grille_compare))) :
            nb_grille+=1
            grille_compare = Grille.genere_grille_de_bateau(bateaux)
            print (nb_grille)
        return nb_grille


##MAIN
grilleA = Grille.genere_grille()
grilleA.affiche()

grilleB = Grille.genere_grille()
grilleB.affiche()

b = Grille.eq(grilleA,grilleB)
if b :
    print("grilleA = grilleB")
else :
    print("grilleA <> grilleB")

grilleC = Grille()
grilleD = Grille()
grilleE = Grille()
print("En testant la fonction qui calcul le nombre de configurations possibles sur des listes de 1, 2, 3 bateaux on aura les résultats suivant ")
print("1 Porte-Avion : ", grilleC.nb_places([1])," dispositions.")
print("1 Porte-Avion + 1 Croiseur : ", grilleD.nb_places([1,2])," dispositions.")
print("1 Porte-Avion + 1 Croiseur + 1 Contre-Torpilleur : ", grilleE.nb_places([1,2,3])," dispositions.")

#n = grilleA.eq_grille_donnee_grille_genere()
#print("Le nombre de grille générées pour trouver une grille égale à grilleA est : ",n)
# %%
