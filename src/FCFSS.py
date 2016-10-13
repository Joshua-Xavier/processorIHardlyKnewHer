from src.Queue import Queue
import copy

def firstComeFirstServeScheduling(inputFeed):
    # Implements first come first serve type scheduling

    processFeed = copy.deepcopy(inputFeed)

    processFeed.sort(key=lambda x:x.getArrivalTime()) #sorts by arrival time
    clock = 0 #system clock starts at 0

    processQ = Queue()
    for process in processFeed:
        processQ.add(process) #add the processes to the Q

    finishedArray = []
    while not processQ.isEmpty():

        nextProcessTime = processQ.peek()
        while (clock < nextProcessTime):
            # Don't work with a process until the clock has reached it's arrival time
            clock += 1

        current_process = processQ.serve()
        clock += current_process.getDuration() #add process time to clock
        current_process.incrementTimeSpentExecuting(current_process.getDuration())
        current_process.calculateTurnAroundTime(clock)
        current_process.calculateWaitingTime(clock)

        finishedArray.append(current_process)

    return finishedArray
