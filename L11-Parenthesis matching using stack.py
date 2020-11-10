class Stack:
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
        return
    def pop(self):
        if (self.items == []):
            print("UnderFlow Condition")
        else:
            return self.items.pop()
    def isEmpty(self):
        if(len(self.items)==0):
            return True
        return False
    def peek(self):
        return self.items[-1]
    def length(self):
        return len(self.items)

    def printstack(self):
        print(self.items)
def Check(string):
    s = Stack()
    balanced = True
    i = 0
    while i < len(string) and balanced:
        symbol = string[i]
        if symbol ==  "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        i = i + 1
    if(balanced and s.isEmpty()):
        return True
    else:
        return False
exp=input("Enter brackets:")
print(Check(exp))