# Program to implement a Linked List with function to change head
print("121910313006","Kadiyala Rohit Bharadwaj ")
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

    # Method to update head
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to print linked list
    def print_list(self):
        cur = self.head
        while cur:
            # Traversing through each element and printing it
            print(cur.data)
            cur = cur.next


ll = LinkedList()  # Creating a linked list
size = int(input("Enter the number of elements  : "))
# Appending data to it
for i in range(size):
    k = input("Enter the data : ")
    ll.append(k)
# Prninting the current linked list
print("The Current Linked List is : ")
ll.print_list()

# Updating head
n = input("Enter the new head of the Linked List : ")
ll.prepend(n)

# Prninting the updated linked list
print("The Updated Linked List is : ")
ll.print_list()