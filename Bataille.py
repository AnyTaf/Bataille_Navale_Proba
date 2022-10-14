#%%
import pdb
from Grille import *


class Bataille():
    def __init__ (self):
            self.grille = Grille.genere_grille()
            self.bateaux_non_coule=[(1,5),(2,4),(3,3),(4,3),(5,2)] #bateaux_non_coule représente la liste des bateaux qui n'ont pas étaient coulé

    
    def nb_case(self,bateau):
        """
            Cette fonction retourne le nombre de cases non touchées occupées par un bateau
        """
        cpt = 0
        for i in range(self.grille.N):
            for j in range(self.grille.N):
                if bateau == self.grille.matrice[i][j][0] and self.grille.matrice[i][j][1] == 0:
                    cpt +=1
        return cpt

    def joue(self, position):
        positions = []
        x , y = position
        if self.grille.matrice[x][y][0] == 0 :
            #print("La case est vide ", position)
            return 1, positions
        else : 
            bateau = self.grille.matrice[x][y][0]
            self.grille.matrice[x][y][1] = -1
            if self.nb_case(bateau) == 0 :
                #print("Coulé ", position)
                b = bateaux[bateau-1]
                print(position," ",b,"  ", self.bateaux_non_coule)
                self.bateaux_non_coule.remove(b)
                nb_case = bateaux[bateau-1][1]
                direction = self.grille.matrice[x][y][2]
                n =  self.grille.matrice[x][y][3]
                for i in range(nb_case):
                    if direction == 1 :
                        positions.append((x,y-n+i))
                    else :
                        positions.append((x-n+i,y))
                return 2,positions
            else:
                #print("touché ", position)
                return 3, positions

    
    def victoire (self) :
        return len(self.bateaux_non_coule) == 0



    def reset (self) :
        self.grille = Grille.genere_grille()
        self.bateaux_non_coule=[(1,5),(2,4),(3,3),(4,3),(5,2)]

    
    
    
    
    


#%%
