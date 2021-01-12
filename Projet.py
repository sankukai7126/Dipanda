from tkinter import *
from PIL import Image
from cv2 import *
import numpy as np
import matplotlib.pyplot as plt

def OpenPath(path):
    return imread(path)

def convertToGray(img, imgPath):
    img = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])
    imwrite(os.path.dirname(imgPath) + "/gray.png", img)
    return img

def seuil(img,imgPath, val_seuil):
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
    imwrite(os.path.dirname(imgPath) + "/seuil.png", img_thres)
    return img_thres

def imgSum(img1, img2, imgPath):
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
        imwrite(os.path.dirname(imgPath) + "/sum.png", img_sum)
        return img_sum
    else:
        print("Veuiller prendre deux images de même taille")

def imgSoust(img1, img2, imgPath):
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
        imwrite(os.path.dirname(imgPath) + "/soust.png", img_soust)
        return img_soust
    else:
        print("Veuiller prendre deux images de même taille")

def erode(img):
    pass

def dilate(img):
    pass

def test(str):
    print(str)

def createWindow():
    fenetre = Tk()
    fenetre.title("Traitement d'image")
    menubar = Menu(fenetre)
    fenetre.config(menu=menubar)

    fileMenu = Menu(menubar)

    submenu = Menu(fileMenu)
    submenu.add_command(label="Open")
    submenu.add_command(label="toGray")
    submenu.add_command(label="Seuil")
    submenu.add_command(label="Erode")
    submenu.add_command(label="Dilate")
    menubar.add_cascade(label="Edit", menu=submenu)
    return fenetre

if __name__ == "__main__":
    imgPath = "D:/VS/Dipanda/test.png"
    img = OpenPath(imgPath)
    img = convertToGray(img, imgPath)
    img_seuil = seuil(img, imgPath, 128)
    print(img_seuil)
    fen = createWindow()
    fen.mainloop()
    


    



