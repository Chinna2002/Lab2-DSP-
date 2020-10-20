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
dList.print()