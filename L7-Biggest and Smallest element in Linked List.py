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
        if self.head is None:
            print("list is empty")
            return
        cur = self.head
        while cur:
            # Traversing through each element and printing it
            print(cur.data)
            cur = cur.next

    # Method for maximum and minimum elements in linked list
    def minmax(self):
        if self.head is None:
            print("list is empty")
            return (None, None)
        cur = self.head
        min = None
        max = None
        while cur:
            # Traversing through each element
            temp = cur.data
            if min == None or temp < min:
                min= temp
            if max == None or temp > max:
                max= temp
            cur = cur.next
        return (min, max)


ll = LinkedList()  # Creating a linked list
size = int(input("Enter the number of elements:"))
# Appending data to it
for i in range(size):
    k = int(input("Enter the data : "))
    ll.append(k)
# Printing the linked list
print("The Linked List: ")
ll.print_list()
# Printing the maximum and minimum of the linked list
small, big = ll.minmax()
print("The minimum element is", small)
print("The maximum element is", big)