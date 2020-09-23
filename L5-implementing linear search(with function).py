#Linear Search by using user defined function and input
print("121910313006","Kadiyala Rohit Bharadwaj")
def Linear(arr,x):#User defined function
    l=len(arr)
    flag=0
    for i in range(l):
        if(x==arr[i]):
            flag=1
            break
    if(flag==1):
        print("Search element found at index location:",i)
    else:
        print("Search element not found")
#Taking input
array=[]
n=int(input("Enter size of the array:"))
for i in range(n):
    array.append(int(input("Enter element:")))
print(array)
search=int(input("Enter element to be searched:"))

Linear(array,search)#Calling function
