# Program to search for an element in a linked list
# J. Raghuramjee - 121910313004

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

    def search(self, key):
        found = False
        cur = self.head
        # Traversing through each element and checking
        while cur:
            if cur.data == key:
                found = True
                break
            cur = cur.next
        return found


ll = LinkedList()  # Creating a linked list

size = int(input("Enter the number of elements  : "))
# Appending data to it
for i in range(size):
    k = input("Enter the data : ")
    ll.append(k)

# Element to search
n = input("Enter the element to search : ")
ans = ll.search(n)
if ans==True:
    print("The element is present in Linked List")
else:
    print("The element is not present in Linked List")