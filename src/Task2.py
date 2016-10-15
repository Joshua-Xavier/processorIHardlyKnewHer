'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 11/10/16
LAST MODIFIED: 15/10/16
DESCRIPTION: This scheduler inherits from the original Scheduler class and extends
it with a unique tick function. It's tick function replicates the scheduling of
processes via a Round Robin Scheduling method.
'''

from src.Queue import Queue
from src.Scheduler import Scheduler
import copy

class roundRobinScheduler(Scheduler):

    def tick(self):
        '''
        In round robin scheduling, the processes are served for a given time
        slice then cycled around. The time slice in this case is 2. The order of
        priority in this implementation is: the longest waiting process, then a
        new arrival to the queue, then the currently executing process goes to
        the end of the queue
        '''
        self.clock += 1
        remArray = []

        '''
        The following checks the arrival queue after each tick to see if any
        processes in the arrival queue have reached their arrival time. If they
        have then they are added to the waiting queue and removed from the
        arrival queue
        '''
        for i in range(self.arrivalQueue.getLength()):
            process = self.arrivalQueue.queue[i]
            if process.getArrivalTime() == self.clock:
                self.waitingQueue.add(process)
                remArray.append(i)

        for index in remArray:
            self.arrivalQueue.remove(index)

        '''
        If the waiting queue is not empty and there is no current process
        executing, then the current process should be grabbed from the waiting
        queue
        '''
        if not self.waitingQueue.isEmpty(): #this is issue
            if (self.currentProcess is None):
                self.currentProcess = self.waitingQueue.serve()

        '''
        We increment the currently executing processes time spent executing
        and also increase the count, if the process is finished then we do its
        calculations and put it in the finished array. We also check if otherwise
        the count is equal to 2, in which case the current processes time slice
        has expired so it is added to the back of the waiting queue.
        '''
        if self.currentProcess is not None:
            if (self.clock > self.currentProcess.getArrivalTime()):
                self.currentProcess.incrementTimeSpentExecuting(1)
                self.count += 1

            if (self.currentProcess.isFinished()):
                self.currentProcess.calculateTurnAroundTime(self.clock)
                self.currentProcess.calculateWaitingTime(self.clock)
                self.finishedArray.append(self.currentProcess)
                self.currentProcess = None
                self.count = 0 # need to reset count for new process

            elif (self.count == 2):
                self.count = 0 #reset count
                self.waitingQueue.add(self.currentProcess)
                self.currentProcess = None
