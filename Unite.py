from Id import *
import random
from helper import Helper as hlp
import math

import Systeme
import Planete

class Unite:
    def __init__(self, proprietaire, parent,
                 energie = 0, vitesse = 0 ,
                 attaque = 0, taille = 0,
                 capacite = 0): #le parent est l'instance qui cr�e l'unite
        self.id=Id.prochainid()
        self.proprietaire = proprietaire
        
        self.action = None
        self.lieu = parent.lieu
        self.x, self.y = self.initier_position(parent)
        self.angletrajet = 0
        self.angleinverse = 0
        self.vitesse = vitesse
        self.chemin = None
        self.indice_chemin = 0
        self.cible = None
        
        self.energie = energie
        self.attaque = attaque
        self.taille = taille
        
    def avancer(self):
        rep=None
        if self.cible and self.lieu == self.cible.lieu:
            if self.lieu is None: #Galaxie
                x=self.cible.x
                y=self.cible.y
                self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
                if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                    rep=self.cible
                    self.base=self.cible
                    self.cible=None
                return rep
            elif isinstance(self.lieu, Systeme.Systeme):
                x=self.cible.x
                y=self.cible.y
                self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
                if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                    rep=self.cible
                    self.base=self.cible
                    self.cible=None
                return rep
            elif self.chemin and isinstance(self.lieu, Planete.Planete):
                x_cible, y_cible = self.lieu.matrice_vers_iso(*self.chemin[self.indice_chemin])
                diff_x = x_cible - self.x
                diff_y = y_cible - self.y
                print(diff_x, diff_y)
                if abs(diff_x) >5 or abs(diff_y) >5:
                    hypot = math.hypot(diff_x, diff_y)
                    self.x += diff_x/hypot
                    self.y += diff_y/hypot
                elif self.indice_chemin<len(self.chemin)-1:
                    self.indice_chemin += 1
        
    def ciblerdestination(self,p):
        self.cible=p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)

    def assigner_cible(self, cible):
            self.cible = Coord(cible.x, cible.y)
            self.chemin = self.calculer_chemin(cible)
            print(self.chemin)
            self.indice_chemin = 1
            
    def calculer_chemin(self, coords_cible):
        def chemin_reconstruit(infos_cases, cible):
            case_courante = cible
            
            chemin = []
            while case_courante != None:
                chemin.append(case_courante)
                case_courante = infos_cases[case_courante].voisin
            chemin.reverse()
            return chemin

        x_init, y_init = self.lieu.iso_vers_matrice(self)
        x_cible, y_cible = self.lieu.iso_vers_matrice(coords_cible)
        InfosCase = collections.namedtuple("InfosCase",
                                             "distance voisin")
        cases_visitees = set()
        cases_nontestees = set()
        cases_nontestees.add((x_init, y_init))
        infos_cases = dict()
        infos_cases[(x_init, y_init)] = InfosCase(0, None)
        cible = (x_cible, y_cible)
        while len(cases_nontestees) != 0: 
            cases_par_distance = sorted([(infos_cases[case].distance, case)
                                         for case in cases_nontestees])
            case_courante = cases_par_distance[0][1]
            cases_nontestees.remove(case_courante)
            cases_visitees.add(case_courante)
            if case_courante == cible :
                print(test)
                return chemin_reconstruit(infos_cases, cible)
            x, y = case_courante
            for a in range(-1, 2):
                for b in range(-1, 2):
                    i = (x+a)%self.lieu.matrice_largeur
                    j = (y+b)%self.lieu.matrice_hauteur
                    voisin = (i, j)
                    if (voisin in cases_visitees):
                        continue
                    if (self.lieu.terrain[j][i] != "terre"):
                        test.add((i, j))
                        continue

                    distance = infos_cases[case_courante].distance+1*abs(a)+0.5*abs(b)
                    if voisin not in cases_nontestees:
                        cases_nontestees.add(voisin)
                    elif distance >= infos_cases[voisin].distance:
                        continue
                    infos_cases[voisin] = InfosCase(distance, case_courante)
        return None
    
    def initier_position(self, parent):
        if self.lieu is None:
            return parent.x+20/100, parent.y
        elif isinstance(self.lieu, Systeme.Systeme):
            return parent.x+20/100, parent.y

    
    def attaquer(self):
        pass
    
class Sonde(Unite):
    def __init__(self, proprietaire, systeme):
        super().__init__(proprietaire, systeme,
                         energie = 100,
                         vitesse = 0.02*5,
                         attaque = 0,
                         taille = 16
                         )

class VaisseauAttaqueGalactique(Unite):
    def __init__(self, proprietaire, systeme):
        super().__init__(proprietaire, systeme,
                         energie = 100,
                         vitesse = 0.02*5,
                         attaque = 0,
                         taille = 16
                         )

class VaisseauAttaqueSolaire(Unite):
    def __init__(self, proprietaire, planete):
        super().__init__(proprietaire, planete,
                         energie = 100,
                         vitesse = 0.02*5,
                         attaque = 0,
                         taille = 16
                         )    
    
class VaisseauCargoSolaire(Unite):
    def __init__(self, proprietaire, planete):
        super().__init__(proprietaire, planete,
                         energie = 100,
                         vitesse = 0.02*5,
                         attaque = 0,
                         taille = 16
                         )
        
    def charger(self):
        pass
    def decharger(self):
        pass
    def chargerressources():
        pass
    
class VaisseauCargoGalactique(Unite):
    def __init__(self, proprietaire ,systeme):
        super().__init__(proprietaire, systeme,
                         energie = 100,
                         vitesse = 0.02*5,
                         attaque = 0,
                         taille = 16
                         )    
    
    def charger(self):
        pass
    def decharger(self):
        pass
    def chargerressources():
        pass
    
class StationPlanetaire(Unite):
    def __init__(self, proprietaire, planete):
        super().__init__(proprietaire, planete,
                         energie = 100,
                         vitesse = None,
                         attaque = 0,
                         taille = 20 
                         )
        self.base = planete
        self.x=planete.x+10 
        self.y=planete.y-10
        
        self.action = self.rotation
        
    def avancer(self):
        pass

    def rotation(self):
        angleRotation = math.radians(2)
        self.x,self.y=hlp.calcRotation(self.base.x-25, self.base.y-25, self.x, self.y, angleRotation)  
        
    def creercargogalactique(self):
        pass
    def creerattaquegalactique(self):
        pass
    def creerbouclierplanetaire(self):
        pass
    
    
class StationGalactique(Unite):
    def __init__(self, proprietaire, systeme):
        super().__init__(proprietaire, systeme,
                         energie = 100,
                         vitesse = 0.02*5,
                         attaque = 0,
                         taille = 20,
                         capacite = 10
                         )
        self.base = systeme
        self.action = self.rotation
    
    def rotation(self):
        pass
    def reparation(self):
        pass
    def troc(self):
        pass
    def deplacer(self):
        pass
    
class Disciple(Unite):
    def __init__(self):
        Unite.__init__(proprietaire, parent)
        self.experience=None  # C'est ici qu'on met les attributs propres à chaque unité