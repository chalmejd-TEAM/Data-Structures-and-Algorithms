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
    # While current_node is not None and position is less than the index
    while (current_node != None and position+1 != index):
        position = position+1 # Add 1 to postion 
        current_node = current_node.next # move current node to next node in line

    # If current node exists
    if current_node != None: 
        new_node = Node(data) # Create new node with given data
        new_node.next = current_node.next # Set new node next to current node next
        current_node.next = new_node # Set current node next to new node
    else:
        print("Index is not present") # If current node does not exist print error message

def update(self, val, index):
    current_node = self.head # Set current node to head node
    position = 0 # Set initial position index to 0
    # If position is equal to index, set current node data to provided value
    if position == index:
        current_node.data = val
    # Else start traversing the list until target index is reached
    else:
        # Loop through list while current node exists and until position equals provided index
        while(current_node != None and position != index):
            position = position+1 # Increment position
            current_node = current_node.next # Move current node to next node

        # If current node exists, update its value to the provided value    
        if current_node != None:
            current_node.data = val
        else:
            print("Index not present") # Else print error message

def remove_first(self):
    # Check if head does not exist, and return if head not present
    if(self.head == None):
        return
    # Set head to node pointed to by the next of the the current head
    self.head = self.head.next


