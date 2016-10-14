'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 11/10/16
LAST MODIFIED: 11/10/16
DESCRIPTION:
'''

class Queue:

    def __init__(self):
        self.queue = []
        self.qLength = 0

    def isEmpty(self):
        return self.qLength == 0

    def serve(self):
        if not self.qLength == 0:
            self.qLength -= 1
            return self.queue.pop(0)
        else:
            print("Queue is empty!")

    def add(self, item):
        self.queue.append(item) #inserts item at the end of the queue
        self.qLength += 1

    def peek(self):
        # returns a shallow copy of the next item in queue to be serviced
        return self.queue[0]

    def getLength(self):
        return self.qLength

    def remove(self, index):
        del self.queue[index]
        self.qLength -= 1
