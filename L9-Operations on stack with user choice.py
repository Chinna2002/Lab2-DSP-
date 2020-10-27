class Stack:
    def __init__(self):
        self.items = []

    def push(self, data,l):
        if data not in self.items and len(self.items) <= l:
            self.items.append(data)
            return
        print("Overflow")
        return

    def pop(self):
        if len(self.items)>0:
            x=self.items[-1]
            self.items.pop()
            return x
        print("Underflow")
        return
    def length(self):
        return len(self.items)

    def printstack(self):
        if(len(self.items) == 0):
            print("UnderFlow Condition")
        else:
            print(self.items)
s=Stack()
n = int(input("Enter size of the stack:"))
i=True
while(i):
    print("1.Push","2.Pop","3.Display","4.Exit")
    choice = int(input("Select an Option:"))
    if(choice==1):
        s.push(int(input("Enter Element:")),n)
    elif choice == 2:
        print(s.pop())
    elif choice == 3:
        s.printstack()
    elif choice== 4:
        i = False
    else:
        print("Enter a valid input ")



