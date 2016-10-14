from src.Queue import Queue
import copy

class shortestRemainingTimeScheduler:

    def __init__(self, inputFeed):
        processFeed = copy.deepcopy(inputFeed)
        processQ = Queue()
        for process in processFeed:
            processQ.add(process)

        self.arrivalQueue = processQ
        self.waitingQueue = Queue()
        self.clock = 0
        self.currentProcess = None

    def tick():
        self.clock += 1
        for process in self.arrivalQueue.queue:
            if process.getArrivalTime() == self.clock:
                self.waitingQueue.add(process)

        self.waitingQueue.queue.sort(key=lambda x:x.getRemainingTime())

        if self.currentProcess is None:
            self.currentProcess = self.waitingQueue.serve()

        self.currentProcess.incrementTimeSpentExecuting(1)
        if ()
