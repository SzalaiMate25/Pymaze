import timer
import highscoreManager as hs
import window
import pygame
import functions
from sys import exit

pygame.init()
window.init(1080, 892, 100) # The actual size of the maze will be 1080x892, as the top 100 pixels will be taken up by the UI

difficulty = 0

sizes = ( # ((size_x, size_y), tileSize)
    ((15, 11), 72), # 0 - easy
    ((45, 33), 24), # 1 - medium
    ((135, 99), 8), # 2 - hard
)

playerPos = [sizes[difficulty][1] * 2.5, sizes[difficulty][1] * 2.5]
speed = 10

window.loadTextures(sizes[difficulty][1])
window.createPlayerRect()
maze = functions.generate(functions.createEmpty(sizes[difficulty][0]))

rects = window.generateRects(maze, sizes[difficulty][1])
direction = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        direction = 0
        playerPos[1] -= speed
    if keys[pygame.K_RIGHT]:
        direction = 1
        playerPos[0] += speed
    if keys[pygame.K_DOWN]:
        direction = 2
        playerPos[1] += speed
    if keys[pygame.K_LEFT]:
        direction = 3
        playerPos[0] -= speed 


    window.drawMaze(maze, sizes[difficulty][1])
    window.drawPlayer(playerPos, direction)

    pygame.display.flip()
    window.clock.tick(60)