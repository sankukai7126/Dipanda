import tkinter
from PIL import Image
from cv2 import *
import numpy as np
import matplotlib.pyplot as plt

def convertToGray(img):
    return np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])

def seuil(img):
    h = img.shape[0]
    w = img.shape[1]

    img_thres= np.zeros((h,w))
    # loop over the image, pixel by pixel
    for y in range(0, h):
        for x in range(0, w):
            # threshold the pixel
            pixel = img[y][x]
            if pixel < 128:
                img_thres[y][x] = 0
            else:
                img_thres[y][x] = 255
    return img_thres

def imgSum(img1, img2):
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
        return img_sum
    else:
        print("Veuiller prendre deux images de même taille")

def imgSoust(img1, img2):
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
        return img_soust
    else:
        print("Veuiller prendre deux images de même taille")

if __name__ == "__main__":
    img = imread("D:/VS/Dipanda/test.png")
    img = convertToGray(img)
    imwrite("D:/VS/Dipanda/gray.png", img)
    img_seuil = seuil(img)
    print(img_seuil)
    imwrite("D:/VS/Dipanda/img_seuil.png", img_seuil)
    


    



