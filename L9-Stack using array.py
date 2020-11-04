print("121910313006","Kadiyala Rohit Bharadwaj")
class Stack:
    def __init__(self):
        self.items = []
    def push(self,data,n):
      if data not in self.items and len(self.items) < n:
        self.items.append(data)
        return
      print("OverFlow")
      return
    def pop(self):
        if (self.items == []):
            print("UnderFlow Condition")
        else:
            return self.items.pop()
    def peek(self):
        return self.items[-1]
    def length(self):
        return len(self.items)

    def printstack(self):
        print(self.items)


s = Stack()
n=int(input("Enter size of the stack:"))
for i in range(n):
    b=int(input("Enter element:"))
    s.push(b,n)
s.printstack()
print("Length of the Stack is:",s.length())
print("The top element is:",s.peek())
print("Stack element which is removed:",s.pop())
print("Updated Stack:")
s.printstack()
print("The top element now  is:",s.peek())
print("Length of the Stack is:",s.length())
