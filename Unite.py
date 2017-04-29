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
                 capacite = 0, portee = 0,
                 vitesse_projectile = 0,
                 delai_attaque = 0): #le parent est l'instance qui crée l'unite
        self.id=Id.prochainid()
        self.proprietaire = proprietaire
        self.action = None
        self.cible = None
        
        #caracteristiques de la position et du deplacement
        self.lieu = parent.lieu
        self.base = parent
        self.base2 = None #Les bases sont les instances entre lesquelles l'unite fait des alles-retours.
        self.x, self.y = self.initier_position(parent)
        self.angletrajet = 0
        self.angleinverse = 0
        self.vitesse = vitesse
        self.chemin = None
        self.indice_chemin = 0
        
        #caracteristiques de l'unite
        self.taille = taille
        self.energie = energie
        
        #caracteristiques de l'attaque
        self.attaque = attaque
        self.portee = portee
        self.delai_attaque = delai_attaque
        self.vitesse_projectile = vitesse_projectile
        self.indice_delai_attaque = 0
        
        #Cargaison
        self.nbbois=1
        self.nbfoin=1
        self.nbargent=1
        self.nbminerai=1
        
    
    #Methodes de deplacement
    def avancer(self):
        rep = None
        if self.cible and self.lieu == self.cible.lieu:
            if self.lieu is None: #Galaxie
                self.ciblerdestination()
                x=self.cible.x
                y=self.cible.y
                if hlp.calcDistance(self.x,self.y,x,y) >= self.vitesse:
                    self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
                else:
                    rep=self.cible
                    self.base=self.cible
                    return True #La cible est atteinte
            elif isinstance(self.lieu, Systeme.Systeme):
                self.ciblerdestination()
                x=self.cible.x
                y=self.cible.y
                if hlp.calcDistance(self.x, self.y, x, y) >= self.vitesse:
                    self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
                else:
                    rep = self.cible
                    self.base = self.cible
                    return True #La cible est atteinte
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
        
    def ciblerdestination(self):
        self.angletrajet=hlp.calcAngle(self.x, self.y, self.cible.x, self.cible.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x, self.y, self.cible.x, self.cible.y)

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
    
    def rotation(self):
        angleRotation = math.radians(2)
        self.x,self.y=hlp.calcRotation(self.base.x, self.base.y, self.x, self.y, angleRotation) 
    
    def collecter_decharger(self):
        if self.cible == self.base:
            self.collecter()
        else:
            self.decharger()
            
    def collecter(self):
        self.cible = self.base
    
    def decharger(self):
        self.cible = self.base2
    
    def initier_position(self, parent):
        if self.lieu is None:
            return parent.x+20/100, parent.y
        elif isinstance(self.lieu, Systeme.Systeme):
            return parent.x+(parent.taille)*100+15, parent.y
        
        
     
    #Methodes d'attaque
    def attaquer(self):
        if self.indice_delai_attaque <= 0:
            if self.cible.energie > 0:
                projectile = Projectile(self.parent, self.cible, self.attaque, self.vitesse_projectile, self.portee_projectile)
                self.proprietaire.parent.objets_cliquables[projectile.id] = projectile
            else:
                self.cible = None
                self.indice_delai_attaque = self.vitesse_attaque

class UniteCargo(Unite):
    def __init__(self):
        pass
    
class UniteAttaque(Unite):
    def __init__(self):
        pass
    
class Station(Unite):
    pass

class Projectile(Unite):
    def __init__(self, parent,
                 attaque, vitesse, portee
                 ):
        super().__init__()
        self.init_x = base.x #position de depart
        self.init_y = base.y #position de depart
        self.x = base.x
        self.y = base.y
        self.portee_carree = portee**2

    def avancer(self): 
        diff_x_caree = (self.init_x-self.x)**2
        diff_y_caree = (self.init_y-self.y)**2
        if (diff_x_caree+diff_y_caree <= self.portee_carree):
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
            return True
        return False # Le projectile a atteint sa distance maximale
    
    
class Sonde(Unite):
    def __init__(self, proprietaire, systeme):
        super().__init__(proprietaire, systeme,
                         energie = 100,
                         vitesse = 0.02*5,
                         taille = 16
                         )

class VaisseauAttaqueGalactique(Unite):
    def __init__(self, proprietaire, systeme):
        super().__init__(proprietaire, systeme,
                         energie = 100,
                         vitesse = 0.02*5,
                         attaque = 15,
                         delai_attaque = 10,
                         portee = 15,
                         vitesse_projectile = 6,
                         taille = 16
                         )
    def avancer(self):
        if super().avancer():
            if self.proprietaire is not self.cible.proprietaire:
                self.attaquer()

class VaisseauAttaqueSolaire(Unite):
    def __init__(self, proprietaire, planete):
        super().__init__(proprietaire, planete,
                         energie = 100,
                         vitesse = 5,
                         attaque = 15,
                         delai_attaque = 10,
                         portee = 15,
                         vitesse_projectile = 6,
                         taille = 16
                         )    
    
class VaisseauCargoSolaire(Unite):
    def __init__(self, proprietaire, planete):
        super().__init__(proprietaire, planete,
                         energie = 100,
                         vitesse = 5,
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
                         vitesse = 5,
                         taille = 20, 
                         portee = 15
                         )
        
        self.action = self.rotation
        
    def avancer():
        pass #La station planetaire ne se deplace pas, je crois. #io 28-04
    
    def avancer(self):
        if super().avancer():
            self.rotation()
        
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
                         attaque = 10,
                         delai_attaque = 10,
                         vitesse_projectile = 6,
                         taille = 20,
                         portee = 15,
                         capacite = 10
                         )
        
        self.action = self.rotation
    
    def avancer(self):
        if super().avancer():
            self.rotation()
            
    def reparation(self):
        pass
    def troc(self):
        pass
    def deplacer(self):
        pass
    
class Disciple(Unite):
    def __init__(self):
        Unite.__init__(proprietaire, parent)
        self.experience=None
        
