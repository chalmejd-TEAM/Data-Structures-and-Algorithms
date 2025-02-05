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
            while True:
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
        if (self.root):
            currentNode = self.root
            while currentNode:
                if currentNode.value == value:
                    print('Value:', currentNode.value)
                    if currentNode.left:
                        print('Left:', currentNode.left.value)
                    if currentNode.right:
                        print('Right:', currentNode.right.value)
                    return
                elif currentNode.value > value:
                    currentNode = currentNode.left
                elif currentNode.value < value:
                    currentNode = currentNode.right
            print('Does not exist')
        else:
            print('Tree is empty')

    def remove(self, value):
        if (self.root):
            currentNode = self.root
            parentNode = None
            while currentNode:
                if value < currentNode.value:
                    parentNode = currentNode
                    currentNode = currentNode.left
                elif value > currentNode.value:
                    parentNode = currentNode
                    currentNode = currentNode.right
                elif currentNode.value == value:
                    # No right child
                    if currentNode.right == None:
                        if parentNode == None:
                            self.root = currentNode.left
                        else:
                            # If parent > current value, make current left child a left child of parent
                            if currentNode.value < parentNode.value:
                                parentNode.left = currentNode.left
                            # If parent < current value, make left child a right child of parent
                            elif currentNode.value > parentNode.value:
                                parentNode.right = currentNode.left
                    # Right child with no left child
                    elif currentNode.right.left == None:
                        currentNode.right.left = currentNode.left
                        if (parentNode == None):
                            self.root = currentNode.right
                        else:
                            # If parent > current, make right child of the left the parent
                            if currentNode.value < parentNode.value:
                                parentNode.left = currentNode.right
                            # If parent < current, make right child a right child of the parent
                            elif currentNode.value > parentNode.value:
                                parentNode.right = currentNode.right
                    # Right child that has left child
                    else:
                        leftmost = currentNode.right.left
                        leftmostParent = currentNode.right
                        while(leftmost.left != None):
                            leftmostParent = leftmost
                            leftmost = leftmost.left

                        leftmostParent.left = leftmost.right
                        leftmost.left = currentNode.left
                        leftmost.right = currentNode.right

                        if parentNode == None:
                            self.root = leftmost
                        else:
                            if currentNode.value < parentNode.value:
                                parentNode.left = leftmost
                            elif currentNode.value > parentNode.value:
                                parentNode.right = leftmost
                        return True

            print('Does not exist')
        else:
            print('Tree is empty')
    
    def bfs(self):
        currentNode = self.root
        list = []
        queue = []
        queue.append(currentNode)
        
        while(len(queue) > 0):
            currentNode = queue.pop(0)
            list.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return list
    
    def bfsR(self, queue, list):
        if len(queue) == 0:
            return list
        currentNode = queue.pop(0)
        list.append(currentNode.value)
        if currentNode.left:
                queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        return self.bfsR(queue, list)
    





myTree = BinarySearchTree()

myTree.insert(9)
myTree.insert(20)
myTree.insert(4)
myTree.insert(15)
myTree.insert(1)
myTree.insert(6)
myTree.insert(170)
myTree.lookup(20)

ans = myTree.bfs()
print(ans)

ansR = myTree.bfsR([myTree.root], [])
print(ansR)





