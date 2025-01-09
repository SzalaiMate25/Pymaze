import pygame

def init(w, h, o):
    global width, height, screen, clock, offset
    width = w
    height = h
    offset = o

    pygame.init()

    pygame.display.set_caption('Pymaze')

    screen = pygame.display.set_mode((width, height), flags=pygame.FULLSCREEN|pygame.SCALED)
    clock = pygame.time.Clock()

    loadFixedTextures()
    loadTimer()
    loadButtons()
    loadWindow()
    loadWindowButtons()

def loadTimer():
    global timerFont, timerPos

    timerFont = pygame.font.Font("freesansbold.ttf",48)
    timerPos = (width / 2, 50)

def loadButtons():
    global diffFont, easyPos, mediumPos, hardPos, easyButtonRect, mediumButtonRect, hardButtonRect, easyText, mediumText, hardText, easyTextRect, mediumTextRect, hardTextRect

    diffFont = pygame.font.Font("freesansbold.ttf",26)

    easyPos = (80,50)
    mediumPos = (220,50)
    hardPos = (360,50)

    easyButtonRect = button.get_rect()
    mediumButtonRect = button.get_rect()
    hardButtonRect = button.get_rect()
    easyButtonRect.center = easyPos
    mediumButtonRect.center = mediumPos
    hardButtonRect.center = hardPos

    easyText = diffFont.render("Easy",True,"black")
    mediumText = diffFont.render("Medium",True,"black")
    hardText = diffFont.render("Hard",True,"black")

    easyTextRect = easyText.get_rect()
    mediumTextRect = mediumText.get_rect()
    hardTextRect = hardText.get_rect()
    easyTextRect.center = easyPos
    mediumTextRect.center = mediumPos
    hardTextRect.center = hardPos

def drawTimer(timer):
    global timerText, timerRect

    timerText = timerFont.render(timer,True,"black")

    timerRect = timerText.get_rect()
    timerRect.center = timerPos

    screen.blit(timerText, timerRect)

def drawButtons():
    screen.blit(button, easyButtonRect)
    screen.blit(button, mediumButtonRect)
    screen.blit(button, hardButtonRect)

    screen.blit(easyText, easyTextRect)
    screen.blit(mediumText, mediumTextRect)
    screen.blit(hardText, hardTextRect)

def drawGUI(timer):
    drawTimer(timer)
    drawButtons()

backgroundColor = (203,208,209)

def drawMaze(maze, size):
    screen.fill(backgroundColor)

    for i in range(maze.size[1]):
        for j in range(maze.size[0]):
            try:
                screen.blit(tiles[maze.map[i][j]], (i * size, j * size + offset))
            except: pass

def drawPlayer(pos, dir):
    playerRect.center = (pos[0], pos[1] + offset)
    screen.blit(player[dir], playerRect)

def loadTextures(size):
    global tiles, player, button

    tiles = {
        "#":pygame.transform.scale(pygame.image.load("textures/wall.png"), (size,size)),
        "+":pygame.transform.scale(pygame.image.load("textures/wall.png"), (size,size)),
        "F":pygame.transform.scale(pygame.image.load("textures/finish.png"), (size,size)),
            }

    player = [
        pygame.transform.scale(pygame.image.load("textures/player_up.png"), (size * 4 / 5, size * 4 / 5)),
        pygame.transform.scale(pygame.image.load("textures/player_right.png"), (size * 4 / 5, size * 4 / 5)),
        pygame.transform.scale(pygame.image.load("textures/player_down.png"), (size * 4 / 5, size * 4 / 5)),
        pygame.transform.scale(pygame.image.load("textures/player_left.png"), (size * 4 / 5, size * 4 / 5))
    ]

def loadFixedTextures():
    global button, window, close, buttonLarge

    button = pygame.image.load("textures/button.png")

    window = pygame.image.load("textures/window.png")
    close = pygame.image.load("textures/close.png")
    buttonLarge = pygame.image.load("textures/largebutton.png")

def generateRects(maze, size):
    rects = []

    for i in range(maze.size[1]):
        for j in range(maze.size[0]):
            if maze.map[i][j] in ("#","+"):
                rect = list(tiles.values())[0].get_rect()
                rect.right = i * size + size
                rect.top = j * size + offset
                rects.append(rect)
            elif maze.map[i][j] == "F":
                finishRect.right = i * size + size
                finishRect.top = j * size + offset
    return rects

