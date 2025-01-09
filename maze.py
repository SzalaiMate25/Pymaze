class Maze:
    def __init__(self, map, distances):
        self.map = map
        self.distances = distances
        self.size = (len(map[0]),len(map))
        self.finishPos = [0,0]