import tkinter
from PIL import Image
from LoadImage import LoadImage
import Seuil

if __name__ == "__main__":
    img = Image.open("C:/Users/Mikrail/Documents/4A Dipanda/TP/test.png").save("C:/Users/Mikrail/Documents/4A Dipanda/TP/test.bmp")
    img.show()