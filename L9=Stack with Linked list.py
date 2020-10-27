class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
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
        self.head.prev = new_node
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def remove_tail(self):
        if self.head is None:
            print("Underflow")
            return
        p = None
        t = self.head
        while t.next:
            p = t
            t = t.next
        l = t.data
        p.next = None
        t = None
        return l
    def printlist(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()


class StackLL:
    def __init__(self):
        self.items = DLL()

    def push(self, data):
        self.items.add_at_end(data)

    def pop(self):
        return self.items.remove_tail()

    def peek(self):
        return self.items.tail.data

    def printstack(self):
        self.items.printlist()


s = StackLL()
n=int(input("Enter Stack size:"))
for i in range(n):
    s.push(int(input("Enter Element:")))
print("Original Stack is")
s.printstack()
print("peek is:", s.peek())
print("Stack element which is removed is:",s.pop())
print("The Updated Stack is:")
s.printstack()
