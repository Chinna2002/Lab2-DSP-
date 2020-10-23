# Program to add at desired position in the linked list
print("121910313006","Kadiyala Rohit Bharadwaj")
# Defining the Node class
class Node:
    def __init__(self, data):  # Constructor for Node class
        self.data = data
        self.next = None


# Defining the Linked List class
class LinkedList:
    def __init__(self):  # Constrctor for LinkedList class
        self.head = None

    # Method to append data
    def append(self, data):
        new_node = Node(data)
        # If head is empty
        if self.head is None:
            self.head = new_node
            return
        # If head is not empty
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    # Method to print linked list
    def print_list(self):
        cur = self.head
        while cur:
            # Traversing through each element and printing it
            print(cur.data)
            cur = cur.next

    # Method to add node at the middle of a linked list
    def addRandom(self, prev_node, data):
        new_node = Node(data)
        cur = self.head
        while cur:
            nxt = cur.next
            if cur.data == prev_node:
                cur.next = new_node
                new_node.next = nxt
                return
            cur = cur.next
        print("Node not found")


ll = LinkedList()  # Creating a linked list

size = int(input("Enter the number of elements : "))
# Appending data to it
for i in range(size):
    k = input("Enter the data : ")
    ll.append(k)

# Prninting the current linked list
print("The Current Linked List is : ")
ll.print_list()

# Taking a value to add at the linked list
n = input("Enter the data you want to add : ")
k = input("Enter the node after which you want to add it : ")
ll.addRandom(k, n)

# Prninting the updated linked list
print("The Updated Linked List is : ")
ll.print_list()
