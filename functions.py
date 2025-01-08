import maze
from random import randint as rand

offsets = ((-1,0),(0,1),(1,0),(0,-1))
doffsets = ((-2,0),(0,2),(2,0),(0,-2))

def createEmpty(size):
    map = [["#" for j in range(size[1])] for i in range(size[0])]
    for i in range(size[1]):
        map[0][i] = "+"
        map[size[0] - 1][i] = "+"
    for i in range(size[0]):
        map[i][0] = "+"
        map[i][size[1] - 1] = "+"
    return map

def generate(map):
    newMaze = maze.Maze(map, [[0 for j in range(len(map[0]))] for i in range(len(map))])

    pos = (2,2)
    dir = rand(0,3)

    highestDistance = 0
    destination = (2,2)

    newMaze.map[pos[0]][pos[1]] = "."
    visited = set()

    iterations = 0
    
    while True:
        iterations += 1
        visited.add((pos[0],pos[1]))

        if rand(1,3) in (1,2):
            dir = (dir + rand(-1,1) + 4) % 4
        if newMaze.map[pos[0] + doffsets[dir][0]][pos[1] + doffsets[dir][1]] != "+":
            if newMaze.map[pos[0] + doffsets[dir][0]][pos[1] + doffsets[dir][1]] == "#":
                newMaze.map[pos[0] + offsets[dir][0]][pos[1] + offsets[dir][1]] = "."
                newMaze.distances[pos[0] + doffsets[dir][0]][pos[1] + doffsets[dir][1]] = newMaze.distances[pos[0]][pos[1]] + 1

                if newMaze.distances[pos[0]][pos[1]] + 1 > highestDistance:
                    destination = (pos[0] + doffsets[dir][0], pos[1] + doffsets[dir][1])
                    highestDistance = newMaze.distances[pos[0]][pos[1]] + 1
            
            pos = (pos[0] + doffsets[dir][0], pos[1] + doffsets[dir][1])
            newMaze.map[pos[0]][pos[1]] = "."

            if len(visited) == int((newMaze.size[0] - 3)/2) * int((newMaze.size[1] - 3)/2):
                newMaze.map[destination[0]][destination[1]] = "F"
                return newMaze