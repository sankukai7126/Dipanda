import Traitement
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import *

def loadPicture(filename,Frame3):
    displayer = Canvas(Frame3,width=400,height=400)
    displayer.grid(column=0, row=0,padx=(0, 10),pady=(10,10))

    #load a test picture
    img = PhotoImage(file=filename)
    displayer.create_image(40,40,anchor=NW,image=img)
    print("loading image")
    Mafenetre.mainloop()  

def askopenfile(t,Frame3):
    from tkinter.filedialog import askopenfilename
    Tk().withdraw() 
    filename = askopenfilename()
    t.setCheminPrincipale(filename)
    print(filename)
    loadPicture(filename,Frame3)

if __name__=='__main__':
    
    t = Traitement.Traitement()

    # Création de la fenêtre principale (main window)
    Mafenetre = Tk()

    Mafenetre.minsize(650, 650)
    Mafenetre.title("Voici notre logiciel de traitement d'image !")
  
    # frame 1
    Frame1 = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
    Frame1.pack(side=TOP, padx=5, pady=5)

    # frame 2
    Frame2 = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
    Frame2.pack(side=TOP, padx=10, pady=10)
    # frame 3
    Frame3 = Frame(Mafenetre, borderwidth=2, relief=GROOVE)
    Frame3.pack(side=TOP, padx=10, pady=10)

    #elements
    Bouton1 = Button(Frame1, text = 'sum', command = t.imgSum)
    Bouton2 = Button(Frame1, text = 'sous', command = t.imgSoust)
    Bouton3 = Button(Frame1, text = 'erotion', command = t.Erosion)
    Bouton4 = Button(Frame1, text = 'dilatation', command = t.Dilatation)
    Bouton5 = Button(Frame1, text = 'ouverture', command = t.Ouverture)
    Bouton6 = Button(Frame1, text = 'fermeture', command = t.Fermeture)

    Bouton1.grid(column=0, row=0,padx=(0, 10),pady=(10,10))
    Bouton2.grid(column=1, row=0,padx=(0, 10),pady=(10,10))
    Bouton3.grid(column=2, row=0,padx=(0, 10),pady=(10,10))
    Bouton4.grid(column=3, row=0,padx=(0, 10),pady=(10,10))
    Bouton5.grid(column=4, row=0,padx=(0, 10),pady=(10,10))
    Bouton6.grid(column=5, row=0,padx=(0, 10),pady=(10,10))

    search = Button(Frame2, text='Browse', command= lambda: askopenfile(t,Frame3))
    search.grid(column=0, row=0,padx=(0, 10),pady=(10,10))

    # Lancement du gestionnaire d'événements
    Mafenetre.mainloop()