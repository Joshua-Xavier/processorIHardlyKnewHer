'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 11/10/16
LAST MODIFIED: 15/10/16
DESCRIPTION: This scheduler inherits from the original Scheduler class and extends
it with a unique tick function. It's tick function replicates the scheduling of
processes via a First Come First Serve Scheduling method.
'''

from src.Queue import Queue
from src.Scheduler import Scheduler
import copy

class firstComeFirstServeScheduler(Scheduler):

    def tick(self):
        '''
        In first come first serve scheduling, the processes are served based
        on arrival time and complete completely before moving on to the next one.
        '''
        if self.currentProcess is not None:
            if (self.clock > self.currentProcess.getArrivalTime()):
                self.currentProcess.incrementTimeSpentExecuting(1)
                print("Time " + str(self.clock - 1) + "-" + str(self.clock) + ": " + self.currentProcess.getID() + " exec " + str(self.currentProcess.getTimeSpentExecuting()) + "/" + str(self.currentProcess.getDuration()))

            if (self.currentProcess.isFinished()):
                self.currentProcess.calculateTurnAroundTime(self.clock)
                self.currentProcess.calculateWaitingTime(self.clock)
                self.finishedArray.append(self.currentProcess)
                self.currentProcess = None
                
        self.clock += 1

        '''
        The following checks the arrival queue after each tick to see if any
        processes in the arrival queue have reached their arrival time. If they
        have then they are added to the waiting queue and removed from the
        arrival queue. It has to be a while loop because in some cases there
        will be multiple processes in the arrival queue with the same arrival
        time so we want to add all of them.
        '''
        if (not self.arrivalQueue.isEmpty()):
            nextProcess = self.arrivalQueue.peek()
            while (nextProcess.getArrivalTime() == self.clock):
                p = self.arrivalQueue.serve()
                self.waitingQueue.add(p)
                if (not self.arrivalQueue.isEmpty()):
                    nextProcess = self.arrivalQueue.peek()
                else:
                    break

        '''
        If the waiting queue is not empty and there is no current process
        executing, then the current process should be grabbed from the waiting
        queue
        '''
        if not self.waitingQueue.isEmpty():
            if (self.currentProcess is None):
                self.currentProcess = self.waitingQueue.serve()

        '''
        Then we incrmenet the time spent executing of a process by 1
        and if the process happens to be finished then calculate turnaround time,
        waiting time and add the process to the finished array.
        '''
