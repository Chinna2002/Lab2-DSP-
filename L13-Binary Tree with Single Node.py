print("121910313006","Kadiyala Rohit Bharadwaj")
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def print(self):
        print(self.data)
n=int(input("Enter a value to add a node to Binary Tree:"))
r = Node(n)
print("Nodes in Binary Tree are:")
r.print()