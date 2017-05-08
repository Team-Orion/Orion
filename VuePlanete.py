# continuer les infrastructures

from PIL import *
from Perspective import *
import random
from helper import Helper as hlp
import tkinter
from Infrastructure import *

class VuePlanete(Perspective):
    def __init__(self,parent,systeme,planete):
        Perspective.__init__(self,parent)
        self.modele=self.parent.modele
        self.planete = planete
        self.sol = planete.sol
        self.systeme=systeme
        self.infrastructures={}
        self.maselection=None
        self.macommande=None
        
        self.KM2pixel=100 # ainsi la terre serait a 100 pixels du soleil et Uranus a 19 Unites Astronomique       
        self.largeur=self.modele.diametre*self.KM2pixel
        self.hauteur=self.largeur
        
        self.action_attente = None  #fp 25 avril
        
        """
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        self.canevas.config(bg="sandy brown")
        
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Mine",command=self.creermine)
        self.btncreervaisseau.pack()
        
        self.btncreerstation=Button(self.cadreetataction,text="Creer Manufacture",command=self.creermanufacture)
        self.btncreerstation.pack()
        """
        
        #self.canevas.createTextNode("salutt")
        
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir Systeme",command=self.voirsysteme)
        self.btnvuesysteme.pack(side=BOTTOM)
        
        self.btncreermine=Button(self.cadreetataction,text="Construire Mine",command=self.creermine)
        self.btncreermine.pack(side=BOTTOM)

        self.btncreerferme=Button(self.cadreetataction,text="Construire Ferme",command=self.creerferme)
        self.btncreerferme.pack(side=BOTTOM)
        
        self.btnhotelville=Button(self.cadreetataction,text="Construire Hotel ville", command=self.creerhotelville)
        self.btnhotelville.pack()
        
        self.btntourdefense=Button(self.cadreetataction,text="Construire Tour de defense",command=self.creertourdefense)
        self.btntourdefense.pack(side=BOTTOM)
        
        self.btnusine=Button(self.cadreetataction,text="Construire Usine",command=self.creerusine)
        self.btnusine.pack(side=BOTTOM)
        
        self.btnuniversite=Button(self.cadreetataction,text="Construire Universite",command=self.creeruniversite)
        self.btnuniversite.pack(side=BOTTOM)
        
        self.btncaserne=Button(self.cadreetataction,text="Construire Caserne",command=self.creercaserne)
        self.btncaserne.pack(side=BOTTOM)
        
        self.btnscierie=Button(self.cadreetataction,text="Construire Scierie",command=self.creerscierie)
        self.btnscierie.pack(side=BOTTOM)
        
        self.btntemple=Button(self.cadreetataction,text="Construire Temple",command=self.creertemple)
        self.btntemple.pack(side=BOTTOM)
        
        self.btnruine=Button(self.cadreetataction,text="Construire Ruine",command=self.creerruine)
        self.btnruine.pack(side=BOTTOM)

        self.population=Label(self.cadreinfo, text="POPULATION :", bg="red")
        self.population.pack(fill=X)
        
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
        
        labelBois.image = imgBois
        labelFoin.image = imgFoin
        labelArgent.image = imgArgent
        labelMinerai.image = imgMinerai

        self.changecadreetat(self.cadreetataction)
    
    
    def creermine(self,evt):
        #img = Label("images/ressources/bois.png")
        self.action_attente = "mine"
        #self.canevas.create_image("images/ressources/bois.png")
        #image = self.parent.images["ferme"]
        #self.canevas.create_image(evt.x, evt.y,image = image, tags=("mine",))
        #self.parent.root.config(cursor='clock red red')
        #self.canevas.create_text(10, 450, text=str("Cliquez a l'endroit ou vous voulez voir votre infrastructure."),font=("calibri", 28), fill="#2360fc", anchor="nw", tag="messagetemporaire")
        self.macommande="mine"
    
    def creerferme(self):
        self.action_attente = "ferme"
        self.macommande="ferme"
        
    def creerhotelville(self):
        self.action_attente = "hotelville"
        self.macommande="hotelville"
        
    def creertourdefense(self):
        self.action_attente = "tourdefense"
        self.macommande="tourdefense"
        
    def creerusine(self):
        self.action_attente = "usine"
        self.macommande="usine"
        
    def creeruniversite(self):
        self.action_attente = "universite"
        self.macommande="universite"
        
    def creercaserne(self):
        self.action_attente = "caserne"
        self.macommande="caserne"
        
    def creerscierie(self):
        self.action_attente = "scierie"
        self.macommande="scierie"
        
    def creertemple(self):
        self.action_attente = "temple"
        self.macommande="temple"
        
    def creerruine(self):
        self.action_attente = "ruine"
        self.macommande="ruine"
    
    def creermanufacture(self):
        pass
    
    def voirsysteme(self):
        for i in self.modele.joueurs[self.parent.nom].systemesvisites:
            if i.id==self.systeme.id:
                self.parent.voirsysteme(i)
    
    """        
    def initplanete(self,sys,plane):
        print(123)
        s=None
        p=None
        for i in self.modele.joueurs[self.parent.nom].systemesvisites:
            if i.id==sys:
                s=i
                for j in i.planetes:
                    if j.id==plane:
                        p=j
                        break
        self.systemeid=sys
        self.planeteid=plane
        #self.affichermodelestatique(s,p)
    
    
    def affichermodelestatique(self,s,p):
        xl=self.largeur/2
        yl=self.hauteur/2
        mini=2
        UAmini=4
        for i in p.infrastructures:
            pass
        
        self.canevas.create_image(p.posXatterrissage,p.posYatterrissage,image=self.parent.images["tortue"])
        
        canl=int(p.posXatterrissage-100)/self.largeur
        canh=int(p.posYatterrissage-100)/self.hauteur
        self.canevas.xview(MOVETO,canl)
        self.canevas.yview(MOVETO, canh)
        
        pass  
     """   
    def afficherdecor(self):
        pass
                
    def creervaisseau(self):
        pass
    
    def creerstation(self):
        print("Creer station EN CONSTRUCTION")
         
    def afficherpartie(self,mod):
        pass
            
    def changerproprietaire(self,prop,couleur,systeme): 
        pass
               
    def afficherselection(self):
        pass
      
    def selectionner(self,evt):
        self.canevas.delete("messagetemporaire")
        x, y=self.sol.iso_vers_matrice(evt)
        print("action_attente: ", str(self.action_attente))
        t=self.canevas.gettags("current")
        #print("x: ", x, " y: ", y)
        #print("terrain" ,self.sol.terrain[y][x])
        #print("t: ", t)
        if(t):          # fp 2 mai  if (t) parce que si on clique dans l'espace, on veut que rien se passe (versus toute plante)
            if not self.action_attente:
               """
                if t and t[0]!="current":   # fp 2 mai Est-ce que tout ca pourrait sauter par hasard?? 
                    if t[0]==self.parent.nom:
                        pass
                    elif t[1]=="systeme":
                        pass
                else:
                    if self.macommande:
                        x=self.canevas.canvasx(evt.x)
                        y=self.canevas.canvasy(evt.y)
                        self.parent.parent.creermine(self.parent.nom,self.systemeid,self.planeteid,x,y)
                        self.macommande=None
                """
            else:
                # fp 2 mai.  pour empecher qu'on construise dans l'eau
                if(self.sol.terrain[y][x] == "terre" or self.sol.terrain[y][x] == "colline"  or t[0] == 'terre1' or t[0] == 'terre2' or t[0] == 'terre3' or t[0] == 'colline'):
                    self.action_joueur("creerinfrastructure", {"id_planete": self.planete.id, "type_unite":self.action_attente, "x":evt.x, "y":evt.y})
                    self.action_attente = None
                else:
                    #print("on ne peut pas construire ici!")
                    self.canevas.create_text(10, 500, text=str("On ne peut pas construire si pres de l'eau!"),font=("calibri", 36), fill="#ff0022", anchor="nw", tag="messagetemporaire")
                    # fp 8 mai  Il faudrait une boucle pour que le message s'efface apres X secondes
                    
                

    def montresystemeselection(self):
        self.changecadreetat(self.cadreetataction)
        
    def montrevaisseauxselection(self):
        self.changecadreetat(self.cadreetatmsg)
    
    def afficherartefacts(self,joueurs):
        pass #print("ARTEFACTS de ",self.nom)

    #### Affichage du terrain
    def initier_affichage(self):
        if self.sol is None:
            self.sol = self.planete.initier_sol()
            self.action_joueur("decouvrirplanete", {"id_planete": self.planete.id, "sol": self.sol})
        self.afficher_sol()
        self.afficher_infrastructures()
    
    def afficher_base(self):
        for y in range(self.sol.matrice_hauteur):
            for x in range(self.sol.matrice_largeur):
                type_tuile = "terre" + str(random.randrange(1, 4))
                image = self.parent.images[type_tuile]
                self.afficher_tuile(x, y, image, type_tuile)

    def afficher_sol(self):
        self.afficher_base()
        for y in range(self.sol.matrice_hauteur):
            for x in range(self.sol.matrice_largeur):
                type_tuile = self.sol.terrain[y][x]
                if type_tuile != "terre":
                    if  type_tuile == "eau":
                        type_tuile = self.selectionner_tuile_eau(x, y)
                    elif type_tuile == "colline":
                        type_tuile = self.selectionner_tuile_colline(x, y)
                    image = self.parent.images[type_tuile]
                    self.afficher_tuile(x, y, image, type_tuile)
                    
    def afficher_tuile(self, x, y, image, type_tuile):
        vue_x, vue_y = self.sol.matrice_vers_iso(x, y)
        self.canevas.create_image(vue_x, vue_y,
                                      image = image, tags=(type_tuile))

    def afficher_infrastructures(self):
        for objet in self.parent.parent.modele.objets_cliquables.values():
            if(isinstance(objet, Infrastructure) and objet.lieu == self.planete.id):
                if(isinstance(objet, Mine)):
                    print(objet.x, objet.y)
                    print("type objet ",type(objet))
                    image = self.parent.images["mine"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("mine",))
                if(isinstance(objet, Ferme)):
                    print(objet.x, objet.y)
                    print("type objet ",type(objet))
                    image = self.parent.images["ferme"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("ferme",))
                if(isinstance(objet, Tourdefense)):
                    print(objet.x, objet.y)
                    print("type objet ",type(objet))
                    image = self.parent.images["tourdefense"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("tourdefense",))
                if(isinstance(objet, Temple)):
                    image = self.parent.images["temple"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("temple",))
                if(isinstance(objet, HotelVille)):
                    image = self.parent.images["hotelville"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("hotelville",))
       
                if(isinstance(objet, Ruine)):
                    image = self.parent.images["ruine"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("ruine",))
    
                if(isinstance(objet, Universite)):
                    image = self.parent.images["universite"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("universite",))
    
                if(isinstance(objet, Usine)):
                    image = self.parent.images["usine"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("usine",))

                if(isinstance(objet, Scierie)):
                    image = self.parent.images["scierie"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("scierie",))
                    
                if(isinstance(objet, Caserne)):
                    image = self.parent.images["caserne"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("caserne",))                    
                if(isinstance(objet, Universite)):
                    image = self.parent.images["universite"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("universite",))
    
    def selectionner_tuile_colline(self, x, y):
        nom_tuile = "colline"
        i = (x+1)%self.sol.matrice_largeur #pour aller de l'autre cote si l'on depasse la matrice
        j = (y+1)%self.sol.matrice_hauteur

        if self.sol.terrain[j][x] != "colline":
            nom_tuile += "-SO"
        if self.sol.terrain[y][i] != "colline":
            nom_tuile += "-SE"
        if self.sol.terrain[y-1][x] != "colline":
                nom_tuile += "-NE"
        if self.sol.terrain[y][x-1] != "colline":
            nom_tuile += "-NO"
 
        if len(nom_tuile)>13:
            nom_tuile = "colline"
        if nom_tuile == "colline":
            if self.sol.terrain[j][i] != "colline":
                nom_tuile += "-S"
            elif self.sol.terrain[y-1][i] != "colline":
                nom_tuile += "-E"
            elif self.sol.terrain[y-1][x-1] != "colline":
                nom_tuile += "-N"
            elif self.sol.terrain[j][x-1] != "colline":
                nom_tuile += "-O"

        return nom_tuile

    def selectionner_tuile_eau(self, x, y):
        nom_tuile = "eau"
        i = (x+1)%self.sol.matrice_largeur #pour aller de l'autre cote si l'on depasse la matrice
        j = (y+1)%self.sol.matrice_hauteur
        if self.sol.terrain[j][x] != "eau":
            nom_tuile += "-SO"
        if self.sol.terrain[y][i] != "eau":
            nom_tuile += "-SE"
        if self.sol.terrain[y-1][x] != "eau":
                nom_tuile += "-NE"
        if self.sol.terrain[y][x-1] != "eau":
            nom_tuile += "-NO"
               
        if len(nom_tuile) == 3:
            if self.sol.terrain[j][i] != "eau":
                nom_tuile += "-S"
            elif self.sol.terrain[y-1][i] != "eau":
                nom_tuile += "-E"
            elif self.sol.terrain[y-1][x-1] != "eau":
                nom_tuile += "-N"
            elif self.sol.terrain[j][x-1] != "eau":
                nom_tuile += "-O"
        
        if nom_tuile == "eau":
            nom_tuile += str(random.choice([1, 1, 1, 2, 2, 2, 3, 4])) #les tuiles n'ont pas le meme nombre de chances d'etre obtenue
        return nom_tuile[:9] #Les tuiles d'eau a trois bords ne sont pas disponibles
