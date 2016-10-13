class Queue:

    def __init__(self):
        self.queue = []
        self.qLength = 0

    def isEmpty(self):
        return self.qLength == 0

    def serve(self):
        if not self.qLength == 0:
            self.qLength -= 1
            return self.queue.pop()
        else:
            print("Queue is empty!")

    def add(self, item):
        self.queue.insert(0, item) #inserts item at the start of the queue
        self.qLength += 1
