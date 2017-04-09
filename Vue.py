from tkinter import *
from PIL import Image,ImageDraw, ImageTk
import os,os.path
import sys
import random
from helper import Helper as hlp
from Perspective import *
import math
from VueGalaxie import *
from VueSysteme import *
from VuePlanete import *


class Vue():
    def __init__(self,parent,ip,nom,largeur=800,hauteur=600):
        self.root=Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        self.nom=None
        self.largeur=largeur
        self.hauteur=hauteur
        self.images={}
        self.modes={}
        self.modecourant=None
        self.cadreactif=None
        self.creercadres(ip,nom)
        self.changecadre(self.cadresplash)
        
        
            #variable pour le message 
        self.cadremessage=None
        self.canevasmessage=None
        self.messagerecu=None
        self.entreemessage = None
        self.messageenvoi=None  
        self.labelrecu=None 
        self.buttonmessage=None
        self.creercadremessage()
        self.tabmessage=[]
        self.listejoueur=None
        
    def setmessagerecu(self, messsage,nom): 
        self.messagerecu=nom+': '+messsage+"\n"
        if len(self.tabmessage)==6:
            self.tabmessage=[]
        self.tabmessage.append(self.messagerecu)
        if self.labelrecu:
            self.labelrecu.pack_forget()
        self.labelrecu=Label(self.canevasmessage, text=self.tabmessage,bg="azure")
        self.labelrecu.pack(side=BOTTOM)  
        print("message final recu:", self.messagerecu)
        
    def creercadremessage(self): 
        self.cadremessage=Frame(self.root,width=self.largeur)
        self.canevasmessage=Canvas(self.cadrejeu,width=self.largeur,height=self.cadremessage.winfo_height(),bg="azure")
        self.entreemessage = Entry(self.canevasmessage)  
        self.labelrecu=None
        self.buttonmessage=Button(self.canevasmessage,text="Envoyer", command=lambda: self.action_joueur("envoimessage", {"message": self.entreemessage.get(),"nom":self.parent.monnom}))
        self.canevasmessage.pack() 
        self.entreemessage.pack(side=TOP) 
        self.buttonmessage.pack(side=TOP)

    def changemode(self,cadre):
        if self.modecourant:
            self.modecourant.pack_forget()
        self.modecourant=cadre
        self.modecourant.pack(expand=1,fill=BOTH)  
        self.canevasmessage.pack_forget()
        self.canevasmessage.pack()           

    def changecadre(self,cadre,etend=0):
        if self.cadreactif:
            self.cadreactif.pack_forget()
        self.cadreactif=cadre
        if etend:
            self.cadreactif.pack(expand=1,fill=BOTH)
        else:
            self.cadreactif.pack()
    
    def creercadres(self,ip,nom):
        self.creercadresplash(ip, nom)
        self.creercadrelobby()
        self.cadrejeu=Frame(self.root,bg="azure")
        self.modecourant=None
                
    def creercadresplash(self,ip,nom):
        self.cadresplash=Frame(self.root)
        self.canevasplash=Canvas(self.cadresplash,width=640,height=480,bg="red")
        self.canevasplash.pack()
        self.nomsplash=Entry(bg="pink")
        self.nomsplash.insert(0, nom)
        self.ipsplash=Entry(bg="pink")
        self.ipsplash.insert(0, ip)
        labip=Label(text=ip,bg="red",borderwidth=0,relief=RIDGE)
        btncreerpartie=Button(text="Creer partie",bg="pink",command=self.creerpartie)
        btnconnecterpartie=Button(text="Connecter partie",bg="pink",command=self.connecterpartie)
        self.canevasplash.create_window(200,200,window=self.nomsplash,width=100,height=30)
        self.canevasplash.create_window(200,250,window=self.ipsplash,width=100,height=30)
        self.canevasplash.create_window(200,300,window=labip,width=100,height=30)
        self.canevasplash.create_window(200,350,window=btncreerpartie,width=100,height=30)
        self.canevasplash.create_window(200,400,window=btnconnecterpartie,width=100,height=30) 
        
    def creercadrelobby(self):
        self.cadrelobby=Frame(self.root)
        self.canevaslobby=Canvas(self.cadrelobby,width=640,height=480,bg="lightblue")
        self.canevaslobby.pack()
        self.listelobby=Listbox(bg="red",borderwidth=0,relief=FLAT)
        self.diametre=Entry(bg="pink")
        self.diametre.insert(0, 50)
        self.densitestellaire=Entry(bg="pink")
        self.densitestellaire.insert(0, 2)
        self.qteIA=Entry(bg="pink")
        self.qteIA.insert(0, 4)
        self.btnlancerpartie=Button(text="Lancer partie",bg="pink",command=self.lancerpartie,state=DISABLED)
        self.canevaslobby.create_window(520,240,window=self.listelobby,width=200,height=400)
        self.canevaslobby.create_window(300,200,window=self.diametre,width=100,height=30)
        self.canevaslobby.create_text(150,200,text="Diametre en annee lumiere")
        
        self.canevaslobby.create_window(300,250,window=self.densitestellaire,width=100,height=30)
        self.canevaslobby.create_text(150,250,text="Nb systeme/AL cube")
        
        self.canevaslobby.create_window(300,300,window=self.qteIA,width=100,height=30)
        self.canevaslobby.create_text(150,300,text="Nb d'IA")
        
        self.canevaslobby.create_window(200,450,window=self.btnlancerpartie,width=100,height=30)

    def voirgalaxie(self):
        # A FAIRE comme pour voirsysteme et voirplanete, tester si on a deja la vuegalaxie
        #         sinon si on la cree en centrant la vue sur le systeme d'ou on vient
        s=self.modes["galaxie"]
        self.changemode(s) 
       
    def voirsysteme(self,systeme=None):
        if systeme:
            sid=systeme.id
            if sid in self.modes["systemes"].keys():
                s=self.modes["systemes"][sid]
            else:
                s=VueSysteme(self)
                self.modes["systemes"][sid]=s
                s.initsysteme(systeme)
            self.changemode(s)
        
    def voirplanete(self,maselection=None):
        s=self.modes["planetes"]
        
        if maselection:
            sysid=maselection[5]
            planeid=maselection[2]
            if planeid in self.modes["planetes"].keys():
                s=self.modes["planetes"][planeid]
            else:
                s=VuePlanete(self,sysid,planeid)
                self.modes["planetes"][planeid]=s
                s.initplanete(sysid,planeid)
            self.changemode(s)
        else:
            print("aucune planete selectionnee pour atterrissage")
        
    def creerpartie(self):
        nom=self.nomsplash.get()
        ip=self.ipsplash.get()
        if nom and ip:
            self.parent.creerpartie()
            self.btnlancerpartie.config(state=NORMAL)
            self.connecterpartie()
          
    def connecterpartie(self):
        nom=self.nomsplash.get()
        ip=self.ipsplash.get()
        if nom and ip:
            self.parent.inscrirejoueur()
            self.changecadre(self.cadrelobby)
            self.parent.boucleattente()
            
    def lancerpartie(self):
        global modeauto
        diametre=self.diametre.get()
        densitestellaire=self.densitestellaire.get()
        qteIA=self.qteIA.get()  # IA
        if diametre :
            diametre=int(diametre)
        else:
            largeurjeu=None
        if densitestellaire :
            densitestellaire=int(densitestellaire)
        else:
            densitestellaire=None
        self.parent.lancerpartie(diametre,densitestellaire,qteIA)  #IA
        
    def affichelisteparticipants(self,lj):
        self.listelobby.delete(0,END)
        for i in lj:
            self.listelobby.insert(END,i)

    def afficherinitpartie(self,mod):
        self.nom=self.parent.monnom
        self.modele=mod
        
        self.modes["galaxie"]=VueGalaxie(self)
        self.modes["systemes"]={}
        self.modes["planetes"]={}
        
        g=self.modes["galaxie"]
        g.labid.config(text=self.nom)
        g.labid.config(fg=mod.joueurs[self.nom].couleur)
        
        g.chargeimages()
        g.afficherdecor() #pourrait etre remplace par une image fait avec PIL -> moins d'objets
        self.changecadre(self.cadrejeu,1)
        self.changemode(self.modes["galaxie"])
        
    def affichermine(self,joueur,systemeid,planeteid,x,y):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images["mine"]
                self.modes["planetes"][i].canevas.create_image(x,y,image=im)
                
    def fermerfenetre(self):
        # Ici, on pourrait mettre des actions a faire avant de fermer (sauvegarder, avertir etc)
        self.parent.fermefenetre()
        
    def action_joueur(self, action, parametres = {}):
            
            self.parent.action_joueur(action, parametres)
        
