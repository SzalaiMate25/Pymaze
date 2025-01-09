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

    loadFixedTextures()
    loadTimer()
    loadButtons()

def loadTimer():
    global timerFont, timerPos

    timerFont = pygame.font.Font("freesansbold.ttf",48)
    timerPos = (width / 2, 50)

def loadButtons():
    global diffFont, easyPos, mediumPos, hardPos, easyButtonRect, mediumButtonRect, hardButtonRect, easyText, mediumText, hardText, easyTextRect, mediumTextRect, hardTextRect

    diffFont = pygame.font.Font("freesansbold.ttf",26)

    easyPos = (100,50)
    mediumPos = (240,50)
    hardPos = (380,50)

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
    global button

    button = pygame.image.load("textures/button.png")

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