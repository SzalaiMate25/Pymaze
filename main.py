import timer
import highscoreManager as hs
import window
import pygame
import functions
from sys import exit

pygame.init()
window.init(1080, 892, 100) # The actual size of the maze will be 1080x892, as the top 100 pixels will be taken up by the UI

difficulty = 2

sizes = ( # ((size_x, size_y), tileSize)
    ((15, 11), 72), # 0 - easy
    ((45, 33), 24), # 1 - medium
    ((135, 99), 8), # 2 - hard
)

window.loadTextures(sizes[difficulty][1])
maze = functions.generate(functions.createEmpty(sizes[difficulty][0]))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



    window.drawMaze(maze, sizes[difficulty][1])

    pygame.display.flip()
    window.clock.tick(60)