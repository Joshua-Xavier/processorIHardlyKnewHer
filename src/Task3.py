'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 11/10/16
LAST MODIFIED: 14/10/16
DESCRIPTION:
'''

from src.Queue import Queue
from src.Scheduler import Scheduler
import copy

class shortestRemainingTimeScheduler(Scheduler):

    def tick(self):
        self.clock += 1
        remArray = []

        for i in range(self.arrivalQueue.getLength()):
            process = self.arrivalQueue.queue[i]
            if process.getArrivalTime() == self.clock:
                self.waitingQueue.add(process)
                remArray.append(i)
                self.waitingQueue.remainingTimeSort()

                if (self.currentProcess is not None):
                    if (self.waitingQueue.peek().getRemainingTime() < self.currentProcess.getRemainingTime()):
                        self.waitingQueue.add(self.currentProcess)
                        self.currentProcess = self.waitingQueue.serve()
                        self.waitingQueue.remainingTimeSort()

        for index in remArray:
            self.arrivalQueue.remove(index)


        if not self.waitingQueue.isEmpty(): #this is issue
            if (self.currentProcess is None):
                self.currentProcess = self.waitingQueue.serve()

        if self.currentProcess is not None:
            if (self.clock > self.currentProcess.getArrivalTime()):
                self.currentProcess.incrementTimeSpentExecuting(1)


            if (self.currentProcess.isFinished()):
                self.currentProcess.calculateTurnAroundTime(self.clock)
                self.currentProcess.calculateWaitingTime(self.clock)
                self.finishedArray.append(self.currentProcess)
                self.currentProcess = None
