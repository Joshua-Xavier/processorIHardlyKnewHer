'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 14/10/16
LAST MODIFIED: 15/10/16
DESCRIPTION: This creates a base class that each of the scheduling algorithms
will inherit from, it defines common tasks like the initiation as well as
the methods that return avg turnaround time, waiting time and throughput of the
scheduling methods.
'''

from src.Queue import Queue
import copy

class Scheduler:

    def __init__(self, inputFeed):
        '''
        In the initiation of a scheduler we set up the variables that will
        be needed, it takes a process feed as input so it can work with a
        group of processes, note that it copies the feed so that it doesn't
        change the feed for other schedulers. It also creates two queues,
        the arrival queue, which stores processes for which their arrival time
        has not yet occured, and the waiting queue which is where the processes
        that have arrived go.
        '''

        processFeed = copy.deepcopy(inputFeed)
        processFeed.sort(key=lambda x:x.getArrivalTime())
        processQ = Queue()
        for process in processFeed:
            processQ.add(process)

        self.arrivalQueue = processQ
        self.waitingQueue = Queue()

        self.clock = -1 # clock starts from -1 because the start of a tick method
                        # always increments the clock at the start, so it will
                        # effectively start from 0

        self.currentProcess = None
        self.finishedArray = [] # processes that have finished get put here to be returned at the end
        self.count = 0 #used for prememption if needed, such as in RRS when the time slice is 2

    def isFinished(self):
        '''
        useful to know when a sheduler is done processing all the processes,
        this has a few elements, but essentially we know the scheduler is done
        only when both the queues are empty, and there is no current process
        '''
        return self.arrivalQueue.isEmpty() and self.waitingQueue.isEmpty() and self.currentProcess is None

    def getAvgTurnaroundTime(self):
        '''
        After asserting the scheduler is finished, it goes through each process
        in the finished array and increments the total turnaround time
        by the current processes turnaround time. It then divides this total by
        the number of processes to get the average turnaround time
        '''
        assert(self.isFinished())
        totalTurnaroundTime = 0
        for process in self.finishedArray:
            totalTurnaroundTime += process.getTurnAroundTime()

        avgTurnaroundTime = totalTurnaroundTime / len(self.finishedArray)
        return avgTurnaroundTime

    def getAvgWaitingTime(self):
        '''
        After asserting the scheduler is finished, it goes through each process
        in the finished array and increments the total waiting time
        by the current processes waiting time. It then divides this total by
        the number of processes to get the average waiting time
        '''
        assert(self.isFinished())
        totalWaitingTime = 0
        for process in self.finishedArray:
            totalWaitingTime += process.getWaitingTime()

        avgWaitingTime = totalWaitingTime / len(self.finishedArray)
        return avgWaitingTime

    def getThroughput(self):
        '''
        After asserting the scheduler is finished it calculates the throughput,
        the throughput is the number of processes completed per second,
        since we know the clock wont be incremented after all the processes are
        done, this is simply the number of processes divided by the clock (since
        every process in the finished array must be finished).
        '''
        assert(self.isFinished())
        throughput = len(self.finishedArray) / self.clock
        return throughput
