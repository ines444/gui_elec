# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 21:59:30 2022

@author: Tristan
"""

'''

Création des classes

'''


from Interface import *
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

global Liste_clique
global c 
global window
global canvas
global T

c = []
Liste_clique = []
T = 0

def clique_bouton(resistance):

    global Liste_clique
    
    if resistance.value == 0:
        resistance.value = 1 
        Liste_clique.append([resistance.x,resistance.y])
        print(Liste_clique)
        
    elif resistance.value == 1:
        if [resistance.x,resistance.y] in Liste_clique:
            for k in range(len(Liste_clique)):
                if Liste_clique[k] == [resistance.x,resistance.y]:
                    del Liste_clique[k]
                    print(Liste_clique)
            resistance.value = 0

    if len(Liste_clique) == 2:
        print('coucou')
        fil_0 = C.fil(Liste_clique[0],Liste_clique[1])
        ligne1 = canvas.create_line(fil_0.coord_1[0], fil_0.coord_1[1], fil_0.coord_2[0], fil_0.coord_2[1])
        canvas.itemconfigure(ligne1, fill='yellow')
        canvas.pack() 
 
        
def getvalue(myentry,f):
    global c
    c.append(myentry.get())
    
    if len(c) > 4:
        f.quit()
        f.destroy()
        
def getvalueT(myentry,f):
    global c
    c.append(myentry.get())
    
    if len(c) > 3:
        f.quit()
        f.destroy()
    
    
def ouvre_fenetre(window):
    
   global c
   
   f = Toplevel(window)
   f.title("paramètre composant")
   window.geometry( '500x150')  
   c = []  
   saisie_nom = Entry(f, bd = 10)
   saisie_nom.grid(column = 1,row = 0)
   label_nom = Button( f, text = "Nom du composant", command = lambda:getvalue(saisie_nom,f))
   label_nom.grid(column = 0,row = 0) 
   
   saisie_longueur = Entry(f, bd = 10)
   saisie_longueur.grid(column = 1,row = 3)        
   label_longueur = Button( f, text = "longueur", command = lambda:getvalue(saisie_longueur,f))
   label_longueur.grid(column = 0,row = 3)


   saisie_largeur = Entry(f, bd = 10)
   saisie_largeur.grid(column = 3,row = 3)  
   label_largeur = Button( f, text = "Largeur", command = lambda:getvalue(saisie_largeur,f))
   label_largeur.grid(column = 2,row = 3)
   
   saisie_X = Entry(f, bd = 10)
   saisie_X.grid(column = 1,row = 4)   
   label_X = Button( f, text = "X", command = lambda:getvalue(saisie_X,f))
   label_X.grid(column = 0,row = 4)

   saisie_Y = Entry(f, bd = 10)
   saisie_Y.grid(column = 3,row = 4)
   label_Y = Button( f, text = "Y" , command = lambda:getvalue(saisie_Y,f))
   label_Y.grid(column = 2,row = 4)
   f.mainloop()
   return c


def ouvre_fenetre_source(window):
    
   global c, T
   
   f = Toplevel(window)
   f.title("paramètre composant")
   window.geometry( '500x150')  
   c = []  
   saisie_nom = Entry(f, bd = 10)
   saisie_nom.grid(column = 1,row = 0)
   label_nom = Button( f, text = "Nom du composant", command = lambda:getvalueT(saisie_nom,f))
   label_nom.grid(column = 0,row = 0) 
   
  
   saisie_tension = Entry(f, bd = 10)
   saisie_tension.grid(column = 1,row = 1)
   label_tension = Button(f, text = "Tension", command = lambda:getvalueT(saisie_tension,f))
   label_tension.grid(column = 0, row = 1)
  
    
   saisie_X = Entry(f, bd = 10)
   saisie_X.grid(column = 1,row = 4)   
   label_X = Button( f, text = "X", command = lambda:getvalueT(saisie_X,f))
   label_X.grid(column = 0,row = 4)

   saisie_Y = Entry(f, bd = 10)
   saisie_Y.grid(column = 3,row = 4)
   label_Y = Button( f, text = "Y" , command = lambda:getvalueT(saisie_Y,f))
   label_Y.grid(column = 2,row = 4)

   f.mainloop()
   return c

def ferme_circuit(window):
    
    global Liste_clique, canvas 
    print(Liste_clique)
    try:
        
        fil_0 = C.fil(Liste_clique[0],Liste_clique[1])
        print('coucu')
        ligne2 = canvas.create_line(fil_0.coord_1[0], fil_0.coord_1[1], fil_0.coord_2[0], fil_0.coord_2[1])
        print('cucu')
        canvas.itemconfigure(ligne2, fill='yellow')
        canvas.pack()         
         
    except:
        print("il n'y a pas de lien existant")
    




def init_composant(window):
    
    global c, canvas
    c = []

    sw = ouvre_fenetre(window)   
    print(c)
    nom = composants(c[0], c[1], c[2], 0, c[3],c[4])
    S = nom.surface()
    print(S)
    print(nom.nom)
    btn_1 = Button(window, text = nom.nom, bd = S,  command= lambda:clique_bouton(nom))  
    position_x = nom.x
    position_y = nom.y
    btn_1.place(x = position_x, y = position_y)

def init_source(window):
    
    global c, canvas,T
    

    sw = ouvre_fenetre_source(window)   
    print(c)
    nom = source(c[0],  np.double(c[1]), c[2], c[3])
    S = nom.surface()
    print(S)
    print(nom.nom)
    btn_1 = Button(window, text = nom.nom, bd = S,  command= lambda:clique_bouton(nom))  
    position_x = nom.x
    position_y = nom.y
    btn_1.place(x = position_x, y = position_y)
     
    




class fenetre_main(Tk) :
    
    def __init__(self,nom,longueur,largeur):
        
        
        Tk.__init__(self)
        self.nom = nom
        self.longueur = longueur
        self.largeur = largeur
        self.ouvre_fenetre()
        
        
    def ouvre_fenetre(self):
       
       global canvas 
       
       canvas = Canvas(self, width = self.longueur, height = self.largeur, background = 'black')
       btn_ferme = Button(self, text = 'Fermer le circuit', bd = 17,  command= lambda:ferme_circuit(self))
       btn_ferme.pack()
     
       self.title("Interface simulation circuit électronique")
       self.geometry( str(self.longueur) + 'x' + str(self.largeur))
       self.create_menu_bar()
       
       
    def create_menu_bar(self):
        
        menu_bar = Menu(self)
        menu_file = Menu(menu_bar, tearoff=0)  
        menu_file.add_command(label="Resistance" , command=lambda:init_composant(self))
        menu_file.add_command(label="Source de tension", command = lambda:init_source(self))
        menu_bar.add_cascade(label="Composants", menu=menu_file)
        self.config(menu=menu_bar) 
       

        

class composants():
    

    def __init__(self,nom, longueur, largeur,value, x, y):
        
        self.nom = nom
        self.longueur = int(longueur)
        self.largeur = int(largeur)
        self.value = int(value)
        self.x = int(x)
        self.y = int(y)
        
        
    def surface(self):
        return str(self.longueur * self.largeur)
    #def position_composant(self):        

class source():


    def __init__(self,nom,tension,x,y):

        self.nom = nom
        self.tension = tension
        self.longueur = 3
        self.largeur = 4
        self.value = 0
        self.x = int(x)
        self.y = int(y)

    def surface(self):
        return str(self.longueur * self.largeur)
               
class fil : 
    
    def __init__(self,coord_1, coord_2):
        
        self.coord_1 = coord_1
        self.coord_2 = coord_2
        print(self.coord_1)
        print(self.coord_2)

    '''    
    def trace(self):
        
        plt.plot([self.coord_1[0],self.coord_2[0]],[self.coord_1[1],self.coord_2[1]],'y')
    '''    
            
            
    
    