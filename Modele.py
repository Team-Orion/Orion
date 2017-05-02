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
    def __init__(self, x, y, lieu = None):
        self.x = x
        self.y = y
        self.lieu = lieu
        self.proprietaire = None
        self.taille = 0

class Joueur():
    def __init__(self,parent,nom,systemeorigine,couleur,codecouleur):
        self.id=Id.prochainid()
        self.artificiel=0   # IA
        self.parent=parent
        self.nom=nom
        self.systemeorigine=systemeorigine
        self.couleur=couleur
        self.codecouleur=codecouleur
        self.systemesvisites= set([systemeorigine])
        self.vaisseauxinterstellaires=[] #à suppr #io 11-04
        self.vaisseauxinterplanetaires=[] #à suppr #io 11-04
        self.messageenvoie=None
        self.actions={"atterrirplanete":self.atterrirplanete,
                      "decouvrirplanete":self.decouvrirplanete,
                      "ciblerdestination":self.ciblerdestination,
                      "creerunite":self.creerunite,
                      "envoimessage":self.envoiemessage,
                      "envoimessagetous":self.envoiemessagetous,
                      "visitersysteme":self.visitersysteme,
                      "creerinfrastructure": self.creerinfrastructure
                     }
    ##lorsqu'un message a ete envoyer au serveur, cette fonction est executer sur toute les machines
    def envoiemessage(self, message, nom,nomquirecoit):
        self.messageenvoie=message
        self.parent.parent.vue.setmessagerecu(self.messageenvoie,nom, nomquirecoit)
    def envoiemessagetous(self, message, nom,nomquirecoit):
        self.messageenvoie=message
        nomquirecoit=""
        self.parent.parent.vue.setmessagerecutous(self.messageenvoie,nom, nomquirecoit)
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
            lacible.lieu = unite.lieu
        unite.cible = lacible
        #unite.ciblerdestination(lacible)
        unite.action = unite.avancer
        return 
    
    def creerinfrastructure(self,id_planete,type_unite,x,y):
        print("creer infrastructure! ici x: ", x, " y: ", y)
        types ={
                "mine": Mine,
                "hotelville":HotelVille,
                "ferme":Ferme,
                "tourdefense":Tourdefense,
                "usine":Usine,
                "universite":Universite,
                "caserne":Caserne,
                "scierie":Scierie,
                "temple":Temple,
                "ruine":Ruine
                }
        infrastructure = types[type_unite](self,id_planete,x,y)
        self.parent.objets_cliquables[infrastructure.id] = infrastructure
        self.parent.objets_cliquables[id_planete].infrastructures.append(infrastructure) 
        self.parent.parent.vue.modecourant.afficher_infrastructures()         
    def creerunite(self, id_appelant, type_unite):
        appelant = self.parent.objets_cliquables[id_appelant]
        types = {
                 "sonde": Sonde,
                 "attaquegalaxie": VaisseauAttaqueGalactique,
                 "cargogalaxie": VaisseauCargoGalactique,
                 "attaquesolaire": VaisseauAttaqueSolaire,
                 "cargosolaire": VaisseauCargoSolaire,
                 "stationgalaxie": StationGalactique,
                 "stationplanetaire": StationPlanetaire
                }
        unite = types[type_unite](self, appelant)
        
        if False:
        #if(unite.cout>appelant.nbargent):
            print("vous n'avez pas assez d'argent")
        else:
            #print(appelant.nbargent)
            appelant.nbargent-=unite.cout
            #print (appelant.nbargent) # ON VA DEVOIR METTRE A JOUR CETTE LIGNE AVEC LA FONCTION CAR ON DOIT DÉDUIRE D'UNE PLANETE LES RESSOURCES NORMALEMENT
            self.vaisseauxinterstellaires.append(unite) #a supprimer #io 18-04
            self.parent.objets_cliquables[unite.id] = unite
        
        
    def decouvrirplanete(self, id_planete, sol):
        planete = self.parent.objets_cliquables[id_planete]
        planete.sol = sol 
        print("Le SOL: ", planete.sol)
        
    def visitersysteme(self, id_appelant):
        for i in self.parent.systemes:
            if i.id==id_appelant:
                self.systemesvisites.add(i)
        
    def prochaineaction(self): # NOTE : cette fonction sera au coeur de votre developpement        
        """
        
        Le contenu de cette fonction a été déplacé dans Modele.prochaineaction.
        
        """

