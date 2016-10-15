'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 13/10/16
LAST MODIFIED: 15/10/16
DESCRIPTION: An implementation of a queue object with a few additional features.
The queue is used for the scheduling algorithms, both the waiting and arrival
queues.
'''

class Queue:

    def __init__(self):
        '''
        Initiation of queue object sets up qlength variable as well
        as the queue array that will hold the elements
        '''
        self.queue = []
        self.qLength = 0

    def isEmpty(self):
        return self.qLength == 0

    def serve(self):
        '''
        Serve returns the next element in the queue (element 0),
        it is worth noting in this queue implementation the next to be served
        is at index 0. If the queue is not empty it will decrement the queue
        length variable and return the element, removing it from the queue.
        '''
        if not self.qLength == 0:
            self.qLength -= 1
            return self.queue.pop(0)
        else:
            print("Queue is empty!")

    def add(self, item):
        '''
        Adds an item to the queue, it is added at the last position, so by
        default it will be the least priority
        '''
        self.queue.append(item) #inserts item at the end of the queue
        self.qLength += 1

    def peek(self):
        '''
        In terms of checking an arrival queue for instance, it becomes useful
        to be able to query the next item in a queue without actually taking
        it out of the queue (to check whether it is it's time to arrive for
        instance). Because of this, peek returns a copy of the next item in the
        queue that can be used to check properties of it, without actually removing
        it from the queue.
        '''
        # returns a shallow copy of the next item in queue to be serviced
        return self.queue[0]

    def getLength(self):
        return self.qLength

    def remove(self, index):
        '''
        To make this unneccesary could just have a loop where you go
        while (nextElement.getDuration == current clock time)
            queue.pop --> waitingQueue
        '''

        del self.queue[index]
        self.qLength -= 1

    def remainingTimeSort(self):
        '''
        In a waiting queue in the shortest remaining time scheduler implementation
        it became necessary to have a queue that is a priority queue, based on
        lowest remaining time. Calling this sort function will sort the queue
        to ensure the element to be served next is the one with the shortest
        time remaining.
        '''
        #sorts queue by remaining time using a lambda function
        self.queue.sort(key=lambda x:x.getRemainingTime())
