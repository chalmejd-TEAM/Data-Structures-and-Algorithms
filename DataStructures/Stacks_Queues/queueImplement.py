# Define Node class with given data and initial next value set to None
class Node:
    # Initialize Node with data set to given data, and next set to None
    def __init__(self, data):
        self.data = data
        self.next = None

# Define Queue Class
class Queue:
    # Initialize Queue with first and last set to None
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if (self.first):
            print(self.first.data)
        else:
            print('Queue Empty')

    def enqueue(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length = self.length+1

    def dequeue(self):
        if self.first == None:
            return
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length = self.length-1

    def queueSize(self):
        print('Queue size:', self.length)

myQueue = Queue()

myQueue.enqueue(1)
myQueue.peek()
myQueue.enqueue(2)
myQueue.peek()
myQueue.queueSize()
myQueue.enqueue(3)
myQueue.peek()
myQueue.queueSize()

myQueue.dequeue()
myQueue.peek()
myQueue.dequeue()
myQueue.peek()
myQueue.dequeue()
myQueue.peek()