def createSingleRects():
    global playerRect, playerCollider, finishRect

    playerRect = player[0].get_rect()
    playerCollider = player[0].get_rect()
    finishRect = list(tiles.values())[0].get_rect()

def loadWindow():
    global windowRect, closeRect, completeRect, completeText
    global difficultyPos, titleFont, diffText, diffRect, valueFont, yourTimeTitle, yourTimeTitleRect, yourTimePos, bestTimeTitleRect, bestTimeTitleText, bestTimePos

    windowRect = window.get_rect()
    windowRect.center = (width / 2, height / 2)

    closeRect = close.get_rect()
    closeRect.center = (windowRect.topright[0] - 10,windowRect.topright[1] + 10)

    titleFont = pygame.font.Font("freesansbold.ttf",48)

    completePos = (width / 2, height / 2 - windowRect.height / 2 + 50)
    completeText = titleFont.render("Maze Completed!",True,"black")
    completeRect = completeText.get_rect()
    completeRect.center = completePos

    smallTitleFont = pygame.font.Font("freesansbold.ttf",32)

    difficultyPos = (width / 2, height / 2 - windowRect.height / 2 + 200)

    valueFont = pygame.font.Font("freesansbold.ttf",72)

    diffTitlePos = (width / 2, height / 2 - windowRect.height / 2 + 150)
    diffText = smallTitleFont.render("Difficulty:",True,"black")
    diffRect = diffText.get_rect()
    diffRect.center = diffTitlePos

    yourTimeTitlePos = (width / 2, height / 2 - windowRect.height / 2 + 275)
    yourTimeTitle = smallTitleFont.render("Your Time:",True,"black")
    yourTimeTitleRect = yourTimeTitle.get_rect()
    yourTimeTitleRect.center = yourTimeTitlePos

    yourTimePos = (width / 2, height / 2 - windowRect.height / 2 + 325)

    bestTimeTitlePos = (width / 2, height / 2 - windowRect.height / 2 + 400)
    bestTimeTitleText = smallTitleFont.render("Best Time:",True,"black")
    bestTimeTitleRect = bestTimeTitleText.get_rect()
    bestTimeTitleRect.center = bestTimeTitlePos

    bestTimePos = (width / 2, height / 2 - windowRect.height / 2 + 450)

def loadWindowButtons():
    global playAgainRect, playAgainTextRect, playAgainText, quitRect, quitText, quitTextRect

    playAgainPos = (width / 2 - 100, height / 2 + windowRect.height / 2 - 75)

    playAgainRect = buttonLarge.get_rect()
    playAgainRect.center = playAgainPos

    playAgainText = diffFont.render("Play Again",True,"black")
    playAgainTextRect = playAgainText.get_rect()
    playAgainTextRect.center = playAgainPos

    quitPos = (width / 2 + 100, height / 2 + windowRect.height / 2 - 75)

    quitRect = buttonLarge.get_rect()
    quitRect.center = quitPos

    quitText = diffFont.render("Quit",True,"black")
    quitTextRect = quitText.get_rect()
    quitTextRect.center = quitPos

def drawWindow(difficulty, time, bestTime, newBest):

    difficultyText = valueFont.render(("Easy","Medium","Hard")[difficulty],True,"black")
    difficultyRect = difficultyText.get_rect()
    difficultyRect.center = difficultyPos

    yourTimeText = valueFont.render(time,True,"black")
    yourTimeRect = yourTimeText.get_rect()
    yourTimeRect.center = yourTimePos

    bestTimeText = valueFont.render(bestTime,True,"black")
    bestTimeRect = bestTimeText.get_rect()
    bestTimeRect.center = bestTimePos

    screen.blit(window, windowRect)
    screen.blit(close, closeRect)
    screen.blit(completeText, completeRect)

    screen.blit(diffText, diffRect)
    screen.blit(difficultyText, difficultyRect)
    
    screen.blit(yourTimeTitle, yourTimeTitleRect)
    screen.blit(yourTimeText, yourTimeRect)

    screen.blit(bestTimeTitleText, bestTimeTitleRect)
    screen.blit(bestTimeText, bestTimeRect)

    # buttons

    screen.blit(buttonLarge, playAgainRect)
    screen.blit(playAgainText, playAgainTextRect)

    screen.blit(buttonLarge, quitRect)
    screen.blit(quitText, quitTextRect)