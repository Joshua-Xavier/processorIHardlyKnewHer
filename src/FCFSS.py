from src.Queue import Queue

def firstComeFirstServeScheduling(processFeed):
    # Implements first come first serve type scheduling

    processFeed.sort(key=lambda x:x.getArrivalTime()) #sorts by arrival time
    clock = 0 #system clock starts at 0

    processQ = Queue()
    for process in processFeed:
        processQ.add(process) #add the processes to the Q

    finishedArray = []
    while not processQ.isEmpty():
        print("val")
        current_process = processQ.serve()
        clock += current_process.getDuration() #add process time to clock
        current_process.setTimeSpentExecuting(current_process.getDuration())
        current_process.calculateTurnAroundTime(clock)
        current_process.calculateWaitingTime(clock)

        finishedArray.append(current_process)

    return finishedArray
