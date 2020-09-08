print("121901313006","Rohit Bharadwaj Kadiyala")
l1=[] #creating a array
n=int(input("Enter array size:"))
for i in range(0,n):
    l1.append(int(input("Enter element:")))
print("Original array:",l1)#Original array
l2=[None]*len(l1)
l=len(l1)
for i in range(0,l):
    l2[i]=l1[i]
for i in range(0,len(l2)):
    print(l2[i])
print("New array is",l2)#new array