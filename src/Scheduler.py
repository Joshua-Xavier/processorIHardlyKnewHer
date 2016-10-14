from src.Queue import Queue
import copy

class Scheduler:

    def __init__(self, inputFeed):
        processFeed = copy.deepcopy(inputFeed)
        processQ = Queue()
        for process in processFeed:
            processQ.add(process)

        self.arrivalQueue = processQ
        self.waitingQueue = Queue()
        self.clock = -1
        self.currentProcess = None
        self.finishedArray = []

    def isFinished(self):
        return self.arrivalQueue.isEmpty() and self.waitingQueue.isEmpty() and self.currentProcess is None

    def getAvgTurnaroundTime(self):
        assert(self.isFinished())
        totalTurnaroundTime = 0
        for process in self.finishedArray:
            totalTurnaroundTime += process.getTurnAroundTime()

        avgTurnaroundTime = totalTurnaroundTime / len(self.finishedArray)
        return avgTurnaroundTime

    def getAvgWaitingTime(self):
        assert(self.isFinished())
        totalWaitingTime = 0
        for process in self.finishedArray:
            totalWaitingTime += process.getWaitingTime()

        avgWaitingTime = totalWaitingTime / len(self.finishedArray)
        return avgWaitingTime

    def getThroughput(self):
        assert(self.isFinished())
        throughput = len(self.finishedArray) / self.clock
        return throughput
