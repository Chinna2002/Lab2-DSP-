print("121910313006","Kadiyala Rohit Bharadwaj")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def remove_head(self):
        if self.head and self.head.next:
            d = self.head
            self.head = self.head.next
            d.next = None
        return d.data

    def printlist(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()


class SLL:
    def __init__(self):
        self.items = LinkedList()

    def push(self, data):
        self.items.add_at_end(data)

    def pop(self):
        return self.items.remove_head()

    def peek(self):
        return self.items.tail.data

    def printstack(self):
        self.items.printlist()

s = SLL()
n=int(input("Enter Stack size:"))
for i in range(n):
    s.push(int(input("Enter Element:")))
print("Original Stack is")
s.printstack()#Displaying the Stack
print("peek is:", s.peek())#Displaying the Top most element
print("Stack element which is removed is:",s.pop())#removing the top element
print("The Updated Stack is:")
s.printstack()

