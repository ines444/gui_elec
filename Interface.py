# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np



'''


Interface


'''


from tkinter import *
import Classe as C
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

global Liste_clique
global window
Liste_clique = []



if __name__ == '__main__':
    
    global window
       
    '''
    
    Création de la fenêtre
    
    '''
    
    window = C.fenetre_main('fenetre', 500, 500)
    window.mainloop()
 



        

