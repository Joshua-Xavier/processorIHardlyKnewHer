
def firstComeFirstServeScheduling(processFeed):
    # Implements first come first serve type scheduling

    processFeed.sort(key=lambda x:x[1]) #sorts by arrival time
    clock = 0 #system clock starts at 0

    processQ = Queue()
    for process in processFeed:
        processQ.put(process) #add the processes to the Q


    while not processQ.empty():
        current_process = processQ.get()
        clock += current_process[2] #add process time to clock
        current_process[5] = current_process[2] #time spent executing is clock time
        current_process[]
