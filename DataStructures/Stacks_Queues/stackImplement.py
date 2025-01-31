# Define Node class with given data and initial next value set to None
class Node:
    # Initialize Node with data set to given data, and next set to None
    def __init__(self, data):
        self.data = data
        self.next = None

# Define Stack Class
class Stack:
    # Initialize Stack with top and bottom set to None
    def __init__(self):
        self.top = None
        self.length = 0

    def peek(self):
        if (self.top):
            print(self.top.data)
        else:
            print('Stack Empty')

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            self.length = self.length+1
            return
        else:
            new_node.next = self.top
            self.top = new_node
            self.length = self.length+1

    def pop(self):
        if self.top == None:
            return
        self.top = self.top.next
        self.length = self.length-1

    def stackSize(self):
        print(self.length)

myStack = Stack()

myStack.peek()
myStack.push('google')
myStack.push('bing')
myStack.push('microsoft')
myStack.stackSize()

myStack.peek()

myStack.pop()
myStack.peek()
myStack.stackSize()

myStack.pop()
myStack.peek()

myStack.pop()
myStack.peek()
myStack.stackSize()