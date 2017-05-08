from Id import *

class Infrastructure():
    def __init__(self,proprietaire,planete,positionx, positiony):
        self.x=positionx
        self.y=positiony
        self.id=Id.prochainid()
        self.proprietaire = proprietaire
        self.planete=planete
        self.lieu = planete
        print("La planete : ", planete)

class Ferme(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        self.vitesseproduction=1
    def nourrirpopulation(self):
        pass
    def exploitationnouriture(self):
        pass
        #self.planete.foinexploite += self.vitesseproduction


class Tourdefense(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
    def attaquer(self):
        pass
class Usine(Infrastructure): 
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
        print("universite creee! x: ", positionx, " y: ", positiony)
        
    def recherche(self):
        pass
class Caserne(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        print("caserne creee! x: ", positionx, " y: ", positiony)
    def creationtroupe(self):
        pass

    
class Scierie(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        self.bois=0
        print("scierie creee! x: ", positionx, " y: ", positiony)
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
        print("mine creee! x: ", positionx, " y: ", positiony)
    def exploitationminerai(self):
        pass
    
    
    
    
    
    
    
    
    
    