print("121910313006","Kadiyala Rohit Bharadwaj")
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def binary(self):
        if self.left:
            self.left.binary()
        print( self.data),
        if self.right:
            self.right.binary()
b = Node(45)
b.insert(100)
b.insert(50)
b.insert(120)
b.insert(30)
b.insert(60)
b.insert(20)
b.insert(35)
b.insert(45)
b.insert(95)
b.insert(105)
b.insert(300)
b.insert(400)
print("Nodes in Binary Tree are:")
b.binary()