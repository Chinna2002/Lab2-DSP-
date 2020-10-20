print("121910313006","Kadiyala Rohit Bharadwaj")
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
    def print(self):
        cur=self.head
        if(self.head==None):
            print("Empty list")
            return;
        print("Nodes of the double lined list are:")
        while(cur!=None):
            print(cur.data)
            cur=cur.next


dList=Doublelinkedlist();
size = int(input("Enter the number of elements : "))
# Appending data to it
for i in range(size):
    k = input("Enter the data : ")
    dList.addNode(k)
print("Original list:")
dList.print()
# Updating head
n = input("Enter the new head of the Linked List : ")
dList.push(n)

# Prninting the updated linked list
print("The Updated Linked List is : ")
dList.print()
