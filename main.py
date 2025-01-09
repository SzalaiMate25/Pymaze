import timer
import highscoreManager
import window
import pygame
import functions
from sys import exit
from copy import deepcopy as copy

pygame.init()
window.init(1080, 892, 100) # The actual size of the maze will be 1080x892, as the top 100 pixels will be taken up by the UI

sizes = ( # ((size_x, size_y), tileSize)
    ((15, 11), 72), # 0 - easy
    ((45, 33), 24), # 1 - medium
    ((135, 99), 8), # 2 - hard
)

speeds = (9,3,1)

highscores = highscoreManager.HighscoreManager("",1,3)
timer = timer.Timer()

timer.startTimer()

def start(d):
    global difficulty, playerPos, speed, maze, rects, direction, timer, run, windowOpen

    difficulty = d

    playerPos = [sizes[difficulty][1] * 2.5, sizes[difficulty][1] * 2.5]
    speed = speeds[difficulty]

    window.loadTextures(sizes[difficulty][1])
    window.createSingleRects()
    maze = functions.generate(functions.createEmpty(sizes[difficulty][0]))

    rects = window.generateRects(maze, sizes[difficulty][1])
    direction = 1

    run = True
    windowOpen = False

    timer.startTimer()

start(0)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                start(difficulty)

    mousePos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0] and not preivousPressed:
        if window.easyButtonRect.collidepoint(mousePos):
            start(0)
        if window.mediumButtonRect.collidepoint(mousePos):
            start(1)
        if window.hardButtonRect.collidepoint(mousePos):
            start(2)

    preivousPressed = pygame.mouse.get_pressed()[0]

    if run:
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

        if window.playerRect.colliderect(window.finishRect):
            print(f"Congratulations! You completed a{("n easy","n intermediate"," hard")[difficulty]} maze! Your time was {timer.convertTime(timer.getTimer(),1,specificity=difficulty + 1)} {("seconds","","")[difficulty]}!")
            
            newBest = highscores.addHighscore(timer.getTimer(),difficulty)

            if newBest:
                print("New best time!")
            runTime = timer.convertTime(timer.getTimer(),1,specificity=difficulty + 1)
            run = False
            windowOpen = True

    window.drawMaze(maze, sizes[difficulty][1])
    window.drawPlayer(playerPos, direction)
    window.drawGUI(timer.convertTime(timer.getTimer(),1,specificity=difficulty + 1) if run else runTime)
    if windowOpen:
        window.drawWindow(difficulty, runTime, timer.convertTime(highscores.getBestScore(difficulty),1,specificity=difficulty + 1), newBest)

        mousePos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if window.closeRect.collidepoint(mousePos):
                windowOpen = False

            if window.playAgainRect.collidepoint(mousePos):
                start(difficulty)

            if window.quitRect.collidepoint(mousePos):
                exit()

    pygame.display.flip()
    window.clock.tick(60)