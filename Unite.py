from Id import *
import random
from helper import Helper as hlp
import math
from _overlapped import NULL

#vaisseau baleine                
class Vaisseau():
    def __init__(self,nom,systeme):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x+20/100
        self.y=self.base.y
        self.taille=16
        self.capacite=0
        self.energie=100
        self.vitesse=0.02*5 
        self.cible=None 
        
    def avancer(self):
        rep=None
        if self.cible:
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                self.cible=None
            return rep
        
    def ciblerdestination(self,p):
        self.cible=p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)
        #print("Distance",dist," en ", int(dist/self.vitesse))
    def charger(self):
        pass
    def decharger(self):
        pass
    
class VaisseauAttaqueGalactique():
    def __init__(self,nom,systeme):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x+20/100
        self.y=self.base.y
        self.taille=16
        self.cargo=0
        self.energie=100
        self.vitesse=0.015*5 
        self.cible=None 
        
    def avancer(self):
        rep=None
        if self.cible:
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                self.cible=None
            return rep
        
    def ciblerdestination(self,p):
        self.cible=p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)
    def attaque(self):
        pass

class VaisseauAttaqueSolaire():
    def __init__(self,nom,systeme):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x+20/100
        self.y=self.base.y
        self.taille=16
        self.cargo=0
        self.energie=100
        self.vitesse=random.choice([0.001,0.003,0.005,0.01])*5 #0.5
        self.cible=None 
        
    def avancer(self):
        rep=None
        if self.cible:
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                self.cible=None
            return rep
        
    def ciblerdestination(self,p):
        self.cible=p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)
    def attaque(self):
        pass
    
    
class VaisseauCargoSolaire():
    def __init__(self,nom,systeme):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x+20/100
        self.y=self.base.y
        self.taille=16
        self.cargo=0
        self.energie=100
        self.vitesse=random.choice([0.001,0.003,0.005,0.01])*5 #0.5
        self.cible=None 
        
    def avancer(self):
        rep=None
        if self.cible:
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                self.cible=None
            return rep
        
    def ciblerdestination(self,p):
        self.cible=p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)
        #print("Distance",dist," en ", int(dist/self.vitesse))
    def charger(self):
        pass
    def decharger(self):
        pass
    def chargerressources():
        pass
    
class VaisseauCargoGalactique():
    def __init__(self,nom,systeme):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x+20/100
        self.y=self.base.y
        self.taille=16
        self.cargo=0
        self.energie=100
        self.vitesse=0.005*5 #0.5
        self.cible=None 
        
    def avancer(self):
        rep=None
        if self.cible:
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                self.cible=None
            return rep
        
    def ciblerdestination(self,p):
        self.cible=p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)
        #print("Distance",dist," en ", int(dist/self.vitesse))
    def charger(self):
        pass
    def decharger(self):
        pass
    def chargerressources():
        pass
    
class StationPlanetaire:
    def __init__(self):
         pass
    def creercargogalactique(self):
        pass
    def creerattaquegalactique(self):
        pass
    def creerbouclierplanetaire(self):
        pass
    
class StationGalactique:
    def __init__(self,nom,systeme):
        self.capacite=10 
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x+20/100
        self.y=self.base.y
        self.taille=16
        self.angletrajet=0
        self.angleinverse=0
        self.vitesse=random.choice([0.001,0.003,0.005,0.01])*5 #0.5
        self.cible=None 
    def avancer(self):
        rep=None
        if self.cible:
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                self.cible=None
            return rep
        
    def ciblerdestination(self,p):
        self.cible=p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)
    def reparation(self):
        pass
    def troc(self):
        pass
    def deplacer(self):
        pass
    
class Unite:
    def __init__(self,parent,lieu):
        self.vie=None
        self.vitesse=None
        self.attaque=None
        self.proprietaire=parent
        self.lieu=lieu
        self.x=None
        self.y=None
        self.chemin=None
        self.coords_random() # on initialize x et y
        self.indice_chemin = 0
        self.cible = None
        
    def avancer(self):
        """
        if self.cible and isinstance(self.lieu, Sol):
            self.calculer_chemin()
            diff_x = self.cible.x - self.x
            diff_y = self.cible.y - self.y
            hypot = math.hypot(diff_x, diff_y)
            self.x += diff_x/hypot
            self.y += diff_y/hypot
        """

        #if self.cible:
        if self.chemin and isinstance(self.lieu, Sol):
            
            x_cible, y_cible = self.lieu.matrice_vers_iso(*self.chemin[self.indice_chemin])
            diff_x = x_cible - self.x
            diff_y = y_cible - self.y
            print(diff_x, diff_y)
            if abs(diff_x) >5 or abs(diff_y) >5:
                print("vrai")
                hypot = math.hypot(diff_x, diff_y)
                self.x += diff_x/hypot
                self.y += diff_y/hypot
            elif self.indice_chemin<len(self.chemin)-1:
                self.indice_chemin += 1
                
    
    def assigner_cible(self, cible):
            self.cible = Coord(cible.x, cible.y)
            self.chemin = self.calculer_chemin(cible)
            print(self.chemin)
            self.indice_chemin = 1
            
    """
        def calculer_chemin(self, coords_cible):
            x_init, y_init = self.lieu.iso_vers_matrice(self)
            x_cible, y_cible = self.lieu.iso_vers_matrice(coords_cible)
            self.chemin = None
            
            def chemins_possibles(x, y, chemin):
                x %= self.lieu.matrice_largeur
                y %= self.lieu.matrice_hauteur
                if ((self.chemin is not None and len(chemin)+1 >= len(self.chemin))
                    or self.lieu.terrain[y][x] != "terre"
                    or (x, y) in chemin):
                    pass
                else:
                    chemin.append((x, y))
                    if x == x_cible and y == y_cible:
                        self.chemin = chemin
                    else:
                        chemins_possibles(x+1, y, chemin[:])
                        chemins_possibles(x-1, y, chemin[:])
                        chemins_possibles(x, y+1, chemin[:])
                        chemins_possibles(x, y-1, chemin[:])
            chemins_possibles(x_init, y_init, list())
        
        def calculer_chemin(self, coords_cible):
            x_init, y_init = self.lieu.iso_vers_matrice(self)
            x_cible, y_cible = self.lieu.iso_vers_matrice(coords_cible)
            print(x_cible, y_cible)
            class trouve(Exception): pass
            try:
                chemins = [[(x_init, y_init)]]
                while True:
                    chemins2 = []
                    for chemin in chemins:
                        x, y = chemin[-1]
                        for a in range(-1, 2):
                            for b in range(-1, 2):
                                i = (x+a)%self.lieu.matrice_largeur
                                j = (y+b)%self.lieu.matrice_hauteur
                                if(self.lieu.terrain[j][i] == "terre"
                                   and (i, j) not in chemin):
                                    nouveau_chemin = chemin[:]
                                    nouveau_chemin.append((i, j))
                                    chemins2.append(nouveau_chemin)
                                    truc = random.randrange(9999999999999999)
                                    print(truc)
                                    if i == x_cible and j == y_cible:
                                        print(i, j, truc)
                                        raise trouve
                    chemins = chemins2[:]
            except trouve:
            self.chemin = chemins2[0]
    """                 
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
        test = set()
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

    
    def attaquer(self):
        pass
    
class Disciple(Unite):
    def __init__(self):
        Unite.__init__(self,parent,lieu)
        self.experience=None  # C'est ici qu'on met les attributs propres à chaque unité
    
