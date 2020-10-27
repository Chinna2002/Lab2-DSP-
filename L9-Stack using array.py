class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

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
        if(self.items == []):
            print("UnderFlow Condition")
        else:
            print(self.items)


s = Stack()
n=int(input("Enter size of the stack:"))
for i in range(n):
    n=int(input("Enter element:"))
    s.push(n)
z=s.length()
s.printstack()
print("Length of the Stack is:",s.length())
print("The top element is:",s.peek())
print("Stack element which is removed:",s.pop())
print("Updated Stack:")
s.printstack()
print("The top element now  is:",s.peek())
print("Length of the Stack is:",s.length())

