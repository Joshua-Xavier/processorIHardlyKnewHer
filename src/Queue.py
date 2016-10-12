class Queue:

    def __init__(self):
        self.queue = []

    def serve(self):
        if not self.isEmpty:
            return self.queue.pop()
        else:
            print("Queue is empty!")
            print(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def add(self, item):
        self.queue.insert(0, item) #inserts item at the start of the queue
        print(self.queue)
