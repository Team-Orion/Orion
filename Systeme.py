from Id import *
import random
from Planete import *

echelle = 100

class Systeme():
    def __init__(self, x, y, modele):
        self.id=Id.prochainid()
        self.modele = modele
        self.proprietaire="inconnu"
        self.lieu = None
        self.visiteurs={}
        self.diametre=50 # UA unite astronomique = 150000000km
        self.x=x
        self.y=y
        self.etoile=Etoile(self,x,y)
        self.taille = self.etoile.taille*3/echelle #io 02-05
        self.planetes=[] #à questionner #io 11-04
        self.planetesvisites=[]
        self.creerplanetes()
        self.nbfoin=0
        self.nbbois=0
        self.nbargent=0
        self.nbminerai=0
        self.nbpopulation=0
        
    def creerplanetes(self):
            nbplanetes=random.randrange(12)+1
            for i in range(nbplanetes):
                type=random.choice(["roc","gaz","glace"])
                distsol=random.randrange(250)/10 #distance en unite astronomique 150000000km
                taille=random.randrange(50)/100 # en masse solaire
                angle=random.randrange(360)
                x=random.randrange(5000)
                y=random.randrange(5000)
                for i in self.planetes:
                    while (x < i.posXatterrissage+100 and x > i.posXatterrissage-100   or  y < i.posYatterrissage+100 and y > i.posYatterrissage-100) :
                        x=random.randrange(5000)
                        y=random.randrange(5000)
                planete = Planete(self, type, distsol, taille, angle, x, y)
                self.modele.objets_cliquables[planete.id] = planete   
                self.planetes.append(planete) #à suppr #io 11-04
                self.ajusterRessources()
                
    def ajusterRessources(self):
        self.nbfoin=0
        self.nbargent=0
        self.nbminerai=0
        self.nbbois=0
        self.nbpopulation=0
                
                
        for i in self.planetes:
            self.nbfoin+= i.nbfoin
            self.nbbois+= i.nbbois
            self.nbargent+= i.nbargent
            self.nbminerai+=i.nbminerai
            self.nbpopulation+=i.nbpopulation
                
     
