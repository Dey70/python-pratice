class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
    
    #Creating Nodes
    node1 = Node(10)
    node1 = Node(20)
    node1 = Node(30)
    node1 = Node(40)
    
    #Conecting nodes to the linked list
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    #Printing the nodes
    current = node1
    while current is not None:
        print(current.next, end = "->")
        current = current.next
    print("None")