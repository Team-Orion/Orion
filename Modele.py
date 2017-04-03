# -*- coding: utf-8 -*-
import os,os.path
import sys
import random
from helper import Helper as hlp
import math
import time

class Id():
    id=0
    def prochainid():
        Id.id+=1
        str_id="id_"+str(Id.id)
        return str_id 


        
class Pulsar():
    def __init__(self,x,y):
        self.id=Id.prochainid()
        self.proprietaire="inconnu"
        self.x=x
        self.y=y
        self.periode=random.randrange(20,50,5)
        self.moment=0
        self.phase=1 
        self.mintaille=self.taille=random.randrange(2,4)
        self.maxtaille=self.mintaille++random.randrange(1,3)
        self.pas=self.maxtaille/self.periode
        self.taille=self.mintaille
        
    def evoluer(self):
        self.moment=self.moment+self.phase
        if self.moment==0:
            self.taille=self.mintaille
            self.phase=1
        elif self.moment==self.periode:
            self.taille=self.mintaille+self.maxtaille
            self.phase=-1
        else:
            self.taille=self.mintaille+(self.moment*self.pas)
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
class Ferme():
    def __init__(self):
        self.capacite=100
    def nourrirpopulation(self):
        pass
    def exploitationnouriture(self):
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
                
class Planete():
    def __init__(self,parent,type,dist,taille,angle):
        self.id=Id.prochainid()
        self.parent=parent
        self.posXatterrissage=random.randrange(5000)
        self.posYatterrissage=random.randrange(5000)
        self.infrastructures=[Ville(self)]
        self.proprietaire="inconnu"
        self.visiteurs={}
        self.distance=dist
        self.type=type
        self.taille=taille
        self.angle=angle
    def creationtourdefense(self):
        pass
        
class Etoile():
    def __init__(self,parent,x,y):
        self.id=Id.prochainid()
        self.parent=parent
        self.type=random.choice(["rouge","rouge","rouge",
                                 "jaune","jaune",
                                 "bleu"])
        self.taille=random.randrange(25)/10 +0.1   # en masse solaire
        
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
        systemeplanetaire=random.randrange(5) # 4 chance sur 5 d'avoir des planetes
        if systemeplanetaire:
            nbplanetes=random.randrange(12)+1
            for i in range(nbplanetes):
                type=random.choice(["roc","gaz","glace"])
                distsol=random.randrange(250)/10 #distance en unite astronomique 150000000km
                taille=random.randrange(50)/100 # en masse solaire
                angle=random.randrange(360)
                self.planetes.append(Planete(self,type,distsol,taille,angle))
#vaisseau baleine                
class Vaisseau():
    def __init__(self,nom,systeme):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x
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
class VaisseauAttaqueGalactique():
    def __init__(self,nom,systeme):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x
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

class VaisseauAttaquePlanetaire():
    def __init__(self,nom,systeme):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x
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
    
    
class VaisseauCargoSysteme():
    def __init__(self,nom,systeme):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x
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
    def __init__(self):
        self.capacite=10 
    def reparation(self):
        pass
    def troc(self):
        pass
    def deplacer(self):
        pass
class Joueur():
    def __init__(self,parent,nom,systemeorigine,couleur):
        self.id=Id.prochainid()
        self.artificiel=0   # IA
        self.parent=parent
        self.nom=nom
        self.systemeorigine=systemeorigine
        self.couleur=couleur
        self.systemesvisites=[systemeorigine]
        self.vaisseauxinterstellaires=[]
        self.vaisseauxinterplanetaires=[]
        self.actions={"creervaisseau":self.creervaisseau,
                      "ciblerdestination":self.ciblerdestination,
                      "atterrirplanete":self.atterrirplanete,
                      "visitersysteme":self.visitersysteme,
                      "creermine":self.creermine}
    def alliance(self):
        pass
    def gaintechnologique(self):
        pass
        
    def creermine(self,listeparams):
        nom,systemeid,planeteid,x,y=listeparams
        for i in self.systemesvisites:
            if i.id==systemeid:
                for j in i.planetes:
                    if j.id==planeteid:
                        mine=Mine(self,nom,systemeid,planeteid,x,y)
                        j.infrastructures.append(mine)
                        self.parent.parent.affichermine(nom,systemeid,planeteid,x,y)
                        
    def atterrirplanete(self,d):
        nom,systeid,planeid=d
        for i in self.systemesvisites:
            if i.id==systeid:
                for j in i.planetes:
                    if j.id==planeid:
                        i.planetesvisites.append(j)
                        if nom==self.parent.parent.monnom:
                            self.parent.parent.voirplanete(i.id,j.id)
                        return 1
        
    def visitersysteme(self,systeme_id):
        for i in self.parent.systemes:
            if i.id==systeme_id:
                self.systemesvisites.append(i)
                
    def creervaisseau(self,id):
        for i in self.systemesvisites:
            if i.id==id:
                v=Vaisseau(self.nom,i)
                self.vaisseauxinterstellaires.append(v)
                return 1
        
    def ciblerdestination(self,ids):
        idori,iddesti=ids
        for i in self.vaisseauxinterstellaires:
            if i.id== idori:
                for j in self.parent.systemes:
                    if j.id== iddesti:
                        #i.cible=j
                        i.ciblerdestination(j)
                        return
                for j in self.systemesvisites:
                    if j.id== iddesti:
                        #i.cible=j
                        i.ciblerdestination(j)
                        return
        
    def prochaineaction(self): # NOTE : cette fonction sera au coeur de votre developpement
        global modeauto
        for i in self.vaisseauxinterstellaires:
            if i.cible:
                rep=i.avancer()
                if rep:
                    if rep.proprietaire=="inconnu":
                        if rep not in self.systemesvisites:
                            self.systemesvisites.append(rep)
                            self.parent.changerproprietaire(self.nom,self.couleur,rep)

