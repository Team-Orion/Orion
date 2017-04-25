from Id import *
class Infrastructure:
    def __init__(self,proprietaire,planete,positionx=0, positiony=0):
        self.x=positionx
        self.y=positiony
        self.id=Id.prochainid()
        self.proprietaire = proprietaire
        self.planete=planete
##a revoir super(). de toutes les infra
class Ferme():
    def __init__(proprietaire, planete):
        super().__init__(self,proprietaire,planete,positionx, positiony)
        self.capacite=100
    def nourrirpopulation(self):
        pass
    def exploitationnouriture(self):
        pass

class TourDefense():
    def __init__(self):
        pass
    def attaquer(self):
        pass
class UsineVaisseau(): 
    def __init__(self):
        self.capacitechargement=0
        pass
    def creervaisseaucargo(self):
        pass
    def creervaisseauattaque(self):
        pass
class HotelVille():
    def __init__(self):
        self.limitepop=500
    def augmentepopulation(self):
        pass
class Universite():
    def __init__(self):
        pass
    def recherche(self):
        pass
class Caserne():
    def __init__(self):
        pass
    def creationtroupe(self):
        pass
    
class Scierie():
    def __init__(self):
        self.bois=0
        pass
    def exploitationbois(self):
        pass
class Temple():
    def __init__(self):
        pass
    def creerdisciple(self):
        pass
class Ruine():
    def __init__(self):
        pass
    def trouverartefact(self):
        pass
class Troupe():
    def __init__(self):
        pass
    def avancer(self):
        pass
    def ciblerdestination(self):
        pass
    def attaque(self):
        pass
    
class Ville():
    def __init__(self,parent,proprio="inconnu",x=2500,y=2500):
        self.id=Id.prochainid()
        self.parent=parent
        self.x=x
        self.y=y
        self.proprietaire=proprio
        self.taille=20
               
class Mine():
    def __init__(self,parent,nom,systemeid,planeteid,x,y):
        self.id=Id.prochainid()
        self.parent=parent
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        self.entrepot=0
        self.capacite=100
    def exploitationminerai(self):
        pass
