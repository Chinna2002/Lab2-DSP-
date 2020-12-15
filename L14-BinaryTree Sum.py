class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
class BinaryTree:
  def __init__(self):
    self.root=None

  def addBT(self, root):
    if (root == None):
      return 0
    return (root.data + self.addBT(root.left) +
            self.addBT(root.right))
B=BinaryTree()
B.root = Node(5)
B.root.left = Node(2)
B.root.right = Node(9)
B.root.left.left = Node(1)
B.root.right.left = Node(8)
B.root.right.right = Node(6)
print("Sum of all nodes BST is",B.addBT(B.root))