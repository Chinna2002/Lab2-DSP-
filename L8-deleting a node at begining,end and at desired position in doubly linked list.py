#Adding a node as per giving user choice
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
    def push(self, new_data):#Funtion for adding node a the begining
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(data=new_data)

        # 3. Make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None

        # 4. change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node

            # 5. move the head to point to the new node
        self.head = new_node
    def appendEnd(self, new_data):

        # 1. allocate node 2. put in the data
        new_node = Node(data=new_data)
        last = self.head

        # 3. This new node is going to be the
        # last node, so make next of it as NULL
        new_node.next = None

        # 4. If the Linked List is empty, then
        #  make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # 5. Else traverse till the last node
        while (last.next is not None):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node
        # 7. Make last node as previous of new node */
        new_node.prev = last
    def adding_Node(self, key, data):
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
    def print(self):
        cur=self.head
        if(self.head==None):
            print("Empty list")
            return;
        print("Nodes of the double lined list are:")
        while(cur!=None):
            print(cur.data)
            cur=cur.next
dList=DoublyLinkedList();
size = int(input("Enter the number of elements : "))
# Appending data to it
for i in range(size):
    k = input("Enter the data : ")
    dList.append(k)
print("Original list:")
dList.print()
print("1.At Begining"
      "2.At End"
      "3.At desired postion")
choice=int(input("Select an option"))
if(choice==1):
    n = input("Enter the new head of the Linked List : ")
    dList.push(n)
    # Prninting the updated linked list
    print("The Updated Linked List is : ")
    dList.print()
elif(choice==2):
    n = input("Enter the new end of the Linked List : ")
    dList.appendEnd(n)
    # Prininting the updated linked list
    print("The Updated Linked List is : ")
    dList.print()
elif(choice==3):
    k = input("Enter the node after which we should add the node : ")
    h = input("Enter the new node : ")
    dList.add_at_middle(k, h)
    print("The updated linked list is : ")
    dList.print_list()
else:
    print("Error")


