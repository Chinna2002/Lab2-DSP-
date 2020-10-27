  print("121910313006","Kadiyala Rohit Bharadwaj")
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self,data):
        if data in self.items:
            self.items.remove(data)
            print("Element removed/popped!")
        else:
            print("Element not found")

    def print_stack(self):
        print(self.items)


s1 = Stack()
n=int(input("Enter Stack Size:"))
for i in range(n):
    s1.push(int(input("Enter Element:")))
print("Original List: ")
s1.print_stack()
d = int(input("Enter the element you want to pop : "))
s1.pop(d)
print("The Updated Stack is:")
s1.print_stack()
