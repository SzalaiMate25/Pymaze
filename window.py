import pygame

def init(w, h, o):
    global width, height, screen, clock, offset
    width = w
    height = h
    offset = o

    pygame.init()

    pygame.display.set_caption('Pymaze')

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

backgroundColor = (203,208,209)

def drawMaze():
    screen.fill(backgroundColor)