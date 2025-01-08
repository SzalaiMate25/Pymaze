import timer
import highscoreManager as highscores
import window
import pygame
import sys

pygame.init()
window.init(1200, 900, 100) # The actual size of the maze will be 1200x800, as the top 100 pixels will be taken up by the UI

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    

    window.drawMaze()

    pygame.display.flip()
    window.clock.tick(60)