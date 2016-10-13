from src.Queue import Queue

def roundRobinScheduling(inputFeed):
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
        count = 0

        while (count <= 2 and not current_process.isFinished()):
            current_process.incrementTimeSpentExecuting(1)
            count += 1

        clock += count

        if current_process.isFinished():
            current_process.calculateTurnAroundTime(clock)
            current_process.calculateWaitingTime(clock)
            finishedArray.append(current_process)
        else:
            processQ.add(current_process)




    return finishedArray
