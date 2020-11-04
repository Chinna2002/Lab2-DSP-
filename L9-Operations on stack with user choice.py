print("121910313006","Kadiyala Rohit Bharadwaj")
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
       if data not in self.items and len(self.items)<=n:
            self.stack.append(data)
            return
        print("OverFlow")
        return

    def pop(self):
        if s.items!=[]: 
            return self.items.pop()
        else:
            print("UnderFlow Condition")
    def printstack(self):
        print(self.items)
s=Stack()
i=True
l=int(input("Enter size of stack "))
while(i):
    print("1.Push","2.Pop","3.Display","4.Exit")
    choice = int(input("Select an Option:"))
    if(choice==1):
        s.push(int(input("Enter Element:")),l)
    elif (choice == 2):
        print("The Stack Element popped is:",s.pop())
    elif (choice == 3):
        print("The Stack is:")
        s.printstack()
    elif (choice== 4):
        i = False
        print("Task Terminated")
    else:
        print("Enter a valid input ")



