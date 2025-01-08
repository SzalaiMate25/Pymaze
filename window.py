import pygame

def init(w, h):
    global width, height, screen, clock
    width = w
    height = h

    pygame.init()

    pygame.display.set_caption('Pymaze')

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

def drawMaze():
    pass