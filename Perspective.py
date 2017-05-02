from tkinter import *
from PIL import *

import Unite

class Perspective(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent.cadrejeu)
        self.parent=parent
        self.modele=None
        self.cadreetatactif=None
        self.images={}
        self.cible = False
        self.cadrevue=Frame(self,width=400,height=400, bg="lightgreen")
        self.cadrevue.pack(side=LEFT,expand=1,fill=BOTH)
        
        self.cadreinfo=Frame(self,width=200,height=200,bg="darkgrey")
        self.cadreinfo.pack(side=LEFT,fill=Y)
        self.cadreinfo.pack_propagate(0)
        self.cadreetat=Frame(self.cadreinfo,width=200,height=200,bg="grey20")
        self.cadreetat.pack()
        
        self.scrollX=Scrollbar(self.cadrevue,orient=HORIZONTAL)
        self.scrollY=Scrollbar(self.cadrevue)
        self.canevas=Canvas(self.cadrevue,width=1000,height=600,bg="grey11",
                             xscrollcommand=self.scrollX.set,
                             yscrollcommand=self.scrollY.set)
        
        self.canevas.bind("<Button-1>",self.selectionner)
        self.canevas.bind("<Button-3>",self.cibler)
        
        self.scrollX.config(command=self.canevas.xview)
        self.scrollY.config(command=self.canevas.yview)
        self.canevas.grid(column=0,row=0,sticky=N+E+W+S)
        self.cadrevue.columnconfigure(0,weight=1)
        self.cadrevue.rowconfigure(0,weight=1)
        self.scrollX.grid(column=0,row=1,sticky=E+W)
        self.scrollY.grid(column=1,row=0,sticky=N+S)
        
        self.labid=Label(self.cadreinfo,text=self.parent.nom)
        self.labid.pack()
        
        self.cadreetataction=Frame(self.cadreetat,width=200,height=200,bg="grey20")
        
        self.cadreetatmsg=Frame(self.cadreetat,width=200,height=200,bg="grey20")
        
        self.cadreminimap=Frame(self.cadreinfo,width=200,height=200,bg="grey20")
        self.cadreminimap.pack(side=BOTTOM)
        self.minimap=Canvas(self.cadreminimap,width=200,height=200,bg="grey11")
        self.minimap.bind("<Button-1>",self.cliquerminimap)
        self.minimap.pack()
    def selectionner(self,evt):
        pass
    
    def cibler(self, evt):
        pass
    
    """
    def cibler(self, evt):
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
    
    def changecadreetat(self,cadre):
        if self.cadreetatactif:
            self.cadreetatactif.pack_forget()
            self.cadreetatactif=None
        if cadre:
            self.cadreetatactif=cadre
            self.cadreetatactif.pack()
            
    def montrevaisseauxselection(self):
        self.changecadreetat(self.cadreetatmsg)
    
    def action_joueur(self, action, parametres = {}, selectionner = False):
        if selectionner:
            pass
        else:
            try:
                parametres["id_appelant"] = self.maselection[2]
            except TypeError:
                pass
            self.parent.parent.action_joueur(action, parametres)
            
            
    
