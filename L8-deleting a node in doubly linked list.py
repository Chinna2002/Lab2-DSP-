#Deleting the nodes in Double linked list
print("121910313006","Kadiyala Rohit Bharadwaj")
# Defining the Node class
class Node:
    def __init__(self,data): # Constructor for Node class
        self.data = data
        self.prev = None
        self.next = None

# Definind the Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to append new nodes
    def append(self,data):
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
            print(cur.data, end = ' ')
            cur = cur.next
    
    # Method to delete nodes
    def delete(self,key):
        if self.head.data==key:
            nxt = self.head.next
            self.head = nxt
            nxt.prev = None
            return 
        cur = self.head
        while cur:
            if cur.data==key:
                prv = cur.prev
                nxt = cur.next
                prv.next = nxt
                if nxt != None: nxt.prev = prv
                cur = None
                return
            cur = cur.next
        

    

dll = DoublyLinkedList()
n = int(input("Enter the size of the linked list : "))
print("Enter the elements of the linked list")
for i in range(n):
    dll.append(input())

print("The old linked list : ")
dll.print_list()
print()
k = input("Enter the node after which we should delete: ")
dll.delete(k)
print("The updated linked list is : ")
dll.print_list()
