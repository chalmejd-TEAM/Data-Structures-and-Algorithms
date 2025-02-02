#       9
#   4        20
# 1   6   15   170

# Binary tree node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root
            while currentNode.value != newNode:
                if newNode.value > currentNode.value:
                    if currentNode.right:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = newNode
                        break
                elif newNode.value < currentNode.value:
                    if currentNode.left:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = newNode
                        break
                else:
                    break
    def lookup(self, value):
        currentNode = self.root
        while True:
            if currentNode.value == value:
                print('Value:', currentNode.value, '\nLeft:', currentNode.left.value, '\nRight:', currentNode.right.value)
                break
            elif currentNode.value > value:
                currentNode = currentNode.left
            elif currentNode.value < value:
                currentNode = currentNode.right


myTree = BinarySearchTree()

myTree.insert(9)
myTree.insert(20)
myTree.insert(4)
myTree.insert(15)
myTree.insert(1)
myTree.insert(6)
myTree.insert(170)
myTree.lookup(20)


