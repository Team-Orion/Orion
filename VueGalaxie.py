from PIL import *
from Perspective import *
import random
from helper import Helper as hlp

from Planete import Pulsar
from Unite import *

class VueGalaxie(Perspective):
    def __init__(self,parent):
        Perspective.__init__(self,parent)
        self.vue = parent
        self.modele=self.parent.modele
        self.maselection=None
        self.AL2pixel=100
        
        self.lieu = None
        
        self.largeur=self.modele.diametre*self.AL2pixel
        self.hauteur=self.largeur
        
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        
        self.labid.bind("<Button-1>",self.identifierplanetemere) #io 03-04
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Sonde", command= lambda: self.action_joueur("creerunite", {"type_unite": "sonde"}))
        self.btncreervaisseau.pack()
        
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Vaisseau-Attaque", command= lambda: self.action_joueur("creerunite", {"type_unite": "attaquegalaxie"}))
        self.btncreervaisseau.pack()
        
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Vaisseau-Cargo", command= lambda: self.action_joueur("creerunite", {"type_unite": "cargogalaxie"}))
        self.btncreervaisseau.pack()
        
        self.btncreerstation=Button(self.cadreetataction,text="Creer Station",command=lambda: self.action_joueur("creerunite",{"type_unite": "stationgalaxie"}))
        self.btncreerstation.pack()
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir systeme",command=self.voirsysteme)
        self.btnvuesysteme.pack(side=BOTTOM)
        
        self.lbselectecible=Label(self.cadreetatmsg,text="Choisir cible",bg="darkgrey")
        self.lbselectecible.pack()
    
    def voirsysteme(self,systeme=None):
        if systeme==None:
            if self.maselection and self.maselection[0]==self.parent.nom and self.maselection[1]=="systeme":
                sid=self.maselection[2]
                for i in self.modele.joueurs[self.parent.nom].systemesvisites:
                    if i.id==sid:
                        s=i
                        break
                self.action_joueur("visitersysteme", {"id_appelant": sid}) #io
                self.parent.voirsysteme(s) #normalement devrait pas planter
        else:                
            sid=systeme.id
            for i in self.modele.joueurs[self.parent.nom].systemesvisites:
                if i.id==sid:
                    s=i
                    break
            # NOTE passer par le serveur est-il requis ????????????
            self.parent.parent.visitersysteme(sid)
            self.parent.voirsysteme(s) #normalement devrait pas planter

        
    def afficherdecor(self):
        self.creerimagefond()
        self.affichermodelestatique()

    def creerimagefond(self): #NOTE - au lieu de la creer a chaque fois on aurait pu utiliser une meme image de fond cree avec PIL
        imgfondpil = Image.new("RGBA", (self.largeur,self.hauteur),"black")
        draw = ImageDraw.Draw(imgfondpil) 
        for i in range(self.largeur*2):
            x=random.randrange(self.largeur)
            y=random.randrange(self.hauteur)
            #draw.ellipse((x,y,x+1,y+1), fill="white")
            draw.ellipse((x,y,x+0.1,y+0.11), fill="white")
        self.images["fond"] = ImageTk.PhotoImage(imgfondpil)
        self.canevas.create_image(self.largeur/2,self.hauteur/2,image=self.images["fond"])
            
    def affichermodelestatique(self): 
        mini=self.largeur/200
        e=self.AL2pixel
        me=200/self.modele.diametre
        for i in self.modele.systemes:
            t=i.etoile.taille*3
            if t<3:
                t=3
            self.canevas.create_oval((i.x*e)-t,(i.y*e)-t,(i.x*e)+t,(i.y*e)+t,fill="grey80",
                                     tags=("inconnu","systeme",i.id,str(i.x),str(i.y)))
            # NOTE pour voir les id des objets systeme, decommentez la ligne suivantes
            #self.canevas.create_text((i.x*e)-t,(i.y*e)-(t*2),text=str(i.id),fill="white")
            
        for i in self.modele.joueurscles:
            couleur=self.modele.joueurs[i].couleur
            m=2
            for j in self.modele.joueurs[i].systemesvisites:
                s=self.canevas.find_withtag(j.id)
                self.canevas.addtag_withtag(i, s)
                self.canevas.itemconfig(s,fill=couleur)
                
                self.minimap.create_oval((j.x*me)-m,(j.y*me)-m,(j.x*me)+m,(j.y*me)+m,fill=couleur)
                
    # ************************ FIN DE LA SECTION D'AMORCE DE LA PARTIE
                
    def identifierplanetemere(self,evt): 
        j=self.modele.joueurs[self.parent.nom]
        couleur=j.couleur
        x=j.systemeorigine.x*self.AL2pixel
        y=j.systemeorigine.y*self.AL2pixel
        id=j.systemeorigine.id
        t=10
        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(3,3),width=2,outline=couleur,
                                 tags=(self.parent.nom,"selecteur",id,""))
        xx=x/self.largeur
        yy=y/self.hauteur
        ee=self.canevas.winfo_width()
        ii=self.canevas.winfo_height()
        eex=int(ee)/self.largeur/2
        self.canevas.xview(MOVETO, xx-eex)
        eey=int(ii)/self.hauteur/2
        self.canevas.yview(MOVETO, yy-eey)
        
    def creervaisseau(self): 
        if self.maselection:
            self.parent.parent.creervaisseau(self.maselection[2])
            self.maselection=None
            self.canevas.delete("selecteur")
    
    def creerstation(self):
        print("Creer station EN CONSTRUCTION")
        
    def afficherpartie(self,mod):
        self.canevas.delete("artefact")
        self.canevas.delete("pulsar")
        self.canevas.delete("projectile")
        self.afficherselection()
        
        e=self.AL2pixel

        
        for objet in mod.objets_cliquables.values():
            if(objet.lieu == self.lieu):
                if(isinstance(objet, VaisseauAttaqueGalactique)):
                     angle = math.degrees(objet.angletrajet)
                     if( angle >= -22 and angle <0 or angle <= 23 and angle >=0):
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["0vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                     elif (angle < -22 and angle >= -68) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["45vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                     elif (angle < -68 and angle >= -113) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["90vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                     elif (angle < -113 and angle >= -158) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["135vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                     elif (angle >158 or angle < -158) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["180vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                     elif (angle >113 and angle <= 158) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["225vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                     elif (angle >68 and angle <= 113) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["270vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                     elif (angle >23 and angle <= 68) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["315vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                
                elif isinstance(objet, Pulsar):
                    t=objet.taille
                    self.canevas.create_oval((objet.x*e)-t,(objet.y*e)-t,(objet.x*e)+t,(objet.y*e)+t,fill="orchid3",dash=(1,1),
                                                     outline="maroon1",width=2,
                                         tags=("inconnu","pulsar",objet.id))
                    
                elif (isinstance(objet, VaisseauCargoGalactique)):
                        angle = math.degrees(objet.angletrajet)
                        if( angle >= -22 and angle <0 or angle <= 23 and angle >=0):
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["0vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle < -22 and angle >= -68) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["45vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle < -68 and angle >= -113) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["90vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle < -113 and angle >= -158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["135vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >158 or angle < -158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["180vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >113 and angle <= 158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["225vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >68 and angle <= 113) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["270vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >23 and angle <= 68) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["315vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                
                elif(isinstance(objet, Sonde)): 
                        angle = math.degrees(objet.angletrajet)
                        if( angle >= -22 and angle <0 or angle <= 23 and angle >=0):
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["0sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle < -22 and angle >= -68) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["45sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle < -68 and angle >= -113) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["90sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle < -113 and angle >= -158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["135sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >158 or angle < -158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["180sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >113 and angle <= 158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["225sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >68 and angle <= 113) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["270sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
                        elif (angle >23 and angle <= 68) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["315sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact")) 
                        
                elif (isinstance(objet,StationGalactique)):
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["stationgalaxie"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire,"unite",objet.id,"artefact"))
          
        for proj in mod.projectiles:
            self.canevas.create_rectangle(proj.x*e-2, proj.y*e-2, proj.x*e+2, proj.y*e+2, fill = "red", tag=("projectile",))
            
    def changerproprietaire(self,prop,couleur,systeme):
        #lp=self.canevas.find_withtag(systeme.id) 
        self.canevas.addtag_withtag(prop,systeme.id)
        
    def changerproprietaire1(self,prop,couleur,systeme): 
        id=str(systeme.id)
        lp=self.canevas.find_withtag(id)
        self.canevas.itemconfig(lp[0],fill=couleur)
        t=(prop,"systeme",id,"systemevisite",str(len(systeme.planetes)),systeme.etoile.type)
        self.canevas.itemconfig(lp[0],tags=t)
            
    def afficherselection(self):
        self.canevas.delete("selecteur")
        if self.maselection!=None:
            joueur=self.modele.joueurs[self.parent.nom]
            
            e=self.AL2pixel
            if self.maselection[1]=="systeme":
                for i in joueur.systemesvisites:
                    if i.id == self.maselection[2]:
                        x=i.x
                        y=i.y
                        t=10
                        self.canevas.create_oval((x*e)-t,(y*e)-t,(x*e)+t,(y*e)+t,dash=(2,2),
                                                 outline=joueur.couleur,
                                                 tags=("select","selecteur"))
            elif self.maselection[1]=="unite":
                for i in joueur.vaisseauxinterstellaires:
                    if i.id == self.maselection[2]:
                        x=i.x
                        y=i.y
                        t=10
                        self.canevas.create_rectangle((x*e)-t,(y*e)-t,(x*e)+t,(y*e)+t,dash=(2,2),
                                                      outline=joueur.couleur,
                                                      tags=("select","selecteur"))
      
    def selectionner(self,evt):
        self.changecadreetat(None)
        t=self.canevas.gettags("current")
        if t and t[0]!="current":

            if t[1]=="unite":
                self.maselection=[self.parent.nom,t[1],t[2]]
                self.montrevaisseauxselection()
            
            elif t[1]=="systeme":
                #if self.parent.nom in t:
                self.maselection=[self.parent.nom,t[1],t[2]]
                self.montresystemeselection()
                #else:    
                #    print("IN systeme + RIEN")
                #    self.maselection=None
                #    self.maselection=[self.parent.nom,t[1],t[2]]
                #    self.lbselectecible.pack_forget()
                #    self.canevas.delete("selecteur")
            else:
                print("Objet inconnu")
        else:
            print("Region inconnue")
            self.maselection=None
            self.lbselectecible.pack_forget()
            self.canevas.delete("selecteur")
            
    def montresystemeselection(self):
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
                x = self.canevas.canvasx(evt.x)/echelle
                y = self.canevas.canvasy(evt.y)/echelle
                cible = {'x': x, 'y': y}
                mode = "coord"
            self.action_joueur("ciblerdestination", {"id_appelant": self.maselection[2], "cible": cible, "mode": mode})
