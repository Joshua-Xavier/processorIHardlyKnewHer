

class Process:

    def __init__(self):
        self.id = ''
        self.arrivalTime = -1
        self.duration = -1
        self.turnAroundTime = -1
        self.waitingTime = -1
        self.timeSpentExecuting = 0


    ## --GETTERS--
    def getID(self):
        return self.id

    def getArrivalTime(self):
        return self.arrivalTime

    def getDuration(self):
        return self.duration

    def getTurnAroundTime(self):
        return self.turnAroundTime

    def getWaitingTime(self):
        return self.waitingTime

    def getTimeSpentExecuting(self):
        return self.timeSpentExecuting

    ## --SETTERS--

    def setTimeSpentExecuting(self, time_increment):
        self.timeSpentExecuting += time_increment

    ## --METHODS--
    def isFinished(self):
        #process will only be complete when the time spent executing
        # is equal to the duration of time the process needs
        return self.timeSpentExecuting == self.duration

    def calculateTurnAroundTime(self, clock):
        assert(self.isFinished())
        self.turnAroundTime = clock - self.arrivalTime

    def calculateWaitingTime(self, clock):
        assert(self.isFinished())
        self.waitingTime = clock - self.arrivalTime - self.duration
