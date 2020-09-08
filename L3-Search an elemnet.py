print("121901313006","Rohit Bharadwaj Kadiyala")
x=0
def search(arr):#Fuction 1
    x=int(input("Enter search element:"))
    for i in arr:
        if(x==i):
            flag=1
            break
        else:
            flag=0
    if(flag==1):
        print("Search element",x,"found in the array at",i-1)
    else:
        print("Search element not found")
l1=[] #creating an array
n=int(input("Enter array size:"))
for i in range(0,n):
    l1.append(int(input("Enter element:")))
print("array:",l1)
search(l1)#function call