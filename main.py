import timer
import highscoreManager as highscores
import window
import pygame
import sys

pygame.init()
window.init(1000,800)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    window.clock.tick(60)