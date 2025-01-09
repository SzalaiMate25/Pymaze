import time

class Timer:
    def __init__(self):
        self.subtract = 0
        self.paused = False

    def startTimer(self):
        self.startTime = time.time()

    def getTimer(self):
        if self.startTime == 0:
            return 0
        elif self.paused:
            return self.pausedAt - self.startTime - self.subtract
        return time.time() - self.startTime - self.subtract 
    
    def pause(self):
        self.paused = True
        self.pausedAt = time.time()

    def resume(self):
        self.paused = False
        self.subtract += time.time() - self.pausedAt


    def convertTime(self, timer, format, specificity=0):
        days = int(timer / 86400)
        hours = int(timer / 3600) - days * 24
        minutes = int(timer / 60) - days * 24 - hours * 60
        seconds = int(timer) - days * 24 - hours * 3600 - minutes * 60

        if format == 0:
            return (days, hours, minutes, seconds)
        
        if len(str(hours)) == 1:
            hours = "0" + str(hours)

        if len(str(minutes)) == 1:
            minutes = "0" + str(minutes)

        if len(str(seconds)) == 1:
            seconds = "0" + str(seconds)

        if specificity == 1:
            return str(seconds)
        if specificity == 2:
            return f"{minutes}:{seconds}"
        if specificity == 3:
            return f"{hours}:{minutes}:{seconds}"
        return f"{days}:{hours}:{minutes}:{seconds}"

