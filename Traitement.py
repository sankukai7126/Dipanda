from tkinter import *
from PIL import Image
from cv2 import *
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
from PIL import Image
from PIL import ImageTk
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

    def convertToGray(self,img):
        img = np.float32(img)
        img = np.array(img)
        # img = np.dot(img[...,:3], [0.299, 0.587, 0.114])
        img = cvtColor(img, COLOR_BGR2GRAY)
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

    def SeuillageWithPath(self, val_seuil):
        img = self.OpenPath(self.getCheminPrincipale())
        img = self.convertToGray(img)
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
        imS = cv2.resize(img_thres, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Fermeture", imS)
        return img_thres

    def imgSum(self,img1, img2, CanSave):
        img1=self.convertToGray(img1)
        img2=self.convertToGray(img2)
        h = img1.shape[0]
        w = img1.shape[1]
        h2 = img2.shape[0]
        w2 = img2.shape[1]
        if h==h2 and w==w2:
            img_sum= np.zeros((h,w))
            for y in range(0, h):
                for x in range(0, w):
                    if img1[y][x] + img2[y][x] >= 255:
                        img_sum[y][x] = 255
                    else:
                        img_sum[y][x] = 0
            if CanSave == True:
                imwrite(os.path.dirname(self.getCheminPrincipale()) + "/sum.png", img_sum)
            #imshow("Addition", img_sum)
            imS = cv2.resize(img_sum, (300, 300),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
            cv2.imshow("Sum", imS)


            return img_sum
        else:
            print("Veuiller prendre deux images de même taille")

    def imgSoust(self,img1, img2, CanSave):
        img1=self.convertToGray(img1)
        img2=self.convertToGray(img2)
        h = img1.shape[0]
        w = img1.shape[1]
        h2 = img2.shape[0]
        w2 = img2.shape[1]
        if h==h2 and w==w2:
            img_soust= np.zeros((h,w))
            for y in range(0, h):
                for x in range(0, w):
                    if img1[y][x] - img2[y][x] <= 0:
                        img_soust[y][x] = 0
                    else:
                        img_soust[y][x] = 255
            if CanSave == True:
                imwrite(os.path.dirname(self.getCheminPrincipale()) + "/soust.png", img_soust)
            #imshow("Soustraction", img_soust)

            imS = cv2.resize(img_soust, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
            cv2.imshow("sous", imS)

            return img_soust
        else:
            print("Veuiller prendre deux images de même taille")

    def ErosionWithPath(self,erodeOrder, canSave):
        
        imgPath = self.getCheminPrincipale()
        im=self.OpenPath(imgPath)

        se=getStructuringElement(MORPH_ELLIPSE,(erodeOrder,erodeOrder)) * 255

        rows,columns = im.shape[0], im.shape[1]

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
                    if(matches < blacks):
                        ero[i+a][j+b] = 0

        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Erode.png", ero)
        #imshow("Erosion",ero)
        imS = cv2.resize(ero, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Erosion", imS)
        return ero
    
    def Erosion(self, im, erodeOrder, canSave):
        im = np.array(im)
        imgPath = self.getCheminPrincipale()

        se=getStructuringElement(MORPH_ELLIPSE,(erodeOrder,erodeOrder)) * 255

        rows,columns = im.shape[0], im.shape[1]

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
                    if(matches < blacks):
                        ero[i+a][j+b] = 0

        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Erode.png", ero)
        #imshow("Erosion",ero)
        imS = cv2.resize(ero, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Erosion", imS)
        return ero

    def DilatationWithPath(self,dilateOrder, canSave):
        
        imgPath = self.getCheminPrincipale()
        im=self.OpenPath(imgPath)

        se=getStructuringElement(MORPH_ELLIPSE,(dilateOrder,dilateOrder)) * 255

        rows,columns = im.shape[0], im.shape[1]

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
                    if(matches < blacks):
                        dil[i+a][j+b] = np.any(img[se==255]) * 255

        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Dilate.png", dil)
        #imshow("Dilatation",dil)
        imS = cv2.resize(dil, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Dilatation", imS)
        return dil
    
    def Dilatation(self, im, dilateOrder, canSave):
        im = np.array(im)
        imgPath = self.getCheminPrincipale()

        se=getStructuringElement(MORPH_ELLIPSE,(dilateOrder,dilateOrder)) * 255

        rows,columns = im.shape[0], im.shape[1]

        #On prend une copie de l'image
        dil = np.copy(im)
        #On specifie la taille de l'élément structurant
        w = dilateOrder
        # w = 3

        for i in range(rows-w-1):
            for j in range(columns-w-1):
                #On prend une partie de l'image
                crop = im[i:w+i,j:w+j]
                #On cette partie d'image en tableau
                img = np.array(crop)

                #On recupere le centre du morceau d'image
                a = math.floor(w/2)
                b = math.floor(w/2)
                
                #On initialise des compteurs pour recuperer le nombre de case noire et si les cases correspondent
                matches = 0
                blacks = 0

                blacks = np.count_nonzero(img == 0)
                matches = np.count_nonzero((img == 0) & (se == 0))

                #On test si l'element structurant correspond a la section couper
                if(matches > 0):
                    if(matches < blacks):
                        dil[i+a][j+b] = np.any(img[se==255]) * 255

        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Dilate.png", dil)
        #imshow("Dilatation",dil)
        imS = cv2.resize(dil, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Dilatation", imS)
        return dil


    def FermetureWithPath(self, Order, canSave):
        imgPath = self.getCheminPrincipale()
        img=self.OpenPath(imgPath)
        img_Ouverte = self.Erosion(self.Dilatation(img, Order, False), Order, False)
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Fermee.png", img_Ouverte)
        #imshow("Ouverture",img_Ouverte)
        imS = cv2.resize(img_Ouverte, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Fermeture", imS)
        return img_Ouverte
    
    def Fermeture(self, img, Order, canSave):
        imgPath = self.getCheminPrincipale()
        img_Ouverte = self.Erosion(self.Dilatation(img, Order, False), Order, False)
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Fermee.png", img_Ouverte)
        #imshow("Ouverture",img_Ouverte)
        imS = cv2.resize(img_Ouverte, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Fermeture", imS)
        return img_Ouverte


    def OuvertureWithPath(self, Order, canSave):
        imgPath = self.getCheminPrincipale()
        img=self.OpenPath(imgPath)
        img_Fermee = self.Dilatation(self.Erosion(img, Order, False), Order, False)
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Ouverte.png", img_Fermee)
        #imshow("Fermeture",img_Fermee)
        imS = cv2.resize(img_Fermee, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Ouverture", imS)
        return img_Fermee


    def Ouverture(self, img, Order, canSave):
        imgPath = self.getCheminPrincipale()
        img_Fermee = self.Dilatation(self.Erosion(img, Order, False), Order, False)
        if canSave == True:
            imwrite(os.path.dirname(imgPath) + "/Ouverte.png", img_Fermee)
        #imshow("Fermeture",img_Fermee)
        imS = cv2.resize(img_Fermee, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Ouverture", imS)
        return img_Fermee

    def Amincissement(self):
        img = self.OpenPath(self.getCheminPrincipale())
        img1 = img.copy()

        lant = np.zeros(img.shape)
           
        erodee = self.Erosion(img1,3,True)
        erodee = self.OpenPath((os.path.dirname(self.getCheminPrincipale()) + "/Erode.png"))
        ouverte = self.Ouverture(erodee, 3,True)
        ouverte = self.OpenPath((os.path.dirname(self.getCheminPrincipale()) + "/Ouverte.png"))
        soustraction = self.imgSoust(erodee,ouverte,True)
        soustraction = self.OpenPath((os.path.dirname(self.getCheminPrincipale()) + "/soust.png"))
        lant = self.imgSum(soustraction,lant, True)
        lant = self.OpenPath((os.path.dirname(self.getCheminPrincipale()) + "/sum.png"))
        img1 = self.OpenPath((os.path.dirname(self.getCheminPrincipale()) + "/Erode.png"))
        
        imgS = cv2.resize(img, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Original", imgS)
        lantS = cv2.resize(lant, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Thinning", lantS)

        return lant

    def Epaisissement(self):
        pass

    def Lantuejoul(self):
        img = self.OpenPath(self.getCheminPrincipale())
        img1 = img.copy()

        lant = np.zeros(img.shape)

        for i in range(50):            
            erodee = self.Erosion(img1,3,True)
            erodee = self.OpenPath((os.path.dirname(self.getCheminPrincipale()) + "/Erode.png"))
            ouverte = self.Ouverture(erodee, 3,True)
            ouverte = self.OpenPath((os.path.dirname(self.getCheminPrincipale()) + "/Ouverte.png"))
            soustraction = self.imgSoust(erodee,ouverte,True)
            soustraction = self.OpenPath((os.path.dirname(self.getCheminPrincipale()) + "/soust.png"))
            lant = self.imgSum(soustraction,lant, True)
            lant = self.OpenPath((os.path.dirname(self.getCheminPrincipale()) + "/sum.png"))
            img1 = self.OpenPath((os.path.dirname(self.getCheminPrincipale()) + "/Erode.png"))
        
        imgS = cv2.resize(img, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Original", imgS)
        lantS = cv2.resize(lant, (400, 400),fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)                    # Resize image
        cv2.imshow("Thinning", lantS)

        return lant

    def test(self):
        print("coucou")