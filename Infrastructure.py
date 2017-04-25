from Id import *

class Infrastructure():
    def __init__(self,proprietaire,planete,positionx, positiony):
        self.x=positionx
        self.y=positiony
        self.id=Id.prochainid()
        self.proprietaire = proprietaire
        self.planete=planete

class Ferme(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        self.capacite=100
    def nourrirpopulation(self):
        pass
    def exploitationnouriture(self):
        pass


class TourDefense(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
    def attaquer(self):
        pass
class UsineVaisseau(Infrastructure): 
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        self.capacitechargement=0
        pass
    def creervaisseaucargo(self):
        pass
    def creervaisseauattaque(self):
        pass
class HotelVille(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        self.limitepop=500
    def augmentepopulation(self):
        pass
class Universite(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        
    def recherche(self):
        pass
class Caserne(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
    def creationtroupe(self):
        pass

    
class Scierie(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        self.bois=0
    def exploitationbois(self):
        pass
class Temple(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        pass
    def creerdisciple(self):
        pass
class Ruine(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        pass
    def trouverartefact(self):
        pass
class Troupe(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        pass
    def avancer(self):
        pass
    def ciblerdestination(self):
        pass
    def attaque(self):
        pass
    
class Ville(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        self.taille=20
               
class Mine(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        self.entrepot=0
        self.capacite=100
    def exploitationminerai(self):
        pass
