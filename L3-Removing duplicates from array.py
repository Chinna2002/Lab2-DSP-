print("121901313006","Rohit Bharadwaj Kadiyala")
l1=[] #creating a array
n=int(input("Enter array size:"))
for i in range(0,n):
    l1.append(int(input("Enter element:")))
print("Original array:",l1)#Original array
res=[]#creating a new array
for i in l1:
    if i not in res:
        res.append(i)
print("New array is:",res)#Array without duplicate elements