'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 11/10/16
LAST MODIFIED: 15/10/16
DESCRIPTION: This file handles the parsing of a processes.txt file found in an
input directory. It scans through the text file and returns an array of process
elements where:
    index[0] = process name
    index[1] = process arival time
    index[2] = process duration
    index[3] = turnaround time (defaults to -1)
    index[4] = waiting time (defaults to -1)
    index[5] = time spent executing (defaults to 0)

Or explained differently:
[name, arrival_time, duration, turnaround_time, waiting_time, time_spent]
'''

from src.Process import Process

def getData(filePath):
    '''
    Given a filepath getData opens that file, then parses through the lines
    one by one splitting the values into an array, then assigning them
    to a new process object. These process objects are added to an array
    and returned at the end.
    '''

    f = open(filePath, 'r')
    processArray = []
    for line in f:
        processItemArray = line.split()

        # There is a strong dependency here that the data be well formed as:
        #  Process ID  |  Arrival Time  | Duration
        current_process = Process()
        current_process.setID(processItemArray[0])
        current_process.setArrivalTime(int(processItemArray[1]))
        current_process.setDuration(int(processItemArray[2]))

        processArray.append(current_process)
    f.close()

    return processArray
