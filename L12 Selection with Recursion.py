import sys
print("121910313006","Kadiyala Rohit Bharadwaj")
print("SELECTION SORT WITH RECURSION")
def Selection(arr,i,n):
    min_idx = i
    for j in range(i + 1, len(A)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    if i + 1 < n: Selection(arr, i + 1, n)
A = []
n=int(input("Enter Array/List Size:"))
for i in range(n):
    A.append(int(input("Enter Element:")))
print("List:",A)
Selection(A,0,n)
print("Sorted array:",A)
