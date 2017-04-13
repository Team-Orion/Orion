# -*- coding: utf-8 -*-
import os,os.path
import sys

import random
from helper import Helper as hlp
import math
import time
from Unite import *
from Infrastructure import *
from Id import *
from Planete import *
from Systeme import *


class Coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.taille = 0

class Joueur():
    def __init__(self,parent,nom,systemeorigine,couleur):
        self.id=Id.prochainid()
        self.artificiel=0   # IA
        self.parent=parent
        self.nom=nom
        self.systemeorigine=systemeorigine
        self.couleur=couleur
        self.systemesvisites=[systemeorigine]
        self.vaisseauxinterstellaires=[] #à suppr #io 11-04
        self.vaisseauxinterplanetaires=[] #à suppr #io 11-04
        self.messageenvoie=None
        self.actions={"atterrirplanete":self.atterrirplanete,
                      "decouvrirplanete":self.decouvrirplanete,
                      "ciblerdestination":self.ciblerdestination,
                      "creervaisseau":self.creervaisseau,
                      "envoimessage":self.envoiemessage,
                      "visitersysteme":self.visitersysteme
                     }
    ##lorsqu'un message a ete envoyer au serveur, cette fonction est executer sur toute les machines
    def envoiemessage(self, message, nom):
        self.messageenvoie=message
        self.parent.parent.vue.setmessagerecu(self.messageenvoie,nom)
    def alliance(self):
        pass
    def gaintechnologique(self):
        pass
    
                        
    def atterrirplanete(self, id_appelant, id_planete):
        for i in self.systemesvisites:
            if i.id==systeid:
                for j in i.planetes:
                    if j.id==planeid:
                        i.planetesvisites.append(j)
                        if nom==self.parent.parent.monnom:
                            self.parent.parent.voirplanete(i.id,j.id)
                        return 1

    def ciblerdestination(self, id_appelant, cible, mode = "id"):
        unite = self.parent.objets_cliquables[id_appelant]
        if mode == "id":
            lacible = self.parent.objets_cliquables[cible]
        elif mode == "coord":
            lacible = Coord(**cible)
        unite.cible = lacible
        unite.ciblerdestination(lacible)
        return 
                
    def creervaisseau(self, id_appelant, type_unite = "sonde"):
        appelant = self.parent.objets_cliquables[id_appelant]
        types = {
                 "sonde": Vaisseau,
                 "attaquegalaxie": VaisseauAttaqueGalactique,
                 "cargogalaxie": VaisseauCargoGalactique,
                 "attaquesolaire": VaisseauAttaqueSolaire,
                 "cargosolaire": VaisseauCargoSolaire
                }
        unite = types[type_unite](self, appelant)
        self.vaisseauxinterstellaires.append(unite)
        self.parent.objets_cliquables[unite.id] = unite
        
    def decouvrirplanete(self, id_planete):
        planete = self.parent.objets_cliquables[id_planete]
        planete.initier_sol() 
        print("Le SOL: ", planete.sol)
        
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
                            
    def visitersysteme(self, id_appelant):
        for i in self.parent.systemes:
            if i.id==id_appelant:
                self.systemesvisites.append(i)
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
                    self.parent.actionsafaire[c].append([self.nom,"creervaisseau", {"id_appelant":self.systemeorigine.id}])
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
                                if d<systdist and j not in self.systemesvisites:
                                    systdist=d
                                    systtemp=j
                            if systtemp:
                                vi.ciblerdestination(systtemp)
                            else:
                                print("JE NE TROUVE PLUS DE CIBLE")
                self.delaiaction=random.randrange(5,10)*20

        else:
            self.delaiaction-=1
        
# FIN IA

class Modele():
    def __init__(self,parent,joueurs,dd):
        self.parent=parent
        self.diametre,self.densitestellaire,qteIA=dd
        self.nbsystemes=int(self.diametre**2/self.densitestellaire)
        self.ias=[]    # IA 
        self.joueurs={}
        self.joueurscles=joueurs
        self.actionsafaire={}
        self.pulsars=[] #à suppr #io 11-04
        self.systemes=[] #à suppr #io 11-04
        self.terrain=[]
        self.unites = [] #io 03-04
        self.infrastructure = [] #io 03-04
        self.objets_cliquables = {} #io 11-04
        self.creersystemes(int(qteIA))  # nombre d'ias a ajouter
        
    def creersystemes(self,nbias):  # IA ajout du parametre du nombre d'ias a ajouter
        for i in range(self.nbsystemes):
            x=random.randrange(self.diametre*10)/10
            y=random.randrange(self.diametre*10)/10
            for i in self.systemes:
                if x == i.x:
                    x=random.randrange(self.diametre*10)/10
                if y == i.y:
                    y=random.randrange(self.diametre*10)/10
            systeme = Systeme(x,y, self)
            self.systemes.append(systeme)
            self.objets_cliquables[systeme.id] = systeme
        
        for i in range(20):
            x=random.randrange(self.diametre*10)/10
            y=random.randrange(self.diametre*10)/10
            pulsar = Pulsar(x,y) #à suprr #io 11-04
            self.pulsars.append(pulsar) #à suprr #io 11-04
            self.objets_cliquables[pulsar.id] = pulsar
            
        np=len(self.joueurscles) + nbias  # on ajoute le nombre d'ias
        planes=[]
        systemetemp=self.systemes[:]
        while np:
            systeme=random.choice(systemetemp)
            if systeme not in planes and len(systeme.planetes)>0:
                planes.append(systeme)
                systemetemp.remove(systeme)
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
        
    def prochaineaction(self,cadre):
        if cadre in self.actionsafaire:
            for nom_joueur, action, parametres in self.actionsafaire[cadre]:
                self.joueurs[nom_joueur].actions[action](**parametres)
            del self.actionsafaire[cadre]
                
        for i in self.joueurscles:
            self.joueurs[i].prochaineaction()
            
        for i in self.ias:
            i.analysesituation()
            
        for i in self.pulsars:
            i.evoluer()
            
    def changerproprietaire(self,nom,couleur,syst):
        self.parent.changerproprietaire(nom,couleur,syst)
                
