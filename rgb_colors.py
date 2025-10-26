import random

class RgbColors:
    def __init__(self, r=0, g=0, b=0):
        self.random_rgb = ()
        self.r = r
        self.g = g
        self.b = b

    def create_rgb(self):
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.random_rgb = (self.r, self.g, self.b)
        return self.random_rgb