from tkinter import *
from PIL import Image
from cv2 import *
import numpy as np
import matplotlib.pyplot as plt
import math

def OpenPath(path):
    return imread(path)

def convertToGray(img):
    img = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])
    return img

def seuil(img, val_seuil):
    h = img.shape[0]
    w = img.shape[1]

    img_thres= np.zeros((h,w))
    # loop over the image, pixel by pixel
    for y in range(0, h):
        for x in range(0, w):
            # threshold the pixel
            pixel = img[y][x]
            if pixel < val_seuil:
                img_thres[y][x] = 0
            else:
                img_thres[y][x] = 255
    return img_thres

def imgSum(img1, img2):
    h = img1.shape[0]
    w = img1.shape[1]
    h2 = img2.shape[0]
    w2 = img2.shape[1]
    img1=convertToGray(img1)
    img2=convertToGray(img2)
    if h==h2 and w==w2:
        img_sum= np.zeros((h,w))
        for y in range(0, h):
            for x in range(0, w):
                if img1[y][x] + img2[y][x] >= 255:
                    img_sum[y][x] = 255
                else:
                    img_sum[y][x] = 0
        return img_sum
    else:
        print("Veuiller prendre deux images de même taille")

def imgSoust(img1, img2):
    h = img1.shape[0]
    w = img1.shape[1]
    h2 = img2.shape[0]
    w2 = img2.shape[1]
    img1=convertToGray(img1)
    img2=convertToGray(img2)
    if h==h2 and w==w2:
        img_soust= np.zeros((h,w))
        for y in range(0, h):
            for x in range(0, w):
                if img1[y][x] - img2[y][x] <= 0:
                    img_soust[y][x] = 0
                else:
                    img_soust[y][x] = 255
        return img_soust
    else:
        print("Veuiller prendre deux images de même taille")

def Erosion(im, erodeOrder):
    
    se=np.zeros((erodeOrder,erodeOrder))
    for i in range(erodeOrder):
        for j in range(erodeOrder):
            if i==0 or j==0 or i == -1 or j == -1:
                se[i][j] = 0
            else:
                se[i][j] = 255

    # se = [[0,255,0],[255,255,255],[0,255,0]]

    rows,columns = im.shape[0], im.shape[1]
    #Initialize counters (Just to keep track)
    fit = 0
    hit = 0
    miss = 0

    #Create a copy of the image to modified it´s pixel values
    ero = np.copy(im)
    #Specify kernel size (w*w)
    w = erodeOrder
    # w=3

    #
    for i in range(rows-w-1):
        for j in range(columns-w-1):
            #Get a region (crop) of the image equal to kernel size
            crop = im[i:w+i,j:w+j]
            #Convert region of image to an array
            img = np.array(crop)

            #Get center
            a = math.floor(w/2)
            b = math.floor(w/2)
            
            #Initialize counters 
            matches = 0
            blacks = 0

            #Count number of black pixels (0) and value matches between the two matrix
            for x in range(w):
                for y in range(w):
                    #Count number of black pixels (0)
                    if(img[x][y] == 0):
                        blacks = blacks+1
                        #Count number of matching pixel values between the two matrix   
                        if (img[x][y] == se[x][y]):         
                            matches = matches+1

            #Test if structuring element fit crop image pixels
            #If fit it does nothing because center pixel is already black
            if(matches > 0):
                if(matches == blacks):
                    #Touch
                    fit = fit + 1
                    pass
                #Test if structuring element hit crop image pixels
                #If hit change ero center pixel to black
                elif(matches < blacks):
                    #Hit
                    hit = hit+1
                    ero[i+a][j+b] = np.all(img[se==255]) * 255
            #If no pixel match just pass
            else:
                #Miss
                miss=miss+1
                pass
    return ero

def Dilatation(im, dilateOrder):
    
    se=np.zeros((dilateOrder,dilateOrder))
    for i in range(dilateOrder):
        for j in range(dilateOrder):
            if i==0 or j==0 or i == -1 or j == -1:
                se[i][j] = 0
            else:
                se[i][j] = 255

    # se = [[0,255,0],[255,255,255],[0,255,0]]

    rows,columns = im.shape[0], im.shape[1]
    #Initialize counters (Just to keep track)
    fit = 0
    hit = 0
    miss = 0

    #Create a copy of the image to modified it´s pixel values
    dil = np.copy(im)
    #Specify kernel size (w*w)
    w = dilateOrder
    # w = 3


    #
    for i in range(rows-w-1):
        for j in range(columns-w-1):
            #Get a region (crop) of the image equal to kernel size
            crop = im[i:w+i,j:w+j]
            #Convert region of image to an array
            img = np.array(crop)

            #Get center
            a = math.floor(w/2)
            b = math.floor(w/2)
            
            #Initialize counters 
            matches = 0
            blacks = 0

            #Count number of black pixels (0) and value matches between the two matrix
            for x in range(w):
                for y in range(w):
                    #Count number of black pixels (0)
                    if(img[x][y] == 0):
                        blacks = blacks+1
                        #Count number of matching pixel values between the two matrix   
                        if (img[x][y] == se[x][y]):         
                            matches = matches+1

            #Test if structuring element fit crop image pixels
            #If fit it does nothing because center pixel is already black
            if(matches > 0):
                if(matches == blacks):
                    #Touch
                    fit = fit + 1
                    pass
                #Test if structuring element hit crop image pixels
                #If hit change ero center pixel to black
                elif(matches < blacks):
                    #Hit
                    hit = hit+1
                    dil[i+a][j+b] = np.any(img[se==255]) * 255
            #If no pixel match just pass
            else:
                #Miss
                miss=miss+1
                pass
    return dil

def Ouverture(img, Order):
    img_Ouverte = Dilatation(Erosion(img, Order), Order)
    return img_Ouverte

def Fermeture(img, Order):
    img_Fermee = Erosion(Dilatation(img, Order), Order)
    return img_Fermee

def Amincissement():
    img = imread("D:/VS/Dipanda/Carre.png")
    img1 = img.copy()

    thin = np.zeros(img.shape)

    for i in range(10):
        eroded = Erosion(img1,3)
        opened = Ouverture(eroded, 3)
        subset = imgSoust(erode,opened)
        thin = imgSum(subset,thin)
        img1 = eroded.copy()
    
    imshow("Original", img)
    imshow("Thinned", thin)

    return thin


def Epaisissement():
    pass

def Lantuejoul(img, Order, imgPath):
    pass

def test():
    print("coucou")

def createWindow():
    fenetre = Tk()
    fenetre.title("Traitement d'image")
    menubar = Menu(fenetre)
    fenetre.config(menu=menubar)

    fileMenu = Menu(menubar)

    submenu = Menu(fileMenu)
    submenu.add_command(label="Open", command=test)
    submenu.add_command(label="toGray")
    submenu.add_command(label="Seuil")
    submenu.add_command(label="Erode")
    submenu.add_command(label="Dilate")
    menubar.add_cascade(label="Edit", menu=submenu)
    return fenetre

if __name__ == "__main__":
    imgPath = "D:/VS/Dipanda/Carre.png"
    img = OpenPath(imgPath)
    thin = Amincissement()
    # img = convertToGray(img, imgPath)
    # img_seuil = seuil(img, imgPath, 128)
    # print(img_seuil)
    # # img_erod = Erosion(img_seuil, 5, imgPath)
    # img_dilate = Dilatation(img_seuil, 5, imgPath)
    # img_ouv = Ouverture(img_seuil, 5, imgPath)
    # img_ferm = Fermeture(img_seuil, 5, imgPath)
    # fen = createWindow()
    # fen.mainloop()
    


    



