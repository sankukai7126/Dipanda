from tkinter import *
from PIL import Image
from cv2 import *
import numpy as np
import matplotlib.pyplot as plt
import math

class Traitement:

    cheminFichierPrincipal = ""

    def __init__(self):
        print("Init")  

    def getCheminPrincipale(self):
        return self.cheminFichierPrincipal

    def setCheminPrincipale(self,chemin):
        self.cheminFichierPrincipal = chemin

    def OpenPath(self,path):
        return imread(path)

    def convertToGray(self,img, imgPath):
        img = np.dot(img[...,:3], [0.299, 0.587, 0.114])
        return img

    def Seuillage(self,img, val_seuil):
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

    def imgSum(self,img1, img2, imgPath):
        h = img1.shape[0]
        w = img1.shape[1]
        h2 = img2.shape[0]
        w2 = img2.shape[1]
        img1=self.convertToGray(img1)
        img2=self.convertToGray(img2)
        if h==h2 and w==w2:
            img_sum= np.zeros((h,w))
            for y in range(0, h):
                for x in range(0, w):
                    if img1[y][x] + img2[y][x] >= 255:
                        img_sum[y][x] = 255
                    else:
                        img_sum[y][x] = 0
            imwrite(os.path.dirname(imgPath) + "/sum.png", img_sum)
            imshow("Addition", img_sum)
            return img_sum
        else:
            print("Veuiller prendre deux images de même taille")

    def imgSoust(self,img1, img2, imgPath):
        h = img1.shape[0]
        w = img1.shape[1]
        h2 = img2.shape[0]
        w2 = img2.shape[1]
        img1=self.convertToGray(img1)
        img2=self.convertToGray(img2)
        if h==h2 and w==w2:
            img_soust= np.zeros((h,w))
            for y in range(0, h):
                for x in range(0, w):
                    if img1[y][x] - img2[y][x] <= 0:
                        img_soust[y][x] = 0
                    else:
                        img_soust[y][x] = 255
            imwrite(os.path.dirname(imgPath) + "/soust.png", img_soust)
            imshow("Soustraction", img_soust)
            return img_soust
        else:
            print("Veuiller prendre deux images de même taille")

    def ErosionWithPath(self,erodeOrder, canSave):
        
        imgPath = self.getCheminPrincipale()
        im=self.OpenPath(imgPath)

        se=getStructuringElement(MORPH_ELLIPSE,(erodeOrder,erodeOrder)) * 255

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

                blacks = np.count_nonzero(img == 0)
                matches = np.count_nonzero((img == 0) & (se == 0))

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
                        ero[i+a][j+b] = 0
                #If no pixel match just pass
                else:
                    #Miss
                    miss=miss+1
                    pass
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Erode.png", ero)
        imshow("Erosion",ero)
        return ero
    
    def Erosion(self, im, erodeOrder, canSave):

        imgPath = self.getCheminPrincipale()

        se=getStructuringElement(MORPH_ELLIPSE,(erodeOrder,erodeOrder)) * 255

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

                blacks = np.count_nonzero(img == 0)
                matches = np.count_nonzero((img == 0) & (se == 0))

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
                        ero[i+a][j+b] = 0
                #If no pixel match just pass
                else:
                    #Miss
                    miss=miss+1
                    pass
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Erode.png", ero)
        imshow("Erosion",ero)
        return ero

    def DilatationWithPath(self,dilateOrder, canSave):
        
        imgPath = self.getCheminPrincipale()
        im=self.OpenPath(imgPath)

        se=getStructuringElement(MORPH_ELLIPSE,(dilateOrder,dilateOrder)) * 255

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

                blacks = np.count_nonzero(img == 0)
                matches = np.count_nonzero((img == 0) & (se == 0))

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
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Dilate.png", dil)
        imshow("Dilatation",dil)
        return dil
    
    def Dilatation(self, im, dilateOrder, canSave):
        
        imgPath = self.getCheminPrincipale()

        se=getStructuringElement(MORPH_ELLIPSE,(dilateOrder,dilateOrder)) * 255

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

                blacks = np.count_nonzero(img == 0)
                matches = np.count_nonzero((img == 0) & (se == 0))

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
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Dilate.png", dil)
        imshow("Dilatation",dil)
        return dil

    def OuvertureWithPath(self, Order, canSave):
        imgPath = self.getCheminPrincipale()
        img=self.OpenPath(imgPath)
        img_Ouverte = self.Erosion(self.Dilatation(img, Order, False), Order, False)
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Ouverte.png", img_Ouverte)
        imshow("Ouverture",img_Ouverte)
        return img_Ouverte
    
    def Ouverture(self, img, Order, canSave):
        imgPath = self.getCheminPrincipale()
        img_Ouverte = self.Erosion(self.Dilatation(img, Order, False), Order, False)
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Ouverte.png", img_Ouverte)
        imshow("Ouverture",img_Ouverte)
        return img_Ouverte

    def FermetureWithPath(self, Order, canSave):
        imgPath = self.getCheminPrincipale()
        img=self.OpenPath(imgPath)
        img_Fermee = self.Dilatation(self.Erosion(img, Order, False), Order, False)
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Fermee.png", img_Fermee)
        imshow("Fermeture",img_Fermee)
        return img_Fermee

    def Fermeture(self, img, Order, canSave):
        imgPath = self.getCheminPrincipale()
        img_Fermee = self.Dilatation(self.Erosion(img, Order, False), Order, False)
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Fermee.png", img_Fermee)
        imshow("Fermeture",img_Fermee)
        return img_Fermee

    def Amincissement(self):
        pass

    def Epaisissement(self):
        pass

    def Lantuejoul(self,img, Order, imgPath):
        pass

    def test(self):
        print("coucou")