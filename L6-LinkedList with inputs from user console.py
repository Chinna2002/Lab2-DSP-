#linked list with user inputs
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


ll = LinkedList()  # Creating a linked list
size = int(input("Enter the number of elements you want to add to the Linked List : "))
# Appending data to it
for i in range(size):
    k = input("Enter the data : ")
    ll.append(k)
# Prninting the linked list
print("The Linked List is : ")
ll.print_list()