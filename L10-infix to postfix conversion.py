print("121910313006","Kadiyala Rohit Bharadwaj")
#Infix to Postfix conversion
infix=input("Enter infix expression(using alphabets in it): ")
s=[]
res=""
prec={'+':1, '-':1, '*':2, '/':2, '^':3}
def notGreater(h):
  try:
    g=prec[h]
    f=prec[s[-1]]
    if g<=f:
      return True
    else:
      return False
  except:
    return False
for i in infix:
  if i=="(":
    s.append(i)
  elif i.isalpha():
    res+=i
  elif i==")":
    while s[-1]!="(" and len(s)!=0 :
      res+=s.pop()
    s.pop()
  else:
    while len(s)!=0 and notGreater(i):
      res+=s.pop()
    s.append(i)
while len(s)>0:
  res+=s.pop()
print("Postfix expression:",res)