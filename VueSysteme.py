from PIL import *
from Perspective import *
import random
import math
from helper import Helper as hlp
import Modele
from Unite import *
from Vue import *
from Planete import *

class VueSysteme(Perspective):
    def __init__(self,parent):
        Perspective.__init__(self,parent)
        self.modele=self.parent.modele
        self.planetes=[]
        self.systeme=None
        self.maselection=None
        
        self.lieu = None
        
        self.UA2pixel=100 # ainsi la terre serait a 100 pixels du soleil et Uranus a 19 Unites Astronomiques       
        self.largeur=self.modele.diametre*self.UA2pixel
        self.hauteur=self.largeur
        
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Vaisseau-Attaque", command= lambda: self.action_joueur("creerunite", {"id_appelant":self.maselection[2],"type_unite": "attaquesolaire"}))
        self.btncreervaisseau.pack()
        
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Vaisseau-Cargo", command= lambda: self.action_joueur("creerunite", {"id_appelant":self.maselection[2],"type_unite": "cargosolaire"}))
        self.btncreervaisseau.pack()
        
        self.btncreerstation=Button(self.cadreetataction,text="Creer Station", command=lambda: self.action_joueur("creerunite", {"id_appelant":self.maselection[2],"type_unite": "stationplanetaire"}))
        self.btncreerstation.pack()
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir planete", command=self.voirplanete)
        self.btnvuesysteme.pack(side=BOTTOM)
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir galaxie", command=self.voirgalaxie)
        self.btnvuesysteme.pack(side=BOTTOM)
        
        self.population=Label(self.cadreinfo, text="POPULATION :", bg="red")
        self.population.pack(fill=X)
        
        imgBois = self.parent.images["bois"]
        imgFoin = self.parent.images["foin"]
        imgArgent = self.parent.images["argent"]
        imgMinerai = self.parent.images["minerai"]

        self.labelBois = Label(self.cadreinfo, image = imgBois)
        self.labelFoin = Label(self.cadreinfo, image = imgFoin)
        self.labelArgent = Label(self.cadreinfo, image = imgArgent)
        self.labelMinerai = Label(self.cadreinfo, image = imgMinerai)

        self.nbbois=0
        self.nbfoin=0
        self.nbargent=0
        self.nbminerai=0
        
        
        self.labelBoistxt = Label(self.cadreinfo, text = "Qte Bois: "+str(self.nbbois))
        self.labelFointxt = Label(self.cadreinfo, text = "Qte Foin: "+str(self.nbfoin))
        self.labelArgenttxt = Label(self.cadreinfo, text = "Qte Argent: "+str(self.nbargent))
        self.labelMineraitxt = Label(self.cadreinfo, text = "Qte Minerai: "+str(self.nbminerai))
        self.labelBois.pack(fill=X)
        self.labelBoistxt.pack(fill=X)
        self.labelFoin.pack(fill=X)
        self.labelFointxt.pack(fill=X)
        self.labelArgent.pack(fill=X)
        self.labelArgenttxt.pack(fill=X)    
        self.labelMinerai.pack(fill=X)
        self.labelMineraitxt.pack(fill=X)
         
        self.labelBois.image=imgBois
        self.labelFoin.image=imgFoin
        self.labelArgent.image=imgArgent
        self.labelMinerai.image= imgMinerai
        
        
        #self.lbselectecible=Label(self.cadreetatmsg,text="Choisir cible",bg="darkgrey") #io 08-05
        #self.lbselectecible.pack() #io -8-05
        self.changecadreetat(self.cadreetataction)
        
    def initier_menu_cargosolaire(self):
        self.cadreetatcargosolaire = None    
        
    def chercheqte(self):
        for objet in self.modele.objets_cliquables.values():
            if objet.id == self.maselection[2]:
                self.nbbois=objet.nbbois
                self.nbfoin=objet.nbfoin
                self.nbargent=objet.nbargent
                self.nbminerai=objet.nbminerai
                
                
                self.labelBois.pack_forget()
                self.labelBoistxt.pack_forget()
                self.labelFoin.pack_forget()
                self.labelFointxt.pack_forget()
                self.labelArgent.pack_forget()
                self.labelArgenttxt.pack_forget()   
                self.labelMinerai.pack_forget()
                self.labelMineraitxt.pack_forget()
                
                self.labelBoistxt = Label(self.cadreinfo, text = "Qte Bois: "+str(self.nbbois))
        
                self.labelFointxt = Label(self.cadreinfo, text = "Qte Foin: "+str(self.nbfoin))
                self.labelArgenttxt = Label(self.cadreinfo, text = "Qte Argent: "+str(self.nbargent))
                self.labelMineraitxt = Label(self.cadreinfo, text = "Qte Minerai: "+str(self.nbminerai))
                self.labelBois.pack(fill=X)
                self.labelBoistxt.pack(fill=X)
                self.labelFoin.pack(fill=X)
                self.labelFointxt.pack(fill=X)
                self.labelArgent.pack(fill=X)
                self.labelArgenttxt.pack(fill=X)    
                self.labelMinerai.pack(fill=X)
                self.labelMineraitxt.pack(fill=X)
    def voirplanete(self):
        self.parent.voirplanete(self.maselection)

    def voirgalaxie(self):
        self.parent.voirgalaxie()
            
    def initsysteme(self,i):
        self.systeme=i
        self.lieu = i
        self.affichermodelestatique(i)
    
    def affichermodelestatique(self,i):
        imgfondpil = Image.new("RGBA", (self.largeur,self.hauteur),"black")
        draw = ImageDraw.Draw(imgfondpil) 
        for j in range(self.largeur*2):
            x=random.randrange(self.largeur)
            y=random.randrange(self.hauteur)
            #draw.ellipse((x,y,x+1,y+1), fill="white")
            draw.ellipse((x,y,x+0.1,y+0.11), fill="white")
        self.images["fond"] = ImageTk.PhotoImage(imgfondpil)
        self.canevas.create_image(self.largeur/2,self.hauteur/2,image=self.images["fond"])
        
        xl=self.largeur/2
        yl=self.hauteur/2
        n=i.etoile.taille*self.UA2pixel/2
        mini=2
        UAmini=4
        self.canevas.create_image(xl, yl, image = self.parent.images["soleil"],tags=("systeme",i.id,"etoile",str(n),))
        self.minimap.create_oval(100-mini,100-mini,100+mini,100+mini,fill="yellow")
        for p in i.planetes:
            x,y=hlp.getAngledPoint(math.radians(p.angle),p.distance*self.UA2pixel,xl,yl)
            p.x=int(x)
            p.y=int(y)
            n=p.taille*self.UA2pixel
            no = random.randrange(1,8)
            self.canevas.create_image(x, y, image = self.parent.images["planete"+str(no)],tags=(i.proprietaire,"planete",p.id,"inconnu",i.id,int(x),int(y)))
            x,y=hlp.getAngledPoint(math.radians(p.angle),p.distance*UAmini,100,100)
            self.minimap.create_oval(x-mini,y-mini,x+mini,y+mini,fill="red",tags=())
            self.planetes.append(p)
            appelant=self.modele.objets_cliquables[p.id] 
            types = {
                     "planete": Planete,
                    }
            laplanete = types["planete"](self.systeme,"habitable",p.distance,p.taille,p.angle,p.x,p.y)
            self.modele.objets_cliquables[laplanete.id] = laplanete
        # NOTE Il y a un probleme ici je ne parviens pas a centrer l'objet convenablement comme dans la fonction 'identifierplanetemere'
        canl=int(self.canevas.cget("width"))/2
        canh=int(self.canevas.cget("height"))/2
        self.canevas.xview(MOVETO, ((self.largeur/2)-canl)/self.largeur)
        self.canevas.yview(MOVETO, ((self.hauteur/2)-canh)/self.hauteur)
                 
    def creerimagefond(self): 
        pass  # on pourrait creer un fond particulier pour un systeme
    
    def afficherdecor(self):
        pass
                
    def creervaisseau(self): 
        pass
    
    def creerstation(self):
        print("Creer station EN CONSTRUCTION")
         
    def afficherpartie(self,mod):
        self.canevas.delete("artefact")
        self.afficherselection()
        for objet in mod.objets_cliquables.values():
            if(objet.lieu == self.lieu):
                if(isinstance(objet, VaisseauCargoSolaire)):
                    angle = math.degrees(objet.angletrajet)
                    if( angle >= -22 and angle <0 or angle <= 23 and angle >=0):
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["0vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle < -22 and angle >= -68) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["45vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle < -68 and angle >= -113) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["90vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle < -113 and angle >= -158) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["135vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle >158 or angle < -158) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["180vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle >113 and angle <= 158) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["225vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle >68 and angle <= 113) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["270vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle >23 and angle <= 68) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["315vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
        
                elif(isinstance(objet, VaisseauAttaqueSolaire)):
                    angle = math.degrees(objet.angletrajet)
                    if( angle >= -22 and angle <0 or angle <= 23 and angle >=0):
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["0vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle < -22 and angle >= -68) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["45vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle < -68 and angle >= -113) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["90vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle < -113 and angle >= -158) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["135vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle >158 or angle < -158) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["180vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle >113 and angle <= 158) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["225vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle >68 and angle <= 113) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["270vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                    elif (angle >23 and angle <= 68) :
                        self.canevas.create_image(objet.x, objet.y, image = self.parent.images["315vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                
                elif(isinstance(objet, Sonde)): 
                        angle = math.degrees(objet.angletrajet)
                        if( angle >= -22 and angle <0 or angle <= 23 and angle >=0):
                            self.canevas.create_image(objet.x, objet.y, image = self.parent.images["0sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle < -22 and angle >= -68) :
                            self.canevas.create_image(objet.x, objet.y, image = self.parent.images["45sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle < -68 and angle >= -113) :
                            self.canevas.create_image(objet.x, objet.y, image = self.parent.images["90sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle < -113 and angle >= -158) :
                            self.canevas.create_image(objet.x, objet.y, image = self.parent.images["135sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >158 or angle < -158) :
                            self.canevas.create_image(objet.x, objet.y, image = self.parent.images["180sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >113 and angle <= 158) :
                            self.canevas.create_image(objet.x, objet.y, image = self.parent.images["225sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >68 and angle <= 113) :
                            self.canevas.create_image(objet.x, objet.y, image = self.parent.images["270sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >23 and angle <= 68) :
                            self.canevas.create_image(objet.x, objet.y, image = self.parent.images["315sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact")) 
                
                
                
                
                elif (isinstance(objet,StationPlanetaire)):
                    self.canevas.create_image(int(objet.x),int(objet.y),image = self.parent.images["stationplanetaire"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))

    def changerproprietaire(self):
        pass
               
    def afficherselection(self):
        e=self.UA2pixel
        self.canevas.delete("selecteur")
        if self.maselection!=None:
            joueur=self.modele.joueurs[self.parent.nom]
            for objet in self.modele.objets_cliquables.values():
                if objet.id == self.maselection[2]:
                    if isinstance(objet, Planete):
                        
                        x=int(self.maselection[3])
                        y=int(self.maselection[4])
                        t= objet.taille*e
                        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(2,2),
                                                 outline=joueur.couleur,
                                                 tags=("select","selecteur"))
                    elif isinstance(objet, Unite):
                        x=objet.x
                        y=objet.y
                        t= objet.taille*e
                        self.canevas.create_rectangle(x-t, y-t, x+t, y+t,dash=(2,2),
                                                      outline= joueur.couleur,
                                                      tags=("select","selecteur"))
                    self.chercheqte()
      
    def selectionner(self,evt):
        self.changecadreetat(None)
        
        t=self.canevas.gettags("current")
        if t and t[0]!="current":
            print(t)
            if t[1]=="unite":
                self.maselection=[self.parent.nom,t[1],t[2]]
                #self.montrevaisseauxselection()
            if t[1] == "planete" :
                self.maselection=[self.parent.nom,t[1],t[2],t[5],t[6],t[4]]  # prop, type, id; self.canevas.find_withtag(CURRENT)#[0]
            if t[1] == "planete" and t[3]=="inconnu":
                nom=t[0]
                idplanete=t[2]
                idsysteme=t[4]
                self.montreplaneteselection()
                
            # ici je veux envoyer un message comme quoi je visite cette planete
            # et me mettre en mode planete sur cette planete, d'une shot
            # ou est-ce que je fais selection seulement pour etre enteriner par un autre bouton
            
            #self.parent.parent.atterrirdestination(nom,idsysteme,idplanete)
        else:
            print("Region inconnue")
            self.maselection=None
            #self.lbselectecible.pack_forget()
            self.canevas.delete("selecteur")
            
    def montreplaneteselection(self):
        self.changecadreetat(self.cadreetataction)
    
    def afficherartefacts(self,joueurs):
        pass #print("ARTEFACTS de ",self.nom)
    
    def cibler(self, evt): #io 02-05
        if self.maselection and self.maselection[1]=="unite":
            cible=self.canevas.gettags("current")
            if cible and cible[0] !="current":
                cible = cible[2]
                mode = "id"
            else:
                x = self.canevas.canvasx(evt.x)#/100
                y = self.canevas.canvasy(evt.y)#/100
                cible = {'x': x, 'y': y}
                mode = "coord"
            self.action_joueur("ciblerdestination", {"id_appelant": self.maselection[2], "cible": cible, "mode": mode})
