import timer
import highscoreManager as hs
import window
import pygame
import functions
from sys import exit
from copy import deepcopy as copy

pygame.init()
window.init(1080, 892, 100) # The actual size of the maze will be 1080x892, as the top 100 pixels will be taken up by the UI

difficulty = 1

sizes = ( # ((size_x, size_y), tileSize)
    ((15, 11), 72), # 0 - easy
    ((45, 33), 24), # 1 - medium
    ((135, 99), 8), # 2 - hard
)

speeds = (9,3,1)

playerPos = [sizes[difficulty][1] * 2.5, sizes[difficulty][1] * 2.5]
speed = speeds[difficulty]

window.loadTextures(sizes[difficulty][1])
window.createPlayerRect()
maze = functions.generate(functions.createEmpty(sizes[difficulty][0]))

rects = window.generateRects(maze, sizes[difficulty][1])
direction = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    colliderPos = copy(playerPos)
    window.playerCollider.center = (colliderPos[0], colliderPos[1] + window.offset)

    if window.playerCollider.collidelist(rects) == -1:
        resetPos = copy(playerPos)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        direction = 0
        colliderPos[1] -= speed / (keys[pygame.K_LSHIFT] + 1)
        window.playerCollider.center = (colliderPos[0], colliderPos[1] + window.offset)

        if window.playerCollider.collidelist(rects) != -1:
            colliderPos = copy(resetPos)
            window.playerCollider.center = (colliderPos[0], colliderPos[1] + window.offset)
        else:
            playerPos[1] -= speed / (keys[pygame.K_LSHIFT] + 1)

    if keys[pygame.K_RIGHT]:
        direction = 1
        colliderPos[0] += speed / (keys[pygame.K_LSHIFT] + 1)
        window.playerCollider.center = (colliderPos[0], colliderPos[1] + window.offset)

        if window.playerCollider.collidelist(rects) != -1:
            colliderPos = copy(resetPos)
            window.playerCollider.center = (colliderPos[0], colliderPos[1] + window.offset)
        else:
            playerPos[0] += speed / (keys[pygame.K_LSHIFT] + 1)

    if keys[pygame.K_DOWN]:
        direction = 2
        colliderPos[1] += speed / (keys[pygame.K_LSHIFT] + 1)
        window.playerCollider.center = (colliderPos[0], colliderPos[1] + window.offset)

        if window.playerCollider.collidelist(rects) != -1:
            colliderPos = copy(resetPos)
            window.playerCollider.center = (colliderPos[0], colliderPos[1] + window.offset)
        else:
            playerPos[1] += speed / (keys[pygame.K_LSHIFT] + 1)

    if keys[pygame.K_LEFT]:
        direction = 3
        colliderPos[0] -= speed / (keys[pygame.K_LSHIFT] + 1)
        window.playerCollider.center = (colliderPos[0], colliderPos[1] + window.offset) 

        if window.playerCollider.collidelist(rects) != -1:
            colliderPos = copy(resetPos)
            window.playerCollider.center = (colliderPos[0], colliderPos[1] + window.offset)
        else:
            playerPos[0] -= speed / (keys[pygame.K_LSHIFT] + 1)


    window.drawMaze(maze, sizes[difficulty][1])
    window.drawPlayer(playerPos, direction)

    pygame.display.flip()
    window.clock.tick(60)