#  DEBUT IA
class IA(Joueur):
    def __init__(self,parent,nom,systemeorigine,couleur):
        Joueur.__init__(self,parent,nom,systemeorigine,couleur)
        self.contexte="galaxie"
         # le delai est calcule pour chaque prochaine action en seconde
        self.delaiaction=random.randrange(5,10)*20  # le 20 =nbr de boucle par sec.
        
        #self.derniereaction=time.time()
        
    # NOTE sur l'analyse de la situation   
    #          on utilise le temps (time.time() retourne le nombre de secondes depuis 1970) pour le delai de 'cool down'
    #          la decision dependra du contexte (modes de la vue)
    #          aussi presentement - on s'occupe uniquement d'avoir un vaisseau et de deplacer ce vaisseau vers 
    #          le systeme le plus proche non prealablement visite.
    def analysesituation(self):
        #t=time.time()
        if self.delaiaction==0:#self.derniereaction and t-self.derniereaction>self.delaiaction:
            if self.contexte=="galaxie":
                if len(self.vaisseauxinterstellaires)==0:
                    c=self.parent.parent.cadre+5
                    if c not in self.parent.actionsafaire.keys(): 
                        self.parent.actionsafaire[c]=[] 
                    self.parent.actionsafaire[c].append([self.nom,"creervaisseau",self.systemeorigine.id])
                    print("AJOUTER VAISSEAU ",self.systemeorigine.x,self.systemeorigine.y)
                else:
                    for i in self.vaisseauxinterstellaires:
                        sanscible=[]
                        if i.cible==None:
                            sanscible.append(i)
                        if sanscible:
                            vi=random.choice(sanscible)
                            systtemp=None
                            systdist=1000000000000
                            for j in self.parent.systemes:
                                d=hlp.calcDistance(vi.x,vi.y,j.x,j.y)
                                print ("DISTANCE ",i,d)
                                if d<systdist and j not in self.systemesvisites:
                                    systdist=d
                                    systtemp=j
                            if systtemp:
                                vi.ciblerdestination(systtemp)
                                print("CIBLER ",systtemp,systtemp.x,systtemp.y)
                            else:
                                print("JE NE TROUVE PLUS DE CIBLE")
                                
                #self.derniereaction=t
                self.delaiaction=random.randrange(5,10)*20
                
                print("CIV:" ,self.nom,self.couleur, self.delaiaction)
        else:
            self.delaiaction-=1
        
# FIN IA

class Modele():
    def __init__(self,parent,joueurs,dd):
        self.parent=parent
        self.diametre,self.densitestellaire,qteIA=dd
        self.nbsystemes=int(self.diametre**2/self.densitestellaire)
        print(self.nbsystemes)
        self.ias=[]    # IA 
        self.joueurs={}
        self.joueurscles=joueurs
        self.actionsafaire={}
        self.pulsars=[]
        self.systemes=[]
        self.terrain=[]
        self.creersystemes(int(qteIA))  # nombre d'ias a ajouter
        
    def creersystemes(self,nbias):  # IA ajout du parametre du nombre d'ias a ajouter
        
        for i in range(self.nbsystemes):
            x=random.randrange(self.diametre*10)/10
            y=random.randrange(self.diametre*10)/10
            self.systemes.append(Systeme(x,y))
        
        for i in range(20):
            x=random.randrange(self.diametre*10)/10
            y=random.randrange(self.diametre*10)/10
            self.pulsars.append(Pulsar(x,y))
            
        np=len(self.joueurscles) + nbias  # on ajoute le nombre d'ias
        planes=[]
        systemetemp=self.systemes[:]
        while np:
            p=random.choice(systemetemp)
            if p not in planes and len(p.planetes)>0:
                planes.append(p)
                systemetemp.remove(p)
                np-=1
        couleurs=["cyan","goldenrod","orangered","greenyellow",
                  "dodgerblue","yellow2","maroon1","chartreuse3",
                  "firebrick1","MediumOrchid2","DeepPink2","blue"]    # IA ajout de 3 couleurs
        
        
        
        for i in self.joueurscles:
            self.joueurs[i]=Joueur(self,i,planes.pop(0),couleurs.pop(0))
            
        for i in range(nbias): # IA
            nomia="IA_"+str(i)
            self.joueurscles.append(nomia)
            ia=IA(self,nomia,planes.pop(0),couleurs.pop(0))
            self.joueurs[nomia]=ia  #IA
            self.ias.append(ia)  #IA
            
    def creervaisseau(self,systeme):
        self.parent.actions.append([self.parent.monnom,"creervaisseau",systeme])
            
    def prochaineaction(self,cadre):
        if cadre in self.actionsafaire:
            for i in self.actionsafaire[cadre]:
                self.joueurs[i[0]].actions[i[1]](i[2])
            del self.actionsafaire[cadre]
                
        for i in self.joueurscles:
            self.joueurs[i].prochaineaction()
            
        for i in self.ias:
            i.analysesituation()
            
        for i in self.pulsars:
            i.evoluer()
            
    def changerproprietaire(self,nom,couleur,syst):
        self.parent.changerproprietaire(nom,couleur,syst)
                