from Id import *

class Infrastructure():
    def __init__(self,proprietaire,planete,positionx, positiony):
        self.planete=planete
        #self.x=positionx
        #self.y=positiony
        self.x, self.y = self.init_position(planete, positionx, positiony)
        self.id=Id.prochainid()
        self.proprietaire = proprietaire
        self.lieu = planete
        
    def init_position(self, planete, positionx, positiony):
        class coord(): #N'IMPORTE QUOII
            def __init__(self, positionx, positiony):
                self.x = positionx
                self.y = positiony
        sol = planete.sol
        x, y = sol.iso_vers_matrice(coord(positionx, positiony))
        sol.terrain[y][x] = "infrastructure"
        return sol.matrice_vers_iso(x, y)

class Ferme(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        self.vitesseproduction=1
        self.action = self.exploitationnouriture
        self.compteurexploitation=0
        self.compteurpopulation=0
        
    def nourrirpopulation(self):
        if(self.compteurpopulation<10):
            self.compteurpopulation+=10
        else:
            self.compteurpopulation=0
            if(self.planete.nbpopulation>0):
                self.planete.foinexploite-= self.planete.nbpopulation*0.10
            else:
                self.planete.nbpopulation-=1
                
    def exploitationnouriture(self):
        if(self.planete.nbfoin >0):
            if (self.compteurexploitation < 10):
                self.compteurexploitation+=1
            else:
                self.compteurexploitation=0
                self.planete.foinexploite += self.vitesseproduction
                self.planete.nbfoin-=self.vitesseproduction
        else:
            self.nourrirpopulation()
            



class Tourdefense(Infrastructure):
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
    def attaquer(self):
        pass
class Usine(Infrastructure): 
    def __init__(self,proprietaire,planete,positionx, positiony):
        super().__init__(proprietaire,planete,positionx, positiony)
        self.compteurexploitation=0
        self.action=self.exploitationargent
        self.vitesseproduction=1
        
        
    def exploitationargent(self):
        if(self.planete.nbargent >0):
            if (self.compteurexploitation < 10):
                self.compteurexploitation+=1
            else:
                self.compteurexploitation=0
                self.planete.argentexploite += self.vitesseproduction
                self.planete.nbargent-=self.vitesseproduction

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
        self.action=self.exploitationbois
        print("scierie creee! x: ", positionx, " y: ", positiony)
        
    def exploitationbois(self):
        if(self.planete.nbbois >0):
            if (self.compteurexploitation < 10):
                self.compteurexploitation+=1
            else:
                self.compteurexploitation=0
                self.planete.boisexploite += self.vitesseproduction
                self.planete.nbbois-=self.vitesseproduction

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
        self.compteurexploitation=0
        self.action=self.exploitationminerai
        self.vitesseproduction=1
        
    def exploitationminerai(self):
        if(self.planete.nbminerai >0):
            if (self.compteurexploitation < 10):
                self.compteurexploitation+=1
            else:
                self.compteurexploitation=0
                self.planete.mineraiexploite += self.vitesseproduction
                self.planete.nbminerai-=self.vitesseproduction
    
    
    
    
    
    
    
    
    
    
