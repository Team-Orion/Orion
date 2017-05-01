from PIL import *
from Perspective import *
import random
from helper import Helper as hlp

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
        
        """
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        self.canevas.config(bg="sandy brown")
        
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Mine",command=self.creermine)
        self.btncreervaisseau.pack()
        
        self.btncreerstation=Button(self.cadreetataction,text="Creer Manufacture",command=self.creermanufacture)
        self.btncreerstation.pack()
        """
        self.action_attente=None
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir Systeme",command=self.voirsysteme)
        self.btnvuesysteme.pack(side=BOTTOM)
       
        self.btncreermine=Button(self.cadreetataction,text="Construire Mine",command=lambda: self.action_joueur("creerinfrastructure", {"type_unite": "mine"}))
        self.btncreermine.pack(side=BOTTOM)

        self.btncreerferme=Button(self.cadreetataction,text="Construire Ferme",command=lambda:self.action_joueur("creerinfrastructure", {"type_unite": "ferme"}))
        self.btncreerferme.pack(side=BOTTOM)
        
        self.btnhotelville=Button(self.cadreetataction,text="Construire Hotel ville",command=lambda:self.action_joueur("creerinfrastructure", {"type_unite": "hotelville"}))
        self.btnhotelville.pack()
        
        self.btntourdefense=Button(self.cadreetataction,text="Construire Tour",command=lambda:self.action_joueur("creerinfrastructure", {"type_unite": "tourdefense"}))
        self.btntourdefense.pack(side=BOTTOM)
        
        self.btnusinevaisseau=Button(self.cadreetataction,text="Construire Usine vaisseau",command=lambda:self.action_joueur("creerinfrastructure", {"type_unite": "usinevaisseau"}))
        self.btnusinevaisseau.pack(side=BOTTOM)
        
        self.btnuniversite=Button(self.cadreetataction,text="Construire Universite",command=lambda:self.action_joueur("creerinfrastructure", {"type_unite": "universite"}))
        self.btnuniversite.pack(side=BOTTOM)
        
        self.btncaserne=Button(self.cadreetataction,text="Construire Caserne",command=lambda:self.action_joueur("creerinfrastructure", {"type_unite": "caserne"}))
        self.btncaserne.pack(side=BOTTOM)
        
        self.btnscierie=Button(self.cadreetataction,text="Construire Scierie",command=lambda:self.action_joueur("creerinfrastructure", {"type_unite": "scierie"}))
        self.btnscierie.pack(side=BOTTOM)
        
        self.btntemple=Button(self.cadreetataction,text="Construire Temple",command=lambda:self.action_joueur("creerinfrastructure", {"type_unite": "temple"}))
        self.btntemple.pack(side=BOTTOM)
        
        self.btnruine=Button(self.cadreetataction,text="Construire Ruine",command=lambda:self.action_joueur("creerinfrastructure", {"type_unite": "ruine"}))
        self.btnruine.pack(side=BOTTOM)
        
        
        self.changecadreetat(self.cadreetataction)
    
    def creermine(self):
        print("creer mine")
        self.macommande="mine"
    
    def creerferme(self):
        print("creer ferme")
        pass
    
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
        
        x, y=self.sol.iso_vers_matrice(evt)
        print(self.sol.terrain[y][x])
        print("action_attente: ", str(self.action_attente))
        if not self.action_attente:
            t=self.canevas.gettags("current")
            print("t: ", t)
            if t and t[0]!="current":
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
        else:
            #self.action_attente["parametres"]["coords"] = evt 
            #print("action attente: ", self.action_attente["parametres"]["coords"])  
            self.action_joueur("creerinfrastructure", {"id_planete": self.planete.id, "type_unite":self.action_attente, "x":evt.x, "y":evt.y})
            self.action_attente = None
            
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
        self.afficher_base()
        self.afficher_sol()
    
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

    def afficher_infrastructure(self, x, y, type_infrastructure):
        image = self.parent.images[type_infrastructure]
        self.canevas.create_image(x, y,
                                      image = image, tags=(type_infrastructure))
        
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
