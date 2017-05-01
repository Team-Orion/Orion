from tkinter import *
from PIL import Image,ImageDraw, ImageTk
import collections
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
    InfosImg = collections.namedtuple("InfosImg", "nom source")
    liste_images = [InfosImg("terre1", "images/tuiles/terre1.png"),
                InfosImg("terre2", "images/tuiles/terre2.png"),
                InfosImg("terre3", "images/tuiles/terre3.png"),
                InfosImg("eau1", "images/tuiles/eau1.png"),
                InfosImg("eau2", "images/tuiles/eau2.png"),
                InfosImg("eau3", "images/tuiles/eau3.png"),
                InfosImg("eau4", "images/tuiles/eau4.png"),
                InfosImg("eau-NE", "images/tuiles/eau-NE.png"),
                InfosImg("eau-SE", "images/tuiles/eau-SE.png"),
                InfosImg("eau-SE-NE", "images/tuiles/eau-SE-NE.png"),
                InfosImg("eau-SO", "images/tuiles/eau-SO.png"),
                InfosImg("eau-SO-NE", "images/tuiles/eau-SO-NE.png"),
                InfosImg("eau-SO-SE", "images/tuiles/eau-SO-SE.png"),
                InfosImg("eau-NO", "images/tuiles/eau-NO.png"),
                InfosImg("eau-NE-NO", "images/tuiles/eau-NE-NO.png"),
                InfosImg("eau-SO-NO", "images/tuiles/eau-SO-NO.png"),
                InfosImg("eau-SE-NO", "images/tuiles/eau-SE-NO.png"),
                InfosImg("eau-N", "images/tuiles/eau-N.png"),
                InfosImg("eau-E", "images/tuiles/eau-E.png"),
                InfosImg("eau-S", "images/tuiles/eau-S.png"),
                InfosImg("eau-O", "images/tuiles/eau-O.png"),
                InfosImg("colline", "images/tuiles/colline.png"),
                InfosImg("colline-SO", "images/tuiles/colline-SO.png"),
                InfosImg("colline-SE", "images/tuiles/colline-SE.png"),
                InfosImg("colline-NE", "images/tuiles/colline-NE.png"),
                InfosImg("colline-NO", "images/tuiles/colline-NO.png"),
                InfosImg("colline-SO-SE", "images/tuiles/colline-SO-SE.png"),
                InfosImg("colline-SO-NO", "images/tuiles/colline-SO-NO.png"),
                InfosImg("colline-SE-NE", "images/tuiles/colline-SE-NE.png"),
                InfosImg("colline-NE-NO", "images/tuiles/colline-NE-NO.png"),
                InfosImg("colline-N", "images/tuiles/colline-N.png"),
                InfosImg("colline-O", "images/tuiles/colline-O.png"),
                InfosImg("colline-S", "images/tuiles/colline-S.png"),
                InfosImg("colline-E", "images/tuiles/colline-E.png"),
                InfosImg("tortue", "images/unites/tortue_1.png"),
                InfosImg("bois", "images/ressources/bois.png"),
                InfosImg("foin", "images/ressources/foin.png"),
                InfosImg("argent", "images/ressources/argent.png"),
                InfosImg("minerai", "images/ressources/minerai.png"),
                InfosImg("0vaisseauattaque1", "images/unites/0attaque_1.png"),
                InfosImg("45vaisseauattaque1", "images/unites/45attaque_1.png"),
                InfosImg("90vaisseauattaque1", "images/unites/90attaque_1.png"),
                InfosImg("135vaisseauattaque1", "images/unites/135attaque_1.png"),
                InfosImg("180vaisseauattaque1", "images/unites/180attaque_1.png"),
                InfosImg("225vaisseauattaque1", "images/unites/225attaque_1.png"),
                InfosImg("270vaisseauattaque1", "images/unites/270attaque_1.png"),
                InfosImg("315vaisseauattaque1", "images/unites/315attaque_1.png"),
                InfosImg("0vaisseauattaque2", "images/unites/0attaque_2.png"),
                InfosImg("45vaisseauattaque2", "images/unites/45attaque_2.png"),
                InfosImg("90vaisseauattaque2", "images/unites/90attaque_2.png"),
                InfosImg("135vaisseauattaque2", "images/unites/135attaque_2.png"),
                InfosImg("180vaisseauattaque2", "images/unites/180attaque_2.png"),
                InfosImg("225vaisseauattaque2", "images/unites/225attaque_2.png"),
                InfosImg("270vaisseauattaque2", "images/unites/270attaque_2.png"),
                InfosImg("315vaisseauattaque2", "images/unites/315attaque_2.png"),
                InfosImg("0vaisseauattaque3", "images/unites/0attaque_3.png"),
                InfosImg("45vaisseauattaque3", "images/unites/45attaque_3.png"),
                InfosImg("90vaisseauattaque3", "images/unites/90attaque_3.png"),
                InfosImg("135vaisseauattaque3", "images/unites/135attaque_3.png"),
                InfosImg("180vaisseauattaque3", "images/unites/180attaque_3.png"),
                InfosImg("225vaisseauattaque3", "images/unites/225attaque_3.png"),
                InfosImg("270vaisseauattaque3", "images/unites/270attaque_3.png"),
                InfosImg("315vaisseauattaque3", "images/unites/315attaque_3.png"),
                InfosImg("0vaisseauattaque4", "images/unites/0attaque_4.png"),
                InfosImg("45vaisseauattaque4", "images/unites/45attaque_4.png"),
                InfosImg("90vaisseauattaque4", "images/unites/90attaque_4.png"),
                InfosImg("135vaisseauattaque4", "images/unites/135attaque_4.png"),
                InfosImg("180vaisseauattaque4", "images/unites/180attaque_4.png"),
                InfosImg("225vaisseauattaque4", "images/unites/225attaque_4.png"),
                InfosImg("270vaisseauattaque4", "images/unites/270attaque_4.png"),
                InfosImg("315vaisseauattaque4", "images/unites/315attaque_4.png"),
                InfosImg("0vaisseauattaque5", "images/unites/0attaque_5.png"),
                InfosImg("45vaisseauattaque5", "images/unites/45attaque_5.png"),
                InfosImg("90vaisseauattaque5", "images/unites/90attaque_5.png"),
                InfosImg("135vaisseauattaque5", "images/unites/135attaque_5.png"),
                InfosImg("180vaisseauattaque5", "images/unites/180attaque_5.png"),
                InfosImg("225vaisseauattaque5", "images/unites/225attaque_5.png"),
                InfosImg("270vaisseauattaque5", "images/unites/270attaque_5.png"),
                InfosImg("315vaisseauattaque5", "images/unites/315attaque_5.png"),
                InfosImg("0vaisseauattaque6", "images/unites/0attaque_6.png"),
                InfosImg("45vaisseauattaque6", "images/unites/45attaque_6.png"),
                InfosImg("90vaisseauattaque6", "images/unites/90attaque_6.png"),
                InfosImg("135vaisseauattaque6", "images/unites/135attaque_6.png"),
                InfosImg("180vaisseauattaque6", "images/unites/180attaque_6.png"),
                InfosImg("225vaisseauattaque6", "images/unites/225attaque_6.png"),
                InfosImg("270vaisseauattaque6", "images/unites/270attaque_6.png"),
                InfosImg("315vaisseauattaque6", "images/unites/315attaque_6.png"),
                InfosImg("0vaisseauattaque7", "images/unites/0attaque_7.png"),
                InfosImg("45vaisseauattaque7", "images/unites/45attaque_7.png"),
                InfosImg("90vaisseauattaque7", "images/unites/90attaque_7.png"),
                InfosImg("135vaisseauattaque7", "images/unites/135attaque_7.png"),
                InfosImg("180vaisseauattaque7", "images/unites/180attaque_7.png"),
                InfosImg("225vaisseauattaque7", "images/unites/225attaque_7.png"),
                InfosImg("270vaisseauattaque7", "images/unites/270attaque_7.png"),
                InfosImg("315vaisseauattaque7", "images/unites/315attaque_7.png"),
                InfosImg("0vaisseauattaque8", "images/unites/0attaque_8.png"),
                InfosImg("45vaisseauattaque8", "images/unites/45attaque_8.png"),
                InfosImg("90vaisseauattaque8", "images/unites/90attaque_8.png"),
                InfosImg("135vaisseauattaque8", "images/unites/135attaque_8.png"),
                InfosImg("180vaisseauattaque8", "images/unites/180attaque_8.png"),
                InfosImg("225vaisseauattaque8", "images/unites/225attaque_8.png"),
                InfosImg("270vaisseauattaque8", "images/unites/270attaque_8.png"),
                InfosImg("315vaisseauattaque8", "images/unites/315attaque_8.png"),
                InfosImg("0vaisseaucargo1", "images/unites/0cargo_1.png"),
                InfosImg("45vaisseaucargo1", "images/unites/45cargo_1.png"),
                InfosImg("90vaisseaucargo1", "images/unites/90cargo_1.png"),
                InfosImg("135vaisseaucargo1", "images/unites/135cargo_1.png"),
                InfosImg("180vaisseaucargo1", "images/unites/180cargo_1.png"),
                InfosImg("225vaisseaucargo1", "images/unites/225cargo_1.png"),
                InfosImg("270vaisseaucargo1", "images/unites/270cargo_1.png"),
                InfosImg("315vaisseaucargo1", "images/unites/315cargo_1.png"),
                InfosImg("0vaisseaucargo2", "images/unites/0cargo_2.png"),
                InfosImg("45vaisseaucargo2", "images/unites/45cargo_2.png"),
                InfosImg("90vaisseaucargo2", "images/unites/90cargo_2.png"),
                InfosImg("135vaisseaucargo2", "images/unites/135cargo_2.png"),
                InfosImg("180vaisseaucargo2", "images/unites/180cargo_2.png"),
                InfosImg("225vaisseaucargo2", "images/unites/225cargo_2.png"),
                InfosImg("270vaisseaucargo2", "images/unites/270cargo_2.png"),
                InfosImg("315vaisseaucargo2", "images/unites/315cargo_2.png"),
                InfosImg("0vaisseaucargo3", "images/unites/0cargo_3.png"),
                InfosImg("45vaisseaucargo3", "images/unites/45cargo_3.png"),
                InfosImg("90vaisseaucargo3", "images/unites/90cargo_3.png"),
                InfosImg("135vaisseaucargo3", "images/unites/135cargo_3.png"),
                InfosImg("180vaisseaucargo3", "images/unites/180cargo_3.png"),
                InfosImg("225vaisseaucargo3", "images/unites/225cargo_3.png"),
                InfosImg("270vaisseaucargo3", "images/unites/270cargo_3.png"),
                InfosImg("315vaisseaucargo3", "images/unites/315cargo_3.png"),
                InfosImg("0vaisseaucargo4", "images/unites/0cargo_4.png"),
                InfosImg("45vaisseaucargo4", "images/unites/45cargo_4.png"),
                InfosImg("90vaisseaucargo4", "images/unites/90cargo_4.png"),
                InfosImg("135vaisseaucargo4", "images/unites/135cargo_4.png"),
                InfosImg("180vaisseaucargo4", "images/unites/180cargo_4.png"),
                InfosImg("225vaisseaucargo4", "images/unites/225cargo_4.png"),
                InfosImg("270vaisseaucargo4", "images/unites/270cargo_4.png"),
                InfosImg("315vaisseaucargo4", "images/unites/315cargo_4.png"),
                InfosImg("0vaisseaucargo5", "images/unites/0cargo_5.png"),
                InfosImg("45vaisseaucargo5", "images/unites/45cargo_5.png"),
                InfosImg("90vaisseaucargo5", "images/unites/90cargo_5.png"),
                InfosImg("135vaisseaucargo5", "images/unites/135cargo_5.png"),
                InfosImg("180vaisseaucargo5", "images/unites/180cargo_5.png"),
                InfosImg("225vaisseaucargo5", "images/unites/225cargo_5.png"),
                InfosImg("270vaisseaucargo5", "images/unites/270cargo_5.png"),
                InfosImg("315vaisseaucargo5", "images/unites/315cargo_5.png"),
                InfosImg("0vaisseaucargo6", "images/unites/0cargo_6.png"),
                InfosImg("45vaisseaucargo6", "images/unites/45cargo_6.png"),
                InfosImg("90vaisseaucargo6", "images/unites/90cargo_6.png"),
                InfosImg("135vaisseaucargo6", "images/unites/135cargo_6.png"),
                InfosImg("180vaisseaucargo6", "images/unites/180cargo_6.png"),
                InfosImg("225vaisseaucargo6", "images/unites/225cargo_6.png"),
                InfosImg("270vaisseaucargo6", "images/unites/270cargo_6.png"),
                InfosImg("315vaisseaucargo6", "images/unites/315cargo_6.png"),
                InfosImg("0vaisseaucargo7", "images/unites/0cargo_7.png"),
                InfosImg("45vaisseaucargo7", "images/unites/45cargo_7.png"),
                InfosImg("90vaisseaucargo7", "images/unites/90cargo_7.png"),
                InfosImg("135vaisseaucargo7", "images/unites/135cargo_7.png"),
                InfosImg("180vaisseaucargo7", "images/unites/180cargo_7.png"),
                InfosImg("225vaisseaucargo7", "images/unites/225cargo_7.png"),
                InfosImg("270vaisseaucargo7", "images/unites/270cargo_7.png"),
                InfosImg("315vaisseaucargo7", "images/unites/315cargo_7.png"),
                InfosImg("0vaisseaucargo8", "images/unites/0cargo_8.png"),
                InfosImg("45vaisseaucargo8", "images/unites/45cargo_8.png"),
                InfosImg("90vaisseaucargo8", "images/unites/90cargo_8.png"),
                InfosImg("135vaisseaucargo8", "images/unites/135cargo_8.png"),
                InfosImg("180vaisseaucargo8", "images/unites/180cargo_8.png"),
                InfosImg("225vaisseaucargo8", "images/unites/225cargo_8.png"),
                InfosImg("270vaisseaucargo8", "images/unites/270cargo_8.png"),
                InfosImg("315vaisseaucargo8", "images/unites/315cargo_8.png"),
                InfosImg("0sonde1", "images/unites/0sonde_1.png"),
                InfosImg("45sonde1", "images/unites/45sonde_1.png"),
                InfosImg("90sonde1", "images/unites/90sonde_1.png"),
                InfosImg("135sonde1", "images/unites/135sonde_1.png"),
                InfosImg("180sonde1", "images/unites/180sonde_1.png"),
                InfosImg("225sonde1", "images/unites/225sonde_1.png"),
                InfosImg("270sonde1", "images/unites/270sonde_1.png"),
                InfosImg("315sonde1", "images/unites/315sonde_1.png"),
                InfosImg("0sonde2", "images/unites/0sonde_2.png"),
                InfosImg("45sonde2", "images/unites/45sonde_2.png"),
                InfosImg("90sonde2", "images/unites/90sonde_2.png"),
                InfosImg("135sonde2", "images/unites/135sonde_2.png"),
                InfosImg("180sonde2", "images/unites/180sonde_2.png"),
                InfosImg("225sonde2", "images/unites/225sonde_2.png"),
                InfosImg("270sonde2", "images/unites/270sonde_2.png"),
                InfosImg("315sonde2", "images/unites/315sonde_2.png"),
                InfosImg("0sonde3", "images/unites/0sonde_3.png"),
                InfosImg("45sonde3", "images/unites/45sonde_3.png"),
                InfosImg("90sonde3", "images/unites/90sonde_3.png"),
                InfosImg("135sonde3", "images/unites/135sonde_3.png"),
                InfosImg("180sonde3", "images/unites/180sonde_3.png"),
                InfosImg("225sonde3", "images/unites/225sonde_3.png"),
                InfosImg("270sonde3", "images/unites/270sonde_3.png"),
                InfosImg("315sonde3", "images/unites/315sonde_3.png"),
                InfosImg("0sonde4", "images/unites/0sonde_4.png"),
                InfosImg("45sonde4", "images/unites/45sonde_4.png"),
                InfosImg("90sonde4", "images/unites/90sonde_4.png"),
                InfosImg("135sonde4", "images/unites/135sonde_4.png"),
                InfosImg("180sonde4", "images/unites/180sonde_4.png"),
                InfosImg("225sonde4", "images/unites/225sonde_4.png"),
                InfosImg("270sonde4", "images/unites/270sonde_4.png"),
                InfosImg("315sonde4", "images/unites/315sonde_4.png"),
                InfosImg("0sonde5", "images/unites/0sonde_5.png"),
                InfosImg("45sonde5", "images/unites/45sonde_5.png"),
                InfosImg("90sonde5", "images/unites/90sonde_5.png"),
                InfosImg("135sonde5", "images/unites/135sonde_5.png"),
                InfosImg("180sonde5", "images/unites/180sonde_5.png"),
                InfosImg("225sonde5", "images/unites/225sonde_5.png"),
                InfosImg("270sonde5", "images/unites/270sonde_5.png"),
                InfosImg("315sonde5", "images/unites/315sonde_5.png"),
                InfosImg("0sonde6", "images/unites/0sonde_6.png"),
                InfosImg("45sonde6", "images/unites/45sonde_6.png"),
                InfosImg("90sonde6", "images/unites/90sonde_6.png"),
                InfosImg("135sonde6", "images/unites/135sonde_6.png"),
                InfosImg("180sonde6", "images/unites/180sonde_6.png"),
                InfosImg("225sonde6", "images/unites/225sonde_6.png"),
                InfosImg("270sonde6", "images/unites/270sonde_6.png"),
                InfosImg("315sonde6", "images/unites/315sonde_6.png"),
                InfosImg("0sonde7", "images/unites/0sonde_7.png"),
                InfosImg("45sonde7", "images/unites/45sonde_7.png"),
                InfosImg("90sonde7", "images/unites/90sonde_7.png"),
                InfosImg("135sonde7", "images/unites/135sonde_7.png"),
                InfosImg("180sonde7", "images/unites/180sonde_7.png"),
                InfosImg("225sonde7", "images/unites/225sonde_7.png"),
                InfosImg("270sonde7", "images/unites/270sonde_7.png"),
                InfosImg("315sonde7", "images/unites/315sonde_7.png"),
                InfosImg("0sonde8", "images/unites/0sonde_8.png"),
                InfosImg("45sonde8", "images/unites/45sonde_8.png"),
                InfosImg("90sonde8", "images/unites/90sonde_8.png"),
                InfosImg("135sonde8", "images/unites/135sonde_8.png"),
                InfosImg("180sonde8", "images/unites/180sonde_8.png"),
                InfosImg("225sonde8", "images/unites/225sonde_8.png"),
                InfosImg("270sonde8", "images/unites/270sonde_8.png"),
                InfosImg("315sonde8", "images/unites/315sonde_8.png"),
                InfosImg("stationgalaxie1", "images/unites/stationgalaxie_1.png"),
                InfosImg("stationgalaxie2", "images/unites/stationgalaxie_2.png"),
                InfosImg("stationgalaxie3", "images/unites/stationgalaxie_3.png"),
                InfosImg("stationgalaxie4", "images/unites/stationgalaxie_4.png"),
                InfosImg("stationgalaxie5", "images/unites/stationgalaxie_5.png"),
                InfosImg("stationgalaxie6", "images/unites/stationgalaxie_6.png"),
                InfosImg("stationgalaxie7", "images/unites/stationgalaxie_7.png"),
                InfosImg("stationgalaxie8", "images/unites/stationgalaxie_8.png"),
                InfosImg("stationplanetaire1", "images/unites/stationplanete_1.png"),
                InfosImg("stationplanetaire2", "images/unites/stationplanete_2.png"),
                InfosImg("stationplanetaire3", "images/unites/stationplanete_3.png"),
                InfosImg("stationplanetaire4", "images/unites/stationplanete_4.png"),
                InfosImg("stationplanetaire5", "images/unites/stationplanete_5.png"),
                InfosImg("stationplanetaire6", "images/unites/stationplanete_6.png"),
                InfosImg("stationplanetaire7", "images/unites/stationplanete_7.png"),
                InfosImg("stationplanetaire8", "images/unites/stationplanete_8.png")
                ]

    
    def __init__(self,parent,ip,nom,largeur=800,hauteur=600):
        self.root=Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        self.nom=None
        self.largeur=largeur
        self.hauteur=hauteur
        self.images = self.charger_images(self.liste_images)
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
    
    def charger_images(self, liste_images):
        images = dict()
        for image in liste_images:
            images[image.nom] = PhotoImage(file = image.source)
        return images
    
    
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
            id_systeme=maselection[5]
            id_planete=maselection[2]
            if id_planete in self.modes["planetes"].keys():
                s=self.modes["planetes"][id_planete]
            else:
                systeme = self.modele.objets_cliquables[id_systeme]
                planete = self.modele.objets_cliquables[id_planete]
                s=VuePlanete(self, systeme, planete)
                self.modes["planetes"][id_planete]=s
            s.initier_affichage()
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
        
        g.afficherdecor() #pourrait etre remplace par une image fait avec PIL -> moins d'objets
        self.changecadre(self.cadrejeu,1)
        self.changemode(self.modes["galaxie"])
                
    def fermerfenetre(self):
        # Ici, on pourrait mettre des actions a faire avant de fermer (sauvegarder, avertir etc)
        self.parent.fermefenetre()
        
    def action_joueur(self, action, parametres = {}):
            self.parent.action_joueur(action, parametres)
        
