L=[]
n=int(input("Enter Size of the array:"))
for i in range(n):
    a=int(input("Enter Element:"))
    L.append(a)
print("The Array is:",L)
#sorting the array
L.sort()
print("Sorted array:",L)
print("Second Smallest Element is:",L[1])