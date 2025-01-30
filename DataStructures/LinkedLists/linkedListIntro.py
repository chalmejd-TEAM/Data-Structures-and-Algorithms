# List/Array:
basket = ['apples', 'grapes', 'pears']

# Linked List pseudo code:
# -----------------------------------------
# linked list: apples --> grapes --> pears
# more accurate diagram:
# apples
# 8947   -->  grapes
#             8742  -->   pears
#                         372    -->  null

# Creating a linked list 10-->5-->16
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def prepend(self, data):
    new_node = Node(data) # Create new node with given data
    # Check if the head is an empty node, if empty make new node the head and return
    if self.head is None:
        self.head = new_node
        return
    # Else insert the head at the next new node and make the head equal to the new node
    else:
        new_node.next = self.head
        self.head = new_node

def append(self, data):
    new_node = Node(data) # Create new node with given data
    # Check if head is an empty node, if empty make new node the head and return
    if self.head is None:
        self.head = new_node
        return
    
    # Else we make current_node equal to the head and traverse to the last node
    # While loop breaks when current_node.next is None
    current_node = self.head
    while(current_node.next):
        current_node = current_node.next
    # Set current_node.next to new_node making it last node of linked list
    current_node.next = new_node

def insert(self, data, index):
    # If index is 0, prepend the node and return
    if (index == 0):
        self.prepend(data)
        return
    
    position = 0 # Set initial position index to 0
    current_node = self.head # Set current_node to head node
    