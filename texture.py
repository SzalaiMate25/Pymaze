import pygame

class Texture:
    def __init__(self, image, offset=(0,0), scale=1, path="", extension="png"):
        self.offset = offset
        self.scale = scale
        self.path = path
        if self.path != "":
            self.path += "/"
        self.raw_image = pygame.image.load(path + image + "." + extension)
        self.image = pygame.transform.scale_by(self.raw_image, self.scale)

    def rescale(self, scale):
        self.scale = scale
        self.image = pygame.transform.scale_by(self.raw_image, self.scale)