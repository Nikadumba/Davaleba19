

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def remove_value(self, value):
        current_node = self.head
        previous_node = None

        while current_node and current_node.data != value:
            previous_node = current_node
            current_node = current_node.next

        if current_node:
            if previous_node:
                previous_node.next = current_node.next
            else:
                self.head = current_node.next

    def display_info(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()


linked_list = LinkedList()

linked_list.append(5)
linked_list.append(10)
linked_list.append(2)
linked_list.append(43)
linked_list.append(21)
linked_list.append(0)

linked_list.display_info()

linked_list.remove_value(43)
linked_list.display_info()
