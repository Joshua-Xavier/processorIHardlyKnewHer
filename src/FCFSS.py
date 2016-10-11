
def firstComeFirstServeScheduling(processFeed):
    # Implements first come first serve type scheduling

    processFeed.sort(key=lambda x:x[1]) #sorts by arrival time
    
