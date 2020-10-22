#Finding biggest and smallest element in doubly linked list
print("121910313006","Kadiyala Rohit Bharadwaj")
# Defining the Node class
class Node:
    def __init__(self, data):  # Constructor for Node class
        self.data = data
        self.prev = None
        self.next = None


# Definind the Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to append new nodes
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    # Method to find min and max Nodes of Linked List
    def minmax(self):
        cur = self.head
        min = None
        max = None
        while cur:
            if min == None or cur.data < min:
                min = cur.data
            if max == None or cur.data > max:
                max = cur.data
            cur = cur.next
        return (min, max)


dll = DoublyLinkedList()
n = int(input("Enter the size of the linked list : "))
print("Enter the elements of the linked list:")
for i in range(n):
    dll.append(int(input("Enter Element:")))

value = dll.minmax()
print("The smallest element of the Doubly linked list : ", value[0])
print("The largest element of the Doubly linked list : ", value[1])
