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

def drawMaze(maze, size):
    screen.fill(backgroundColor)

    for i in range(maze.size[1]):
        for j in range(maze.size[0]):
            try:
                screen.blit(tiles[maze.map[i][j]], (i * size, j * size + offset))
            except: pass

def loadTextures(size):
    global tiles, player

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

def generateRects(maze, size):
    rects = []

    for i in range(maze.size[1]):
        for j in range(maze.size[0]):
            if maze.map[i][j] in ("#","+"):
                rect = tiles.values()[0].get_rect()
                rect.right = i * size
                rect.top = j * size + offset
                rects.append(rect)
    return rects