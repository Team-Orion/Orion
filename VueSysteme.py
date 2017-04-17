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
        
        self.UA2pixel=100 # ainsi la terre serait a 100 pixels du soleil et Uranus a 19 Unites Astronomiques       
        self.largeur=self.modele.diametre*self.UA2pixel
        self.hauteur=self.largeur
        
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Vaisseau-Attaque", command= lambda: self.action_joueur("creervaisseau", {"id_appelant":self.maselection[2],"type_unite": "attaquesolaire"}))
        self.btncreervaisseau.pack()
        
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Vaisseau-Cargo", command= lambda: self.action_joueur("creervaisseau", {"id_appelant":self.maselection[2],"type_unite": "cargosolaire"}))
        self.btncreervaisseau.pack()
        
        self.btncreerstation=Button(self.cadreetataction,text="Creer Station",command=self.creerstation)
        self.btncreerstation.pack()
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir planete",command=self.voirplanete)
        self.btnvuesysteme.pack(side=BOTTOM)
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir galaxie",command=self.voirgalaxie)
        self.btnvuesysteme.pack(side=BOTTOM)
        
        self.population=Label(self.cadreinfo, text="POPULATION :", bg="red")
        self.population.pack(fill=X)
        
        #imgBois = PhotoImage(file="images/ressources/bois.png")
        imgBois = self.parent.images["bois"]
        imgFoin = self.parent.images["foin"]
        imgArgent = self.parent.images["argent"]
        imgMinerai = self.parent.images["minerai"]

        labelBois = Label(self.cadreinfo, image = imgBois)
        labelFoin = Label(self.cadreinfo, image = imgFoin)
        labelArgent = Label(self.cadreinfo, image = imgArgent)
        labelMinerai = Label(self.cadreinfo, image = imgMinerai)

        labelBoistxt = Label(self.cadreinfo, text = "qte Bois")
        labelFointxt = Label(self.cadreinfo, text = "qte Foin")
        labelArgenttxt = Label(self.cadreinfo, text = "qte Argent")
        labelMineraitxt = Label(self.cadreinfo, text = "qte Minerai")


        
        labelBois.pack(fill=X)
        labelBoistxt.pack(fill=X)
        labelFoin.pack(fill=X)
        labelFointxt.pack(fill=X)
        labelArgent.pack(fill=X)
        labelArgenttxt.pack(fill=X)    
        labelMinerai.pack(fill=X)
        labelMineraitxt.pack(fill=X)
        
        labelBois.image=imgBois
        labelFoin.image=imgFoin
        labelArgent=imgArgent
        labelMinerai= imgMinerai
        
        self.lbselectecible=Label(self.cadreetatmsg,text="Choisir cible",bg="darkgrey")
        self.lbselectecible.pack()
        self.changecadreetat(self.cadreetataction)
    
    def voirplanete(self):
        self.parent.voirplanete(self.maselection)

    def voirgalaxie(self):
        self.parent.voirgalaxie()
            
    def initsysteme(self,i):
        self.systeme=i
        self.affichermodelestatique(i)
    
    def affichermodelestatique(self,i):
        xl=self.largeur/2
        yl=self.hauteur/2
        n=i.etoile.taille*self.UA2pixel/2
        mini=2
        UAmini=4
        self.canevas.create_oval(xl-n,yl-n,xl+n,yl+n,fill="yellow",dash=(1,2),width=4,outline="white",
                                 tags=("systeme",i.id,"etoile",str(n),))
        self.minimap.create_oval(100-mini,100-mini,100+mini,100+mini,fill="yellow")
        for p in i.planetes:
            x,y=hlp.getAngledPoint(math.radians(p.angle),p.distance*self.UA2pixel,xl,yl)
            p.x=int(x)
            p.y=int(y)
            n=p.taille*self.UA2pixel
            self.canevas.create_oval(x-n,y-n,x+n,y+n,fill="red",tags=(i.proprietaire,"planete",p.id,"inconnu",i.id,int(x),int(y)))
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
        for i in mod.joueurscles: #a remplacer par dictionnaire # io 11-04
            i=mod.joueurs[i]
            for objet in mod.objets_cliquables.values():
                    if(isinstance(objet, VaisseauCargoSolaire)):
                        self.canevas.create_image(int(objet.x+30), int(objet.y+30), image = self.parent.images["vaisseauattaque"],tags=(objet.proprietaire,"cargosolaire",objet.id,"artefact"))
                    elif(isinstance(objet, VaisseauAttaqueSolaire)):
                        self.canevas.create_image(int(objet.x+30), int(objet.y+30), image = self.parent.images["vaisseauattaque"],tags=(objet.proprietaire,"attaquesolaire",objet.id,"artefact"))
            
    def changerproprietaire(self):
        pass
               
    def afficherselection(self):
        if self.maselection!=None:
            joueur=self.modele.joueurs[self.parent.nom]
            if self.maselection[1]=="planete":
                for i in self.systeme.planetes:
                    if i.id == self.maselection[2]:
                        x=int(self.maselection[3])
                        y=int(self.maselection[4])
                        t=20
                        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(2,2),
                                                 outline=joueur.couleur,
                                                 tags=("select","selecteur"))
      
    def selectionner(self,evt):
        self.changecadreetat(None)
        
        t=self.canevas.gettags("current")
        if t and t[0]!="current":
            if t[1]=="attaquesolaire":
                self.maselection=[self.parent.nom,t[1],t[2]]
                self.montrevaisseauxselection()
            elif t[1]=="cargosolaire":
                self.maselection=[self.parent.nom,t[1],t[2]]
                self.montrevaisseauxselection()
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
            self.lbselectecible.pack_forget()
            self.canevas.delete("selecteur")
            
    def montreplaneteselection(self):
        self.changecadreetat(self.cadreetataction)
    
    def afficherartefacts(self,joueurs):
        pass #print("ARTEFACTS de ",self.nom)
    """
    def cliquerminimap(self,evt):
        x=evt.x
        y=evt.y
        xn=self.largeur/int(self.minimap.winfo_width())
        yn=self.hauteur/int(self.minimap.winfo_height())
        
        ee=self.canevas.winfo_width()
        ii=self.canevas.winfo_height()
        eex=int(ee)/self.largeur/2
        eey=int(ii)/self.hauteur/2
        
        self.canevas.xview(MOVETO, (x*xn/self.largeur)-eex)
        self.canevas.yview(MOVETO, (y*yn/self.hauteur)-eey)
    """
