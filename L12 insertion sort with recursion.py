print("121910313006","Kadiyala Rohit Bharadwaj")
print("INSERTION  SORT WITH RECURSION")
def insertionsort(arr,i,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j=j-1
        arr[j + 1] = key
        if i + 1 < n:
            insertionsort(arr, i + 1, n)
l=[]
n=int(input("Enter size of the list:"))
for i in range(n):
    l.append(int(input("Enter Element:")))
print("List:",l)
insertionsort(l,0,n)
print("Sorted List is: ",l)