import Traitement
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import *
from cv2 import *
import cv2
from PIL import Image
from PIL import ImageTk

def loadPicture(filename,Frame3):
    displayer = Canvas(Frame3,width=400,height=400)
    displayer.grid(column=0, row=0,padx=(0, 10),pady=(10,10))

    img = Image.open(filename)
    img = img.resize((300,300), Image.ANTIALIAS)
    photoImg =  ImageTk.PhotoImage(img)

    displayer.create_image(40,40,anchor=NW,image=photoImg)
    print("loading image")
    Mafenetre.mainloop()  

def askopenfile(t,Frame3):
    from tkinter.filedialog import askopenfilename
    Tk().withdraw() 
    filename = askopenfilename()
    t.setCheminPrincipale(filename)
    print(filename)
    loadPicture(filename,Frame3)

def askopenFileSum(t):
    from tkinter.filedialog import askopenfilename
    Tk().withdraw() 
    filename = askopenfilename()
    print(filename)
    t.imgSum(imread(t.getCheminPrincipale()),imread(filename),True)

def askopenFileSustraction(t):
    from tkinter.filedialog import askopenfilename
    Tk().withdraw() 
    filename = askopenfilename()
    print(filename)
    t.imgSoust(imread(t.getCheminPrincipale()),imread(filename),True)

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
    Bouton1 = Button(Frame1, text = 'sum', command = lambda: askopenFileSum(t))
    Bouton2 = Button(Frame1, text = 'sous', command = lambda: askopenFileSustraction(t))
    Bouton3 = Button(Frame1, text = 'erosion', command = lambda: t.ErosionWithPath(3,True))
    Bouton4 = Button(Frame1, text = 'dilatation', command = lambda: t.DilatationWithPath(3,True))
    Bouton5 = Button(Frame1, text = 'ouverture', command = lambda: t.OuvertureWithPath(3,True))
    Bouton6 = Button(Frame1, text = 'fermeture', command = lambda: t.FermetureWithPath(3,True))
    Bouton7 = Button(Frame1, text = 'epaisissement', command = lambda: t.Epaisissement())
    Bouton8 = Button(Frame1, text = 'amincissement', command = lambda: t.Amincissement(True))
    Bouton9 = Button(Frame1, text = 'seuil', command = lambda: t.SeuillageWithPath(128))
    Bouton10 = Button(Frame1, text = 'lantuejoul', command = lambda: t.Lantuejoul())


    Bouton1.grid(column=0, row=0,padx=(0, 10),pady=(10,10))
    Bouton2.grid(column=1, row=0,padx=(0, 10),pady=(10,10))
    Bouton3.grid(column=2, row=0,padx=(0, 10),pady=(10,10))
    Bouton4.grid(column=3, row=0,padx=(0, 10),pady=(10,10))
    Bouton5.grid(column=4, row=0,padx=(0, 10),pady=(10,10))
    Bouton6.grid(column=5, row=0,padx=(0, 10),pady=(10,10))
    Bouton7.grid(column=6, row=0,padx=(0, 10),pady=(10,10))
    Bouton8.grid(column=7, row=0,padx=(0, 10),pady=(10,10))
    Bouton9.grid(column=8, row=0,padx=(0, 10),pady=(10,10))
    Bouton10.grid(column=9, row=0,padx=(0, 10),pady=(10,10))



    search = Button(Frame2, text='Browse', command= lambda: askopenfile(t,Frame3))
    search.grid(column=0, row=0,padx=(0, 10),pady=(10,10))

    # Lancement du gestionnaire d'événements
    Mafenetre.mainloop()