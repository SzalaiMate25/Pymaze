class HighscoreManager:
    def __init__(self, name, type, categories):
        self.name = name # Used to differentiate separate highscore files
        self.type = type # 0: highscore - higher score gets added, 1: best time: lower time gets added
        self.categories = categories # How many separate categories are there
        self.fileName = "highscores" + str(self.name).capitalize() + ".txt" # Name of the file that belongs to this highScoreManager

        try:
            open(self.fileName,"x")

            self.highscores = [-1.0 for i in range(categories)]

            file = open(self.fileName,"w")
            file.write("|".join([str(score) for score in self.highscores]))
            
        except:
            self.highscores = [float(score) for score in open(self.fileName,"r").read().split("|")]

    def writeFile(self):
        file = open(self.fileName, "w")
        file.write("|".join([str(score) for score in self.highscores]))

    def getHighscores(self):
        return self.highscores
    
    def addHighscore(self, score, category) -> bool: # Returns whether the score was a new best or not
        if self.type == 0:
            if score > self.highscores[category]:
                self.highscores[category] = float(score)
                self.writeFile()
                if self.highscores[category] != -1.0:
                    return True
        else:
            if score < self.highscores[category] or self.highscores[category] == -1.0:
                self.highscores[category] = float(score)
                self.writeFile()
                if self.highscores[category] != -1.0:
                    return True
        return False

    def getBestScore(self, category):
        return self.highscores[category]