from src.Queue import Queue

def roundRobinScheduling(processFeed):
    # Implements first come first serve type scheduling

    processFeed.sort(key=lambda x:x.getArrivalTime()) #sorts by arrival time
    clock = 0 #system clock starts at 0

    processQ = Queue()
    for process in processFeed:
        processQ.add(process) #add the processes to the Q

    finishedArray = []
    while not processQ.isEmpty():

        current_process = processQ.serve()
        clock += 2 #a time quantum elapses
        current_process.setTimeSpentExecuting(current_process.getDuration())
        current_process.calculateTurnAroundTime(clock)
        current_process.calculateWaitingTime(clock)

        finishedArray.append(current_process)

    return finishedArray
