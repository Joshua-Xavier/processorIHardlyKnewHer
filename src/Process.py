'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 11/10/16
LAST MODIFIED: 15/10/16
DESCRIPTION: The following is a process object that became a useful datatype to
create for the managing of process data, it holds their identifiers, arrival
times, durations, turnaround times, waiting times and time spent executing and
does the calculations to produce these.
'''

class Process:

    def __init__(self):
        '''
        Initiation sets up the variables, note that the values all have
        defaults that don't make sense such as -1, so that if they
        aren't calculated correctly it will be obvious in debugging
        '''
        self.id = ''
        self.arrivalTime = -1
        self.duration = -1
        self.turnAroundTime = -1
        self.waitingTime = -1
        self.timeSpentExecuting = 0


    ## --GETTERS--
    def getID(self):
        return self.id

    def getArrivalTime(self):
        return self.arrivalTime

    def getDuration(self):
        return self.duration

    def getTurnAroundTime(self):
        return self.turnAroundTime

    def getWaitingTime(self):
        return self.waitingTime

    def getTimeSpentExecuting(self):
        return self.timeSpentExecuting

    def getRemainingTime(self):
        '''
        The remaining time of a process is just it's duration minus the time
        its already spent executing
        '''
        return self.duration - self.timeSpentExecuting

    ## --SETTERS--
    def setID(self, newID):
        self.id = newID

    def setArrivalTime(self, newArrivalTime):
        self.arrivalTime = newArrivalTime

    def setDuration(self, newDuration):
        self.duration = newDuration

    def incrementTimeSpentExecuting(self, time_increment):
        '''
        More useful and less prone to mistakes to have the ability to increment
        rather than explicitly set the time spent executing
        '''
        self.timeSpentExecuting += time_increment

    ## --METHODS--
    def isFinished(self):
        '''
        Probs need to reimplement as well
        '''
        #process will only be complete when the time spent executing
        # is equal to the duration of time the process needs
        if self.timeSpentExecuting >= self.duration:
            self.timeSpentExecuting = self.duration
            return True
        else:
            return False

    def calculateTurnAroundTime(self, finishTime):
        '''
        calculates the turnaround time for a process, the turnaround time is
        defined as the time between a process arriving and finishing. It is
        fed a finishTime, which is just the clock value integer at its time
        of finishing
        '''
        assert(self.isFinished()) #for more safety and bug finiding, can only
        # calculate the turnaround time if the process is finished
        self.turnAroundTime = finishTime - self.arrivalTime

    def calculateWaitingTime(self, finishTime):
        '''
        similar to the above, this calculates the waiting time for a process,
        the waiting time is defined as the time spent after a process arrives
        waiting, so it is calculated via the finish time, minus the arrival time,
        minus the duration. In other words, the waiting time = turnaround time
        minus duration, because any time spent not executing must be time it was
        waiting.
        '''
        assert(self.isFinished())
        self.waitingTime = finishTime - self.arrivalTime - self.duration

    def stringify(self):
        '''
        A method that returns an array of the values of the process for printing
        purposes, useful for debugging or if you want to see the states of
        the processes at each stage
        '''
        return [self.id, self.arrivalTime, self.duration, self.turnAroundTime, self.waitingTime, self.timeSpentExecuting]
