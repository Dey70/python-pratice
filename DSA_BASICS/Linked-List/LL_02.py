"""

🏋️‍♂️ Exercise: Build and Print a Linked List
🎯 Your Goal:
Create a linked list with 3 nodes containing the values:
11, 22, and 33, in that order.

You should:

Create a Node class

Create a LinkedList class with:

a constructor (__init__)

a print_list() method

Manually link the nodes (no append() method for now)

Call print_list() to print the values
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end = "->")
            temp = temp.next
        print("None")

my_linked_list = LinkedList(11)
my_linked_list.tail.next = Node(22)
my_linked_list.tail = my_linked_list.tail.next
my_linked_list.tail.next = Node(33)
my_linked_list.tail = my_linked_list.tail.next

my_linked_list.print_list()