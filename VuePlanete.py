# continuer les infrastructures

from PIL import *
from Perspective import *
import random
from helper import Helper as hlp
import tkinter
from Infrastructure import *
import Unite

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
        self.cadrecaserne=Frame(self,width=400,height=400, bg="lightgreen")
        
        """
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        self.canevas.config(bg="sandy brown")
        
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Mine",command=self.creermine)
        self.btncreervaisseau.pack()
        
        self.btncreerstation=Button(self.cadreetataction,text="Creer Manufacture",command=self.creermanufacture)
        self.btncreerstation.pack()
        """
        self.btnmenuavancer= Button(self.cadreUni,text="Menu Universite", command= self.creermenuavancer)
        self.btnmenuavancer.pack()
        
        self.btncreerDis= Button(self.cadreCaserne,text="Creer Disciple", command= lambda: self.action_joueur("creerunite", {"type_unite": "disciple"}))
        self.btncreerDis.pack()
        
        self.btnRetour= Button(self.cadreCaserne,text="Retour", command=lambda: self.changecadreetat(self.cadreetataction))
        self.btnRetour.pack()

        self.population=Label(self.cadreetataction, text="CONSTRUIRE DES INFRASTRUCTURES", bg="#8afc92")
        self.population.pack(side=TOP,fill=X)
        
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir Systeme",command=self.voirsysteme)
        self.btnvuesysteme.pack(side=BOTTOM, fill=X)
        
        self.btncreermine=Button(self.cadreetataction,text="Mine",command=self.creermine)
        self.btncreermine.pack(side=BOTTOM, fill=X)        
                
        self.btncreermine.bind("<Enter>", self.on_enter)
        self.btncreermine.bind("<Leave>", self.on_leave)

        self.btncreerferme=Button(self.cadreetataction,text="Ferme",command=self.creerferme)
        self.btncreerferme.pack(side=BOTTOM, fill=X)
        
        self.btncreerferme.bind("<Enter>", self.on_enter)
        self.btncreerferme.bind("<Leave>", self.on_leave)
        
        self.btnhotelville=Button(self.cadreetataction,text="Hotel de ville", command=self.creerhotelville)
        self.btnhotelville.pack(side=BOTTOM, fill=X)
        
        self.btnhotelville.bind("<Enter>", self.on_enter)
        self.btnhotelville.bind("<Leave>", self.on_leave)
                                
        self.btntourdefense=Button(self.cadreetataction,text="Tour de defense",command=self.creertourdefense)
        self.btntourdefense.pack(side=BOTTOM, fill=X)
        
        self.btntourdefense.bind("<Enter>", self.on_enter)
        self.btntourdefense.bind("<Leave>", self.on_leave)
        
        self.btnusine=Button(self.cadreetataction,text="Usine",command=self.creerusine)
        self.btnusine.pack(side=BOTTOM, fill=X)
        
        self.btnusine.bind("<Enter>", self.on_enter)
        self.btnusine.bind("<Leave>", self.on_leave)
        
        self.btnuniversite=Button(self.cadreetataction,text="Universite",command=self.creeruniversite)
        self.btnuniversite.pack(side=BOTTOM, fill=X)
        
        self.btnuniversite.bind("<Enter>", self.on_enter)
        self.btnuniversite.bind("<Leave>", self.on_leave)
        
        self.btncaserne=Button(self.cadreetataction,text="Caserne",command=self.creercaserne)
        self.btncaserne.pack(side=BOTTOM, fill=X)
        
        self.btncaserne.bind("<Enter>", self.on_enter)
        self.btncaserne.bind("<Leave>", self.on_leave)
        
        self.btnscierie=Button(self.cadreetataction,text="Scierie",command=self.creerscierie)
        self.btnscierie.pack(side=BOTTOM, fill=X)
        
        self.btnscierie.bind("<Enter>", self.on_enter)
        self.btnscierie.bind("<Leave>", self.on_leave)
        
        self.btntemple=Button(self.cadreetataction,text="Temple",command=self.creertemple)
        self.btntemple.pack(side=BOTTOM, fill=X)
        
        self.btntemple.bind("<Enter>", self.on_enter)
        self.btntemple.bind("<Leave>", self.on_leave)
        
        #self.btnruine=Button(self.cadreetataction,text=" Ruine",command=self.creerruine)
        #self.btnruine.pack(side=BOTTOM, fill=X)

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

        self.labelBoistxt = Label(self.cadreinfo, text = "Exploite " + str(systeme.nbbois) + " |  Utilisable " + str(planete.nbbois))
        self.labelFointxt = Label(self.cadreinfo, text = "Exploite " + str(systeme.nbfoin) + " |  Utilisable " + str(planete.nbfoin))
        self.labelArgenttxt = Label(self.cadreinfo, text ="Exploite " + str(systeme.nbargent) + " |  Utilisable " + str(planete.nbargent))
        self.labelMineraitxt = Label(self.cadreinfo, text = "Exploite " + str(systeme.nbminerai) + " | Utilisable " + str(planete.nbminerai))

        self.labelBois.pack(fill=X)
        self.labelBoistxt.pack(fill=X)
        self.labelFoin.pack(fill=X)
        self.labelFointxt.pack(fill=X)
        self.labelArgent.pack(fill=X)
        self.labelArgenttxt.pack(fill=X)    
        self.labelMinerai.pack(fill=X)
        self.labelMineraitxt.pack(fill=X)
        
        self.labelBois.image = imgBois
        self.labelFoin.image = imgFoin
        self.labelArgent.image = imgArgent
        self.labelMinerai.image = imgMinerai

        self.changecadreetat(self.cadreetataction)
        
    def afficherMenu(self, infrastructure):
        if infrastructure == 'caserne':
            self.changecadreetat(self.cadreCaserne)   
        elif infrastructure == 'universite':
             self.changecadreetat(self.cadreUni)
                   
    def detruire(self):
        self.fenetre.destroy()
        self.changecadreetat(self.cadreetataction)    
                
    def changeronglet(self,FrameActuel,NextFrame):
        if(NextFrame==self.FrameDiplo):
            self.refrechalliance()
        FrameActuel.pack_forget()
        NextFrame.pack(side=BOTTOM)   
        self.current = NextFrame 
        
    def refrechalliance(self):
        self.CanevasDiplo.create_text(100,100,text=self.modele.getalliance())
        
    def changerTech(self,FrameActuel,NextFrame):
        FrameActuel.pack_forget()
        NextFrame.pack(side=BOTTOM)
        self.tech = NextFrame  
            
    def creermenuavancer(self):
        self.largeur=600
        self.hauteur=600
        self.current=None
        self.tech=None
        
        self.fenetre=Toplevel(height=self.hauteur, width=self.largeur, bg="black") #contenant
        
        
        
        self.topframe=Frame(self.fenetre,width=self.largeur,height=200,bg="grey")
        self.topframe.pack() 
        
        self.FrameDef=Frame(self.fenetre,width=self.largeur,height=400)
        self.FrameDef.pack(side=BOTTOM)
        self.current = self.FrameDef
        
        self.FrameTech = Frame(self.fenetre,height=self.hauteur,width=self.largeur,bg="blue") #contenant
        self.toptech=Frame(self.FrameTech,width=self.largeur,height=200,bg="grey")
        self.toptech.pack()
        
        
        self.FrameTechMilit=Frame(self.FrameTech,width=self.largeur,height=400,bg="black")
        
        self.ButtonM1=Button(self.FrameTechMilit,image=self.parent.images["epee"],state=DISABLED)
        self.ButtonM1.pack()
        
        self.ButtonM2=Button(self.FrameTechMilit,image=self.parent.images["char"],state=DISABLED)
        self.ButtonM2.pack()
        
        self.ButtonM3=Button(self.FrameTechMilit,image=self.parent.images["missile"],state=DISABLED)
        self.ButtonM3.pack()
        
        self.FrameTechMilit.pack()
        self.tech = self.FrameTechMilit
        
        self.FrameTechRess=Frame(self.FrameTech,width=self.largeur,height=400,bg="black")
        
        self.ButtonR1=Button(self.FrameTechRess,image=self.parent.images["mine1"],state=DISABLED)
        self.ButtonR1.pack()
        
        self.FrameTechRess.pack()
        self.tech = self.FrameTechRess
 
        self.FrameTechAgr=Frame(self.FrameTech,width=self.largeur,height=400,bg="black")
        
        self.ButtonA1=Button(self.FrameTechAgr,image=self.parent.images["cart"],state=DISABLED)
        self.ButtonA1.pack()
        
        self.ButtonA2=Button(self.FrameTechAgr,image=self.parent.images["puit"],state=DISABLED)
        self.ButtonA2.pack()
        
        self.ButtonA3=Button(self.FrameTechAgr,image=self.parent.images["moulin"],state=DISABLED)
        self.ButtonA3.pack()
        
        self.ButtonA4=Button(self.FrameTechAgr,image=self.parent.images["tracteur"],state=DISABLED)
        self.ButtonA4.pack()
        
        self.ButtonA5=Button(self.FrameTechAgr,image=self.parent.images["batteuse"],state=DISABLED)
        self.ButtonA5.pack()
        
        self.FrameTechAgr.pack()
        self.tech = self.FrameTechAgr
        
        self.FrameArt=Frame(self.fenetre,width=self.largeur,height=400,bg="brown")
        self.FrameA=Frame(self.FrameArt,width=self.largeur,height=400,bg="black")
        #A REVOIR
        self.ButtonArt=Button(self.FrameA,image=self.parent.images["batteuse"],state=DISABLED)
        self.ButtonArt.pack()
        
        self.FrameDiplo=Frame(self.fenetre,width=self.largeur,height=400,bg="red")
        self.CanevasDiplo=Canvas(self.FrameDiplo,width=self.largeur,height=400,bg="white")
        self.CanevasDiplo.pack()
        
        self.FrameText=Frame(self.FrameDef,width=self.largeur,height=200,bg="white")
        self.FrameText.pack();
        
        self.CanevasText=Canvas(self.FrameText,width=self.largeur,height=200,bg="white")
        self.CanevasText.pack();
        
        self.CanevasText.create_text(300,100,text="Bienvenue, dans le menu avance d'ORION."+'\n' +" Vous pouvez cliquez sur les trois bouton ci-dessus pour connaitre les options avance du jeu. "+'\n' +" Le boutons TECHONOLOGIE vous permet d'acceder aux nouvelles technologies "+'\n' +"debloquer et bloquer par votre universite.Le boutons ARTEFACTS vous permet de voir les nouvelles "+'\n' +"fonctionnalites, tels que de nouveau batiments,"+'\n' +" nouvelles unites ou meme des TECHNOLOGIES EXTRATERRESTRES. "+'\n' +"Le bouton Diplomatie affiche l'arbre des alliances entre tous les joueurs du jeu. "+'\n' +"Vous pouvez ainsi mieux planifier votre prochain attaque. "+'\n' +"Choissisez judicieusement ")
        
        
        self.FrameImage=Frame(self.FrameDef, width=self.largeur,height=200,bg="white")
        self.FrameImage.pack(side=RIGHT);
        
        self.CanevasImage=Canvas(self.FrameImage, width=self.largeur,height=200,bg="white")
        self.CanevasImage.pack();
        
        self.CanevasImage.create_image(300,100, image = self.parent.images["fermier"]) 
        
        self.buttontech=Button(self.topframe, text="Technologies", fg="blue" , command=lambda: self.changeronglet(self.current, self.FrameTech ))
        self.buttontech.pack(side=LEFT)
        
        self.buttonartefact= Button(self.topframe, text="Artefact", fg="brown", command=lambda: self.changeronglet(self.current, self.FrameArt))
        self.buttonartefact.pack(side=LEFT)
        
        self.buttondiplo=Button(self.topframe, text="Diplomatie", fg="red", command=lambda: self.changeronglet(self.current, self.FrameDiplo))
        self.buttondiplo.pack(side=LEFT)
        
        self.buttonDef=Button(self.topframe, text="Retour", fg="pink", command=lambda: self.changeronglet(self.current, self.FrameDef))
        self.buttonDef.pack(side=LEFT)
        
        self.buttonMilit=Button(self.toptech,text="Militaire",fg="blue" , command=lambda: self.changerTech(self.tech, self.FrameTechMilit))
        self.buttonMilit.pack(side=LEFT)
        
        self.buttonRess=Button(self.toptech,text="Ressources",fg="blue",command=lambda: self.changerTech(self.tech, self.FrameTechRess))
        self.buttonRess.pack(side=LEFT)
        
        self.buttonAgr=Button(self.toptech,text="Agriculture",fg="blue",command=lambda: self.changerTech(self.tech, self.FrameTechAgr))
        self.buttonAgr.pack(side=LEFT)
        
        self.fenetre.protocol("WM_DELETE_WINDOW", self.detruire)
    
    def on_enter(self, event):
        texteoriginal = event.widget.cget("text")
        self.prix={   "Mine":           "250 Bois, 100 $",
                      "Tour de defense":"250 Minerai, 200 Foin, 100 $",
                      "Usine":          "250 Minerai, 50 Foin",
                      "Universite":     "250 Minerai, 50 Foin, 50 $",
                      "Caserne":        "250 Minerai, 50 Foin, 50 Bois, 200$",
                      "Scierie":        "50 Minerai, 50 Foin, 200 Bois",
                      "Temple":         "500 Minerai, 500 Foin, 500 $",
                      "Ferme":          "500 Minerai, 500 Foin, 100 $",
                      "Hotel de ville": "250 Minerai, 250 Foin, 250 $"
                     }
        event.widget.configure(text=self.prix[texteoriginal])

    def on_leave(self, enter):
        texteprix = enter.widget.cget("text")
        self.nom={    "250 Bois, 100 $":                    "Mine",
                      "250 Minerai, 200 Foin, 100 $":       "Tour de defense",
                      "250 Minerai, 50 Foin":               "Usine",
                      "250 Minerai, 50 Foin, 50 $":          "Universite",
                      "250 Minerai, 50 Foin, 50 Bois, 200$": "Caserne",
                      "50 Minerai, 50 Foin, 200 Bois":      "Scierie",
                      "500 Minerai, 500 Foin, 500 $":  "Temple",
                      "500 Minerai, 500 Foin, 100 $":   "Ferme",
                      "250 Minerai, 250 Foin, 250 $":  "Hotel de ville"
                     }
        enter.widget.configure(text=self.nom[texteprix])
    
    def creermine(self):
        self.action_attente = "mine"
        self.parent.root.config(cursor='cross red red')
        self.macommande="mine"
    
    def creerferme(self):
        print(self.parent)
        self.action_attente = "ferme"
        self.parent.root.config(cursor='cross red red')
        self.macommande="ferme"
        
    def creerhotelville(self):
        self.action_attente = "hotelville"
        self.parent.root.config(cursor='cross red red')
        self.macommande="hotelville"
        
    def creertourdefense(self):
        self.action_attente = "tourdefense"
        self.parent.root.config(cursor='cross red red')
        self.macommande="tourdefense"
        
    def creerusine(self):
        self.action_attente = "usine"
        self.parent.root.config(cursor='cross red red')
        self.macommande="usine"
        
    def creeruniversite(self):
        self.action_attente = "universite"
        self.parent.root.config(cursor='cross red red')
        self.macommande="universite"
        
    def creercaserne(self):
        self.action_attente = "caserne"
        self.parent.root.config(cursor='cross red red')
        self.macommande="caserne"
        
    def creerscierie(self):
        self.action_attente = "scierie"
        self.parent.root.config(cursor='cross red red')
        self.macommande="scierie"
        
    def creertemple(self):
        self.action_attente = "temple"
        self.parent.root.config(cursor='cross red red')
        self.macommande="temple"
        
    def creerruine(self):
        self.action_attente = "ruine"
        self.parent.root.config(cursor='cross red red')
        self.macommande="ruine"
    
    def creermanufacture(self):
        pass
    
    def creerDisciple(self):
        pass
    
    def voirsysteme(self):
        self.action_attente = None
        self.parent.root.config(cursor='')
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
        self.afficher_infrastructures()
        self.actualiser_ressources()
        
    def actualiser_ressources(self):
        self.labelFointxt.config(text= "Exploite " + str(self.planete.foinexploite) + " |  Utilisable " + str(self.planete.nbfoin))
        self.labelBoistxt.config(text= "Exploite " + str(self.planete.boisexploite) + " |  Utilisable " + str(self.planete.nbbois))
        self.labelMineraitxt.config(text= "Exploite " + str(self.planete.mineraiexploite) + " |  Utilisable " + str(self.planete.nbminerai))
        self.labelArgenttxt.config(text= "Exploite " + str(self.planete.argentexploite) + " |  Utilisable " + str(self.planete.nbargent))

            
    def changerproprietaire(self,prop,couleur,systeme): 
        pass
               
    def afficherselection(self):
        pass
    
    def exploitation(self):
        for i in self.infrastructures:
            if(isinstance(objet, Ferme)):
               i.exploitationnouriture()
               self.labelFointxt.config(text= "Exploite " + str(systeme.nbfoin) + " |  Utilisable " + str(planete.nbfoin))

    def selectionner(self,evt):
        self.canevas.delete("messagetemporaire")
        x, y=self.sol.iso_vers_matrice(evt)
        print("action_attente: ", str(self.action_attente))
        t=self.canevas.gettags("current")
        print("t: ", t)
        if(t):          #fp 2 mai  if (t) parce que si on clique dans l'espace, on veut que rien se passe (versus toute plante)
            #print("t[0]: ", t[0])
            #print(self.sol.terrain[y][x])
            #print("t typeof: ", type(t))
            if not self.action_attente:
                print("pas attente")
                if t and t[0]!="current":   #fp 2 mai Est-ce que tout Ã§a pourrait sauter par hasard??
                    self.afficherMenu(t[0])
                    self.maselection=[self.parent.nom,t[1],t[2]]
                else:
                    if self.macommande:
                        x=self.canevas.canvasx(evt.x)
                        y=self.canevas.canvasy(evt.y)
                        self.parent.parent.creermine(self.parent.nom,self.systemeid,self.planeteid,x,y)
                        self.macommande=None
                   
            else:# fp 2 mai.  pour empecher qu'on construise dans l'eau
                if(self.sol.terrain[y][x] == "terre"):# or self.sol.terrain[y][x] == "colline" or t[0] == 'terre1' or t[0] == 'terre2' or t[0] == 'terre3' or t[0] == 'colline'):
                    if(t[1] == 'infrastructure'):
                        self.canevas.create_text(10, 500, text=str("On ne peut pas construire si pres d'un autre batiment."),font=("calibri", 36), fill="#ff0022", anchor="nw", tag="messagetemporaire")
                    else:
                        self.action_joueur("creerinfrastructure", {"id_planete": self.planete.id, "type_unite":self.action_attente, "x":evt.x, "y":evt.y})
                        self.action_attente = None
                else:
                    #print("on ne peut pas construire ici!")
                    self.canevas.create_text(10, 500, text=str("On ne peut pas construire si pres de l'eau."),font=("calibri", 36), fill="#ff0022", anchor="nw", tag="messagetemporaire")
                

                            
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
        self.canevas.delete("infrastructure")
        self.canevas.delete("unite")
        for objet in self.parent.parent.modele.objets_cliquables.values():
            
            if(isinstance(objet, Infrastructure) and objet.lieu == self.planete):
                if(isinstance(objet, Mine)):
                    image = self.parent.images["mine"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("mine","infrastructure", objet.id))
                elif(isinstance(objet, Ferme)):
                    image = self.parent.images["ferme"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("ferme","infrastructure", objet.id))

                    
                elif(isinstance(objet, Tourdefense)):
                    image = self.parent.images["tourdefense"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("tourdefense","infrastructure", objet.id))
                elif(isinstance(objet, Temple)):
                    image = self.parent.images["temple"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("temple","infrastructure", objet.id))
                elif(isinstance(objet, HotelVille)):
                    image = self.parent.images["hotelville"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("hotelville","infrastructure", objet.id))

                elif(isinstance(objet, Ruine)):
                    image = self.parent.images["ruine"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("ruine","infrastructure", objet.id))
    
                elif(isinstance(objet, Universite)):
                    image = self.parent.images["universite"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("universite","infrastructure", objet.id))
    
                elif(isinstance(objet, Usine)):
                    image = self.parent.images["usine"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("usine","infrastructure", objet.id))

                elif(isinstance(objet, Scierie)):
                    image = self.parent.images["scierie"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("scierie","infrastructure", objet.id))
                    
                elif(isinstance(objet, Caserne)):
                    image = self.parent.images["caserne"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("caserne","infrastructure", objet.id))                    
                elif(isinstance(objet, Universite)):
                    image = self.parent.images["universite"]
                    self.canevas.create_image(objet.x, objet.y,
                                            image = image, tags=("universite","infrastructure", objet.id))
            elif(isinstance(objet, Unite.Disciple) and objet.lieu == self.planete):
                print("une unite veut se faire afficher")
                type = objet.type
                image = self.parent.images[type]
                self.canevas.create_image(objet.x, objet.y,
                                    image = image, tags=(type,"unite", objet.id))
    
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