#  DEBUT IA
"""
class IA(Joueur):
    def __init__(self,parent,nom,systemeorigine,couleur,codecouleur):
        Joueur.__init__(self,parent,nom,systemeorigine,couleur,codecouleur)
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
                    self.parent.actionsafaire[c].append([self.nom,"creerunite", {"id_appelant":self.systemeorigine.id,"type_unite": "attaquegalaxie"}])
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
                            #if systtemp:
                            #   vi.ciblerdestination()
                            else:
                                print("JE NE TROUVE PLUS DE CIBLE")
                self.delaiaction=random.randrange(5,10)*20

        else:
            self.delaiaction-=1
"""
        
# FIN IA


#  DEBUT IA
class IA(Joueur):
    def __init__(self,parent,nom,systemeorigine,couleur,codecouleur):
        Joueur.__init__(self,parent,nom,systemeorigine,couleur,codecouleur)
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
                unites_IA = list()
                unites_enemies = list()
                for x in self.parent.objets_cliquables.values():
                    if x.proprietaire == self:
                        unites_IA.append(x)
                    else:
                        unites_enemies.append(x)
                        
                for unite in unites_IA:
                    if isinstance(unite, Unite):
                        cible = random.choice(unites_enemies)
                        if unite.lieu == cible.lieu:
                            unite.cible = random.choice(unites_enemies)
                            unite.action = unite.avancer
                        
                c=self.parent.parent.cadre+5
                if c not in self.parent.actionsafaire.keys(): 
                    self.parent.actionsafaire[c]=[]
                appelant = random.sample(self.systemesvisites, 1)[0]
                type_unite = random.choice(["sonde", "attaquegalaxie", "cargogalaxie", "stationgalaxie"])
                self.parent.actionsafaire[c].append([self.nom,"creerunite", {"id_appelant":appelant.id,"type_unite": type_unite}])
            self.delaiaction=random.randrange(5,10)*5
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
        self.objets_cliquables = {} 
        self.projectiles = list()
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
        couleurs=["firebrick","saddlebrown","seagreen","chartreuse","darkturquoise",
                  "dodgerblue3","purple4","maroon3"]    # IA ajout de 3 couleurs
        
        codecouleur=1
        
        for i in self.joueurscles:
            self.joueurs[i]=Joueur(self,i,planes.pop(0),couleurs.pop(0),codecouleur)
            codecouleur+=1
            
        for i in range(nbias): # IA
            nomia="IA_"+str(i)
            self.joueurscles.append(nomia)
            ia=IA(self,nomia,planes.pop(0),couleurs.pop(0),codecouleur)
            self.joueurs[nomia]=ia  #IA
            self.ias.append(ia)  #IA
            codecouleur+=1
        
    def prochaineaction(self,cadre):
        if cadre in self.actionsafaire:
            for nom_joueur, action, parametres in self.actionsafaire[cadre]:
                self.joueurs[nom_joueur].actions[action](**parametres)
            del self.actionsafaire[cadre]
                
        for i in self.joueurscles: #il se pourrait que cette instruction ne servent plus #io 20-04
            self.joueurs[i].prochaineaction()
            
        for i in self.ias:
            i.analysesituation()
            
        for objet in self.objets_cliquables.values():
            try:
                objet.action()
            except AttributeError:
                pass #l'ojet n'a pas d'attibut "action". C'est normal s'il s'agit d'un système solaire ou une planete.
            except TypeError:
                pass #l'objet n'a pas d'action assignee. C'est normal.
            
        for projectile in self.projectiles:
            if not projectile.action():
                self.projectiles.remove(projectile)
            
    def changerproprietaire(self,nom,couleur,syst):
        self.parent.changerproprietaire(nom,couleur,syst)
                
