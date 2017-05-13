from Id import *
import random
from helper import Helper as hlp
import math

import Systeme
import Planete

echelle = 100

class Unite:
    def __init__(self, proprietaire, parent,
                 energie = 0, vitesse = 0 ,
                 attaque = 0, taille = 0,
                 capacite = 0, portee = 0,
                 portee_projectile = 0,
                 taille_projectile = 0,
                 vitesse_projectile = 0,
                 delai_attaque = 0, cout = 5
                 ): #le parent est l'instance qui crée l'unite
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
        self.cout = cout
        
        #caracteristiques de l'attaque
        self.attaque = attaque
        self.portee = portee
        self.taille_projectile = taille_projectile
        self.portee_projectile = portee_projectile
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
        if self.cible.proprietaire is None:
            distance_avec_cible = self.vitesse
        elif self.cible.proprietaire in (self.proprietaire, "inconnu"):
            distance_avec_cible = self.cible.taille+self.taille
        else:
            distance_avec_cible = self.vitesse+self.portee
            
        if self.cible and self.lieu == self.cible.lieu:
            if self.lieu is None: #Galaxie
                self.ciblerdestination()
                x=self.cible.x
                y=self.cible.y
                if hlp.calcDistance(self.x,self.y,x,y) >= distance_avec_cible: #self.vitesse+self.cible.taille+self.taille+portee:
                    self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
                else:
                    if isinstance(self.cible, Systeme.Systeme):
                        self.proprietaire.systemesvisites.add(self.cible)
                    self.base=self.cible
                    return True #La cible est atteinte
            elif isinstance(self.lieu, Systeme.Systeme):
                self.ciblerdestination()
                x=self.cible.x
                y=self.cible.y
                if hlp.calcDistance(self.x,self.y,x,y) >= distance_avec_cible: #self.vitesse+self.cible.taille+self.taille+portee:
                    self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
                else:
                    if isinstance(self.cible, Systeme.Systeme):
                        self.proprietaire.systemesvisites.add(self.cible)
                    self.base=self.cible
                    return True #La cible est atteinte
                """
                self.ciblerdestination()
                x=self.cible.x
                y=self.cible.y
                if hlp.calcDistance(self.x, self.y, x, y) >= self.vitesse:
                    self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
                else:
                    rep = self.cible
                    self.base = self.cible
                    return True #La cible est atteinte
                """
            elif self.chemin and isinstance(self.lieu, Planete.Planete):
                x_cible, y_cible = self.lieu.matrice_vers_iso(*self.chemin[self.indice_chemin])
                diff_x = x_cible - self.x
                diff_y = y_cible - self.y
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
            return parent.x+20/echelle, parent.y
        elif isinstance(self.lieu, Systeme.Systeme):
            return parent.x+(parent.taille)*echelle+15, parent.y
        
    def visiter(self):
        
        if self.avancer():
            print("trallalala")
            self.lieu = self.cible
            self.x = 2500#self.cible.etoile.x*echelle
            self.y = 2500 #self.cible.etoile.y*echelle
            print("cooords", self.x, self.y)
            
        
     
    #Methodes d'attaque
    def attaquer(self):
        self.indice_delai_attaque += 1
        if self.indice_delai_attaque >= self.delai_attaque:
            self.indice_delai_attaque = 0
            if self.cible.energie > 0:
                projectile = Projectile(self, self.cible, self.attaque,
                                        self.vitesse_projectile, self.portee_projectile,
                                        self.taille_projectile, self.proprietaire.parent.objets_cliquables)
                self.proprietaire.parent.projectiles.append(projectile)
            else:
                self.cible = None
                
            

class UniteCargo(Unite):
    def __init__(self):
        pass
    
class UniteAttaque(Unite):
    def __init__(self):
        pass
    
class Station(Unite):
    pass

class Projectile():
    def __init__(self, parent, cible,
                 attaque, vitesse, portee,
                 taille, objets_cliquables
                 ):
        
        self.lieu = parent.lieu
        self.init_x = parent.x #position de depart
        self.init_y = parent.y #position de depart
        self.taille = taille
        self.x, self.y = hlp.getAngledPoint(parent.angletrajet, parent.taille, parent.x, parent.y)
        self.portee_carree = portee**2
        self.angletrajet = hlp.calcAngle(parent.x, parent.y, cible.x, cible.y)
        self.angleinverse = math.radians(math.degrees(self.angletrajet)+180)
        
        self.action = self.avancer
        self.vitesse = vitesse
        self.attaque = attaque
        
        self.objets_cliquables = objets_cliquables
    
    def avancer(self):
        diff_x_caree = (self.init_x-self.x)**2
        diff_y_caree = (self.init_y-self.y)**2
        if (diff_x_caree+diff_y_caree <= self.portee_carree):
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
            self.toucher_unite()
            return True
        return False # Le projectile a atteint sa distance maximale
    
    def ciblerdestination(self):
        self.angletrajet=hlp.calcAngle(self.x, self.y, self.cible.x, self.cible.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x, self.y, self.cible.x, self.cible.y)
    
    def toucher_unite(self):
        unites_mortes = set()
        
        liste_objets = sorted(self.objets_cliquables.values(), key = (lambda objet: objet.id))
        for objet in liste_objets:
            if self.lieu == objet.lieu:
                if self.intersection(objet):
                    try:
                        objet.energie -= self.attaque
                        if objet.energie <= 0:
                            unites_mortes.add(objet)
                    except AttributeError: #Les systemes n'ont pas d'attribut energie
                        pass
        
        for unite in unites_mortes:
            self.objets_cliquables.pop(unite.id)
    
    def intersection(self, unite):
        diff_x = abs(self.x - unite.x)
        diff_y = abs(self.y - unite.y)
        if (diff_x < (self.taille + unite.taille)/2 and
            diff_y < (self.taille + unite.taille)/2):
            return True
        else:
            return False
    
class Sonde(Unite):
    def __init__(self, proprietaire, systeme):
        super().__init__(proprietaire, systeme,
                         energie = 100,
                         vitesse = 0.02*5,
                         taille = 16/echelle,
                         cout = 5
                         )

class VaisseauAttaqueGalactique(Unite):
    def __init__(self, proprietaire, systeme):
        super().__init__(proprietaire, systeme,
                         energie = 100,
                         vitesse = 0.02*5,
                         #vitesse = 0.50,
                         attaque = 15,
                         delai_attaque = 2,
                         portee = 50/echelle,
                         portee_projectile = 60/echelle,
                         vitesse_projectile = 6/echelle,
                         taille_projectile = 10/echelle,
                         taille = 16/echelle,
                         cout = 5
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
                         delai_attaque = 3,
                         portee = 15,
                         portee_projectile = 7,
                         taille_projectile = 10,
                         vitesse_projectile = 6,
                         taille = 16/echelle,
                         cout = 5
                         )    
    
class VaisseauCargoSolaire(Unite):
    def __init__(self, proprietaire, planete):
        super().__init__(proprietaire, planete,
                         energie = 100,
                         vitesse = 5,
                         taille = 16/echelle,
                         cout = 5
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
                         vitesse = 0.01*5,
                         taille = 16/echelle,
                         cout = 5
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
                         taille = 20/echelle, 
                         portee = 15,
                         cout = 5
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
                         taille = 20/echelle,
                         portee = 40/echelle,
                         portee_projectile = 10/echelle,
                         capacite = 10,
                         cout = 5
                         )
        
        self.action = self.rotation
    
    def avancer(self):
        if super().avancer():
            #self.vitesse= self.cible.vitesse
            self.rotation()
        else:
            self.vitesse =self.vitesse_defaut
            
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
        
