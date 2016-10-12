
def firstComeFirstServeScheduling(processFeed):
    # Implements first come first serve type scheduling

    processFeed.sort(key=lambda x:x[1]) #sorts by arrival time
    clock = 0 #system clock starts at 0

    processQ = Queue()
    for process in processFeed:
        processQ.put(process) #add the processes to the Q

    finishedArray = []
    while not processQ.empty():
        current_process = processQ.get()
        clock += current_process.getDuration() #add process time to clock
        current_process.setTimeSpentExecuting(current_process.getDuration())
        current_process.calculateTurnAroundTime(clock)
        current_process.calculateWaitingTime(clock)

        finishedArray.append(current_process)

    return finishedArray
