from Id import *
from Infrastructure import *
import random
import math

DEMIELARGEUR_TUILES = 32 #à suppr #io 11-04
DEMIEHAUTEUR_TUILES = 16 #à suppr #io 11-04

class Pulsar():
    def __init__(self,x,y):
        self.id=Id.prochainid()
        self.lieu = None
        self.proprietaire="inconnu"
        self.x=x
        self.y=y
        self.periode=random.randrange(20,50,5)
        self.moment=0
        self.phase=1 
        self.mintaille=self.taille=random.randrange(2,4)
        self.maxtaille=self.mintaille++random.randrange(1,3)
        self.pas=self.maxtaille/self.periode
        self.taille=self.mintaille
        self.action = self.evoluer
        
    def evoluer(self):
        self.moment=self.moment+self.phase
        if self.moment==0:
            self.taille=self.mintaille
            self.phase=1
        elif self.moment==self.periode:
            self.taille=self.mintaille+self.maxtaille
            self.phase=-1
        else:
            self.taille=self.mintaille+(self.moment*self.pas)
                
class Planete():
    def __init__(self, parent, type, dist, taille, angle, x, y):
        self.id=Id.prochainid()
        self.parent = parent #questionner la pertinence #io 18-04
        self.lieu = parent
        self.posXatterrissage=x
        self.posYatterrissage=y 
        self.proprietaire="inconnu"
        self.visiteurs={}
        self.distance=dist
        self.type=type
        self.taille=taille
        self.angle=angle
        self.sol = None
        self.x=x
        self.y=y
        self.nbbois=random.randrange(1,1000)
        self.nbfoin=random.randrange(1,1000)
        self.nbargent=random.randrange(1,1000)
        self.nbminerai=random.randrange(1,1000)
        self.nbpopulation=100
        self.infrastructures = [] 
        
    def creationtourdefense(self):
        pass
    
    def initier_sol(self):
        self.sol = Sol(15, 15) #refaire plus propre #io 11-04
        return self.sol

class Sol():
    def __init__(self, matrice_largeur, matrice_hauteur):
        self.matrice_largeur = matrice_largeur
        self.matrice_hauteur = matrice_hauteur
        self.terrain = self.generer_terrain()
        self.demielargeur_tuiles = DEMIELARGEUR_TUILES
        self.demiehauteur_tuiles = DEMIEHAUTEUR_TUILES
        self.demielargeur_sol = self.demielargeur_tuiles*self.matrice_largeur

    def generer_base(self):
        terrain = []
        for y in range(self.matrice_hauteur):
            terrain.append([])
            for x in range(self.matrice_largeur):
                terrain[y].append("terre")
        return terrain

    def generer_collines(self, terrain):
        cases_colline = list()
        x = random.randrange(0, self.matrice_largeur-1)
        y = random.randrange(0, self.matrice_hauteur-1)
        x2 = random.randrange(0, self.matrice_largeur-1)
        y2 = random.randrange(0, self.matrice_hauteur-1)
        cases_colline.append([x, y])
        terrain[y][x] = "colline"

        sens_x = -1 if x > x2 else 1
        sens_y = -1 if y > y2 else 1

        while x != x2 and y != y2:
            axe = random.choice(['x', 'y'])
            if axe == 'x':
                 x += sens_x
            else:
                y += sens_y
            x %= self.matrice_largeur
            y %= self.matrice_hauteur
            terrain[y][x] = "colline"
            cases_colline.append([x, y])

        for i in range(50):
            case_alea = random.choice(cases_colline)
            j = random.randrange(0, 2)
            case_nouv = case_alea[:]
            case_nouv[j] = case_alea[j] + random.choice([-1, 1])
            x, y = case_nouv
            x %= self.matrice_largeur
            y %= self.matrice_hauteur
            if terrain[y][x] == "terre":
                terrain[y][x] = "colline"
                cases_colline.append(case_nouv)
            
        for x, y in cases_colline:
            x %= self.matrice_largeur
            y %= self.matrice_hauteur
            terrain[y][x-1] = "colline"
            terrain[y-1][x-1] = "colline"
            terrain[y-1][x] = "colline"

    def generer_eau(self, terrain):
        cases_eau = []
        while True:
            x = random.randrange(0, self.matrice_largeur-1)
            y = random.randrange(0, self.matrice_hauteur-1)
            if terrain[y][x] == "terre":
                break

        sens_x = -1 if x > self.matrice_largeur/2 else 1
        sens_y = -1 if y > self.matrice_hauteur/2 else 1

        while self.matrice_largeur > x >=0 and self.matrice_hauteur > y >= 0:
            if terrain[y][x] == "terre":
                terrain[y][x] = "eau"
                cases_eau.append([x, y])
            axe = random.choice(['x', 'y'])
            if axe == 'x':
                x += sens_x
            else:
                y += sens_y
        
        for i in range(200):
            case_alea = random.choice(cases_eau)
            j = random.randrange(0, 2)
            case_nouv = case_alea[:]
            case_nouv[j] = case_alea[j] + random.choice([-1, 1])
            x, y = case_nouv
            x %= self.matrice_largeur
            y %= self.matrice_hauteur
            if terrain[y][x] == "terre":
                terrain[y][x] = "eau"
                cases_eau.append(case_nouv)

    def generer_terrain(self):
        terrain = self.generer_base()
        self.generer_collines(terrain)
        self.generer_eau(terrain)
        return terrain

    def iso_vers_matrice(self, coords):
        vue_x = coords.x
        vue_y = coords.y
        x = math.floor(((vue_x - 512)/self.demielargeur_tuiles +
                        (vue_y)/self.demiehauteur_tuiles)/2)
        y = math.floor(((vue_y)/self.demiehauteur_tuiles -
                        (vue_x - 512)/self.demielargeur_tuiles)/2)
        return (x, y)
    
    def matrice_vers_iso(self, matrice_x, matrice_y):
        vue_x = self.demielargeur_tuiles*(matrice_x-matrice_y) + self.demielargeur_sol
        vue_y = self.demiehauteur_tuiles*(matrice_x+matrice_y)
        return (vue_x, vue_y)
        
    
class Etoile():
    def __init__(self,parent,x,y):
        self.id=Id.prochainid()
        self.parent = parent #questionner la pertinence #io 04=08
        self.lieu = parent
        self.type=random.choice(["rouge","rouge","rouge",
                                 "jaune","jaune",
                                 "bleu"])
        self.taille=random.randrange(25)/10 +0.1   # en masse solaire
