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

if __name__ == "__main__":
    img = imread("D:/VS/Dipanda/test.png")
    img = convertToGray(img)
    imwrite("D:/VS/Dipanda/gray.png", img)
    img_seuil = seuil(img)
    print(img_seuil)
    imwrite("D:/VS/Dipanda/img_seuil.png", img_seuil)
    


    



