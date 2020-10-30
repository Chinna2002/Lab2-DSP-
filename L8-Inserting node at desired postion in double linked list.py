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

    # Method to Print Nodes of Linked List
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next


    # Method to insert at middle
    def addDesired(self, key, data):
        new_node = Node(data)
        cur = self.head
        while cur.next:
            nxt = cur.next
            if cur.data == key:
                cur.next = new_node
                new_node.prev = cur
                new_node.next = nxt
                nxt.prev = new_node
            cur = cur.next


dll = DoublyLinkedList()
n = int(input("Enter the size of the Double linked list : "))
print("Enter the elements of the linked list")
for i in range(n):
    dll.append(input())

print("The old double linked list : ")
dll.print_list()
print()
k = input("Enter the node after which we should add the node : ")
h = input("Enter the new node : ")
dll.addDesired(k, h)
print("The updated linked list is : ")
dll.print_list()






