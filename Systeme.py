from Id import *
import random
from Planete import *

class Systeme():
    def __init__(self,x,y):
        self.id=Id.prochainid()
        self.proprietaire="inconnu"
        self.visiteurs={}
        self.diametre=50 # UA unite astronomique = 150000000km
        self.x=x
        self.y=y
        self.etoile=Etoile(self,x,y)
        self.planetes=[]
        self.planetesvisites=[]
        self.creerplanetes()
        
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
                self.planetes.append(Planete(self,type,distsol,taille,angle,x,y))
