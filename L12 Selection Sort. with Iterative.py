import sys
print("121910313006","Kadiyala Rohit Bharadwaj")
print("SELECTION SORT")
def Selection(arr):
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
A = []
n=int(input("Enter Array/List Size:"))
for i in range(n):
    A.append(int(input("Enter Element:")))
print("List:",A)
Selection(A)
print("Sorted array:",A)
