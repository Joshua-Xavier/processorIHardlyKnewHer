'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 11/10/16
LAST MODIFIED: 11/10/16
DESCRIPTION:
'''
from src.Queue import Queue
import copy

def shortestRemainingTimeScheduling(inputFeed):

    processFeed = copy.deepcopy(inputFeed)

    processFeed.sort(key=lambda x:x.getArrivalTime()) #sorts by arrival time
    clock = 0 #system clock starts at 0

    processQ = Queue()
    for process in processFeed:
        processQ.add(process) #add the processes to the Q

    finishedArray = []

    while not processQ.isEmpty():
        nextProcess = processQ.peek()
        nextProcessTime = nextProcess.getArrivalTime()
        print(processQ.queue)
        while (clock < nextProcessTime):
            # Don't work with a process until the clock has reached it's arrival time
            clock += 1

        current_process = processQ.serve()
        print(processQ.queue)
        nextProcess = processQ.peek()
        nextProcessTime = nextProcess.getArrivalTime()
        print(processQ.queue)

        while (not current_process.isFinished()):
            clock += 1
            current_process.incrementTimeSpentExecuting(1)

            if (current_process.isFinished()):
                current_process.calculateTurnAroundTime(clock)
                current_process.calculateWaitingTime(clock)
                finishedArray.append(current_process)
            elif (clock == nextProcessTime):
                if (nextProcess.getRemainingTime() < current_process.getRemainingTime()):
                    processQ.add(current_process) #add current process back because other process has shorter duration

        return finishedArray
