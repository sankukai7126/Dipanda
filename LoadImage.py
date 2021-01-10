from PIL import Image

class LoadImage:
    def __init__(self, imgPath):
        self.picturePath = imgPath

    def load(self):
        self.im = Image.open(self.picturePath)
        return self.im
