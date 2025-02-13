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

# Define Node class with given data and initial next value set to None
class Node:
    # Initialize Node with data set to given data, and next set to None
    def __init__(self, data):
        self.data = data
        self.next = None

# Define Linked List Class
class LinkedList:
    # Initialize linked list with head set to None
    def __init__(self):
        self.head = None

    # Method to prepend data to the LL
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

    # Method to append data to the LL
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

    # Method to insert data at given index to the LL
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

    # Method to update value at given index of LL
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

    # Method to remove first value of LL
    def remove_first(self):
        # Check if head does not exist, and return if head not present
        if(self.head == None):
            return
        # Set head to node pointed to by the next of the the current head
        self.head = self.head.next

    # Method to remove last value of LL
    def remove_last(self):
        # If list is empty return while doing nothing
        if self.head is None:
            return
        
        current_node = self.head # Set current node variable to the head node
        # While two nodes after current node exist
        while (current_node.next != None and current_node.next.next != None):
            # Set current node to next node
            current_node = current_node.next
        # Set next value of current node to None
        current_node.next = None

    # Method to remove value at given index of LL
    def remove(self, index):
        # If list is empty return and do nothing
        if self.head is None:
            return
        
        current_node = self.head # Set current node to first node in list
        position = 0 # Set position index to 0

        # If given index is 0 use remove_first function
        if index == 0:
            self.remove_first()
        # Else start traversing the list
        else:
            # While current node exists and position is less than the given index minus 1
            while current_node != None and position < index - 1:
                # Increment position and move current node to the next in the list
                position += 1
                current_node = current_node.next
            
            # If the current node or next node is none return error
            if current_node is None or current_node.next is None:
                print("Index is not present")
            # Else set the next value for the current node to the next value of the next node
            else:
                current_node.next = current_node.next.next

    # Method to remove data from LL that matches given data
    def remove_data(self, data):
        current_node = self.head # Set current node to first item in list

        # Check if head node contains the specified data
        if current_node.data == data:
            # if true run remove_first function and return
            self.remove_first()
            return
        # Traverse the node while it exists and next node data does not equal given data
        while current_node != None and current_node.next.data != data:
            current_node = current_node.next

        # If current node is does not exist do nothing and return
        if current_node is None:
            return
        # Else set current node next to the next value of the next node
        else:
            current_node.next = current_node.next.next

    # Print the LL
    def printLL(self):
        current_node = self.head # Set current node to first node in list
        # Traverse the list and print the data from each node while current node exists
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    # Print the size of the LL
    def sizeLL(self):
        size = 0 # Set initial size to 0
        # If list has head node
        if(self.head):
            current_node = self.head # Set current node to first item in list
            # Traverse the list while incrementing size variable while current node exists
            while(current_node):
                size = size + 1
                current_node = current_node.next
            return size # Return size value after while loop
        # if list is empty return 0
        else:
            return 0

# Create a new linked list
llist = LinkedList()

# Add nodes to the linked list
llist.append('a')
llist.append('b')
llist.prepend('c')
llist.append('d')
llist.insert('g', 2)

# Print the linked list
print('Node Data:')
llist.printLL()

# Remove nodes form the linked list
print("\nRemove First Node:")
llist.remove_first()
llist.printLL()

print("\nRemove Last Node:")
llist.remove_last()
llist.printLL()

print("\nRemove Node at Index 1:")
llist.remove(1)
llist.printLL()

# Print the LL after all removals
print("\nLinked list after removing nodes:")
llist.printLL()

# Update node at index 0 to 'z' and print the LL
print("\nUpdate node Value at Index 0:")
llist.update('z', 0)
llist.printLL()

# Print the size of the LL
print("\nSize of linked list:", llist.sizeLL())
