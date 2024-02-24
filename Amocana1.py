
# Creating Node class for the linked list
class Node:
    def __init__(self, data):
        # Data of the node
        self.data = data  
        # next node of the list
        self.next = None  

# Creating LinkedList class
class LinkedList:
    def __init__(self):
        # Initializing empty list
        self.head = None

    # Appending new node
    def append(self, data):
        new_node = Node(data)
        
        # If the list is empty, new node will be the head
        if self.head is None: 
            self.head = new_node
            return

        # while there is next node, next node is considered as last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # Appending new node
        last_node.next = new_node

    # Inserting new node
    def insert(self, data, index):
        new_node = Node(data)
        
        # If the index is 0, inserting the new node at the beginning
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_index = 0
        # inserting node, while index is more than 0
        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        # Inserting new node
        new_node.next = current_node.next
        current_node.next = new_node

    # Removing the node from the list
    def remove(self, index):
        # If the index is 0, removing the head node
        if index == 0:
            self.head = self.head.next
            return
         
        current_node = self.head
        current_index = 0
        # removing node, while index more than 0
        while current_index < index - 1 and current_node.next:
            current_index += 1
            current_node = current_node.next

        # Removing the node
        if current_node.next:
            current_node.next = current_node.next.next

    # Displaying node of the list
    def display_info(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()


linked_list = LinkedList()

# Appending data to the linked list
linked_list.append(5)
linked_list.append(10)
linked_list.append(2)

# Displaying linked list
linked_list.display_info()

# Inserting data in the list
linked_list.insert(11, 1)
linked_list.insert(15, 2)

# Displaying linked list
linked_list.display_info()

# Removing node from the linked list
linked_list.remove(2)

# Displaying linked list
linked_list.display_info()



# Creating Node class for the stack
class Node:
    def __init__(self, data):
        # Data of the node
        self.data = data  
        # next node of the stack
        self.next = None  

# Creating Stack class
class Stack:
    def __init__(self):
        # Initializing an empty stack
        self.top_node = None  
        # Initializing the length of the stack
        self.length = 0  

    # Checking if the stack is empty
    def empty(self):
        return self.length == 0

    # Getting stack size
    def size(self):
        return self.length

    # Getting data of the top element
    def top(self):
        if not self.empty():
            return self.top_node.data
        else:
            raise IndexError("Stack Is Empty")

    # Pushing new element into the stack
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top_node
        self.top_node = new_node
        self.length += 1

    # Pop top of the stack
    def pop(self):
        if not self.empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.length -= 1
            return popped_item
        else:
            raise IndexError("Stack Is Empty")


stack = Stack()

# Displaying stack size
print(stack.size())

# Pushing elements into the stack
stack.push(1)
stack.push(5)
stack.push(10)

# Displaying new size of the stack
print(stack.size())

# Pop top of the stack
print(stack.pop())

# Displaying top of the stack
print(stack.top())

