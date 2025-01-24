import pygame

class Element:
    def __init__(self, texture, pos=(0, 0)):
        self.texture = texture
        self.rect = texture.image.get_rect()
        self.rect.center = (pos[0] + texture.offset[0], pos[1] + texture.offset[1])

    def clicked(self, button):
        mouse_pos = pygame.mouse.get_pos()

        return self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[button]
    
    def get_texture(self):
        return self.texture.image
    
    def get_rect(self):
        return self.rect