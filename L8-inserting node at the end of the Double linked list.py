class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
        self.prev=None;
class Doublelinkedlist:
    def __init__(self):
        self.head=None;
        self.tail=None;
    def addNode(self,data):
        newNode=Node(data)

        if(self.head==None):
            self.head=self.tail=newNode

            self.head.prev=None

            self.tail.next=None
        else:
            self.tail.next=newNode

            newNode.prev=self.tail
            self.tail=newNode
            self.tail.next=None

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
    def print(self):
        cur = self.head
        if (self.head == None):
            print("Empty list")
            return;
        print("Nodes of the double lined list are:")
        while (cur != None):
            print(cur.data)
            cur = cur.next



dList=Doublelinkedlist();
size = int(input("Enter the number of elements : "))
# Appending data to it
for i in range(size):
    k = input("Enter the data : ")
    dList.addNode(k)
print("Original list:")
dList.print()
# Updating head
n = input("Enter the new end of the Linked List : ")
dList.appendEnd(n)

# Prninting the updated linked list
print("The Updated Linked List is : ")
dList.print()
