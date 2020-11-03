print("121910313006","Kadiyala Rohit Bhardawaj")
#Evaluating Postfix Expression
class Evaluate:
    def __init__(self):
        self.top = -1
        self.array = []
    def isEmpty(self):
      if self.top == -1:
          return True
      else:
          return False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            print("Empty")
    def push(self, op):
        self.top += 1
        self.array.append(op)
    def evaluatePostfix(self, exp):#Function for postfix evaluation
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
        return int(self.pop())

x=input("Enter an expression:")
s=Evaluate()
print(s.evaluatePostfix(x))



