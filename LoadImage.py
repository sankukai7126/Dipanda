from PIL import Image
import numpy as np

class LoadImage:
    def __init__(self, imgPath):
        self.picturePath = imgPath

    def convertToBitmap(self):
        img = Image.open(self.picturePath)
        img = img.tobitmap()
        img.save('test.bmp')
