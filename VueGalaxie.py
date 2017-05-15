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
        self.nbbois=0
        self.nbfoin=0
        self.nbargent=0
        self.nbminerai=0
        
        self.cadreetatsysteme=Frame(self.cadreetat,width=200,height=200,bg="grey20")
        self.initier_cadresysteme()
        
        self.cadreetatsonde=Frame(self.cadreetat,width=200,height=200,bg="grey20")
        self.initier_cadresonde()
        
        self.cadreetatattaquegalactique=Frame(self.cadreetat,width=200,height=200,bg="grey20")
        self.initier_cadreetatattaquegalactique()
        
        self.cadreetatcargogalactique=Frame(self.cadreetat,width=200,height=200,bg="grey20")
        self.initier_cadreetatcargogalactique()
        
        self.cadreetatstationgalactique=Frame(self.cadreetat,width=200,height=200,bg="grey20")
        self.initier_cadreetatstationgalactique()

        self.lieu = None
        
        self.largeur=self.modele.diametre*self.AL2pixel
        self.hauteur=self.largeur
        
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        
        
        self.labid.bind("<Button-1>",self.identifierplanetemere)
        
        self.tags_unite = ("sonde", "cargo_galactique", "attaque_galactique", "station_galactique")

    def initier_cadresysteme(self):
        self.btncreervaisseau=Button(self.cadreetatsysteme,text="Creer Sonde", command= lambda: self.action_joueur("creerunite", {"type_unite": "sonde"}))
        self.btncreervaisseau.pack()
        
        self.btncreervaisseau=Button(self.cadreetatsysteme,text="Creer Vaisseau-Attaque", command= lambda: self.action_joueur("creerunite", {"type_unite": "attaquegalaxie"}))
        self.btncreervaisseau.pack()
        
        self.btncreervaisseau=Button(self.cadreetatsysteme,text="Creer Vaisseau-Cargo", command= lambda: self.action_joueur("creerunite", {"type_unite": "cargogalaxie"}))
        self.btncreervaisseau.pack()
        
        self.btncreerstation=Button(self.cadreetatsysteme,text="Creer Station",command=lambda: self.action_joueur("creerunite",{"type_unite": "stationgalaxie"}))
        self.btncreerstation.pack()
        self.btnvuesysteme=Button(self.cadreetatsysteme,text="Voir systeme",command=self.voirsysteme)
        self.btnvuesysteme.pack()
        
        self.packer_ressources(self.cadreetatsysteme)
        
        
    def initier_cadresonde(self):
        self.btnvisiter=Button(self.cadreetatsonde,text="Visiter", command=lambda: self.action_joueur("ciblerdestination", {"mode": "visiter"}, selectionner = True))
        self.btnvisiter.pack()
        self.packer_ressources(self.cadreetatsonde)
        
    def initier_cadreetatattaquegalactique(self):
        self.btnvisiter=Button(self.cadreetatattaquegalactique,text="Visiter", command=lambda: self.action_joueur("ciblerdestination", {"mode": "visiter"}, selectionner = True))
        self.btnvisiter.pack()
        self.packer_ressources(self.cadreetatattaquegalactique)
        
    def initier_cadreetatcargogalactique(self):
        self.btnvisiter=Button(self.cadreetatcargogalactique,text="Visiter", command=lambda: self.action_joueur("ciblerdestination", {"mode": "visiter"}, selectionner = True))
        self.btnvisiter.pack()
        self.packer_ressources(self.cadreetatcargogalactique)
        
        
    def initier_cadreetatstationgalactique(self):        
        pass
    
    def packer_ressources(self, cadreetat):
        self.labelBois = Label(cadreetat, image = self.parent.images["bois"])
        self.labelFoin = Label(cadreetat, image = self.parent.images["foin"])
        self.labelArgent = Label(cadreetat, image = self.parent.images["argent"])
        self.labelMinerai = Label(cadreetat, image = self.parent.images["minerai"])
        
        self.labelBoistxt = Label(cadreetat, text = "Qte Bois: "+str(self.nbbois))
        self.labelFointxt = Label(cadreetat, text = "Qte Foin: "+str(self.nbfoin))
        self.labelArgenttxt = Label(cadreetat, text = "Qte Argent: "+str(self.nbargent))
        self.labelMineraitxt = Label(cadreetat, text = "Qte Minerai: "+str(self.nbminerai))
        
        
        self.labelMinerai.pack(fill=X,side=BOTTOM)
        self.labelMineraitxt.pack(fill=X,side=BOTTOM)
        self.labelArgent.pack(fill=X,side = BOTTOM)
        self.labelArgenttxt.pack(fill=X,side=BOTTOM)
        self.labelFoin.pack(fill=X,side = BOTTOM)
        self.labelFointxt.pack(fill=X,side = BOTTOM)
        self.labelBois.pack(fill=X,side=BOTTOM)
        self.labelBoistxt.pack(fill=X,side = BOTTOM)

    def voirsysteme(self,systeme=None):
        if systeme==None:
            if self.maselection and self.maselection[0]==self.parent.nom and self.maselection[1]=="systeme":
                sid=self.maselection[2]
                for i in self.modele.joueurs[self.parent.nom].systemesvisites:
                    if i.id==sid:
                        s=i
                        self.action_joueur("visitersysteme", {"id_appelant": sid}) #io
                        self.parent.voirsysteme(s) #normalement devrait pas planter
                        break
                
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
        
    def chercheqte(self):
        for objet in self.modele.objets_cliquables.values():
            if objet.id == self.maselection[2]:
                objet.ajusterRessources()
                
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
                
                self.labelBoistxt = Label(self.cadreetataction, text = "Qte Bois: "+str(self.nbbois))
        
                self.labelFointxt = Label(self.cadreetataction, text = "Qte Foin: "+str(self.nbfoin))
                self.labelArgenttxt = Label(self.cadreetataction, text = "Qte Argent: "+str(self.nbargent))
                self.labelMineraitxt = Label(self.cadreetataction, text = "Qte Minerai: "+str(self.nbminerai))
                self.labelBois.pack(fill=X)
                self.labelBoistxt.pack(fill=X)
                self.labelFoin.pack(fill=X)
                self.labelFointxt.pack(fill=X)
                self.labelArgent.pack(fill=X)
                self.labelArgenttxt.pack(fill=X)    
                self.labelMinerai.pack(fill=X)
                self.labelMineraitxt.pack(fill=X)
                
                
    

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
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["0vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"attaque_galactique",objet.id,"artefact"))
                     elif (angle < -22 and angle >= -68) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["45vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"attaque_galactique",objet.id,"artefact"))
                     elif (angle < -68 and angle >= -113) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["90vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom, "attaque_galactique",objet.id,"artefact"))
                     elif (angle < -113 and angle >= -158) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["135vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"attaque_galactique",objet.id,"artefact"))
                     elif (angle >158 or angle < -158) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["180vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"attaque_galactique",objet.id,"artefact"))
                     elif (angle >113 and angle <= 158) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["225vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"attaque_galactique",objet.id,"artefact"))
                     elif (angle >68 and angle <= 113) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["270vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"attaque_galactique",objet.id,"artefact"))
                     elif (angle >23 and angle <= 68) :
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["315vaisseauattaque"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"attaque_galactique",objet.id,"artefact"))
                
                elif isinstance(objet, Pulsar):
                    t=objet.taille
                    self.canevas.create_image((objet.x*e), (objet.y*e), image = self.parent.images["pulsar"],tags=("inconnu","pulsar",objet.id))
                    
                elif (isinstance(objet, VaisseauCargoGalactique)):
                        angle = math.degrees(objet.angletrajet)
                        if( angle >= -22 and angle <0 or angle <= 23 and angle >=0):
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["0vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"cargo_galactique",objet.id,"artefact"))
                        elif (angle < -22 and angle >= -68) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["45vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"cargo_galactique",objet.id,"artefact"))
                        elif (angle < -68 and angle >= -113) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["90vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"cargo_galactique",objet.id,"artefact"))
                        elif (angle < -113 and angle >= -158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["135vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"cargo_galactique",objet.id,"artefact"))
                        elif (angle >158 or angle < -158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["180vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"cargo_galactique",objet.id,"artefact"))
                        elif (angle >113 and angle <= 158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["225vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"cargo_galactique",objet.id,"artefact"))
                        elif (angle >68 and angle <= 113) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["270vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"cargo_galactique",objet.id,"artefact"))
                        elif (angle >23 and angle <= 68) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["315vaisseaucargo"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"cargo_galactique",objet.id,"artefact"))
                
                elif(isinstance(objet, Sonde)): 
                        angle = math.degrees(objet.angletrajet)
                        if( angle >= -22 and angle <0 or angle <= 23 and angle >=0):
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["0sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"sonde",objet.id,"artefact"))
                        elif (angle < -22 and angle >= -68) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["45sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"sonde",objet.id,"artefact"))
                        elif (angle < -68 and angle >= -113) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["90sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"sonde",objet.id,"artefact"))
                        elif (angle < -113 and angle >= -158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["135sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"sonde",objet.id,"artefact"))
                        elif (angle >158 or angle < -158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["180sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"sonde",objet.id,"artefact"))
                        elif (angle >113 and angle <= 158) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["225sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"sonde",objet.id,"artefact"))
                        elif (angle >68 and angle <= 113) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["270sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"sonde",objet.id,"artefact"))
                        elif (angle >23 and angle <= 68) :
                            self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["315sonde"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"sonde",objet.id,"artefact")) 
                        
                elif (isinstance(objet,StationGalactique)):
                        self.canevas.create_image(objet.x*e, objet.y*e, image = self.vue.images["stationgalaxie"+str(objet.proprietaire.codecouleur)],tags=(objet.proprietaire.nom,"station_galactique",objet.id,"artefact"))
          
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
                        self.chercheqte()
            elif self.maselection[1] in self.tags_unite:
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
        if self.action_attente is None:
            if t and t[0]!="current":
                if t[1] in self.tags_unite and t[0]==self.parent.nom:
                    self.maselection=[self.parent.nom,t[1],t[2]]
                    if t[1] == "sonde": 
                        self.changecadreetat(self.cadreetatsonde)
                    if t[1] == "cadreetat_attaquegalactique": 
                        self.changecadreetat(self.cadreetatattaquegalactique)
                    if t[1] == "cargo_galactique": 
                        self.changecadreetat(self.cadreetatcargogalactique)
                    if t[1] == "station_galactique": 
                        self.changecadreetat(self.cadreetatstationgalactique)
                
                elif t[1]=="systeme" : #and self.parent.nom in t: #manque la logique pour déterminer si on peut fabvriquer à partir du système #io 09-05
                    self.maselection=[self.parent.nom,t[1],t[2]]
                    self.changecadreetat(self.cadreetatsysteme)
                else:
                    print("Objet inconnu")
            else:
                print("Region inconnue")
                self.maselection=None
                self.canevas.delete("selecteur")
        else:
            try:
                self.action_attente["parametres"]["cible"] =  t[2]
                self.action_joueur(**self.action_attente)
                self.action_attente = None
            except IndexError:
                pass
    
    def afficherartefacts(self,joueurs):
        pass #print("ARTEFACTS de ",self.nom)    

        
    def afficherartefacts(self,joueurs):
        pass #print("ARTEFACTS de ",self.nom)
    
    def cibler(self, evt): #io 02-05
        if self.maselection and self.maselection[1] in self.tags_unite:
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
