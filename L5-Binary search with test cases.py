"""
#Test Case-1(Array of characters)
Enter the size of array: 4
enter element:a
enter element:b
enter element:c
enter element:d
['a', 'b', 'c', 'd']
Enter the target to be searched:c
Element c found at 2
"""
"""
#Test Case -2(With repetation of elements)
Enter the size of array: 4
enter element:1
enter element:2
enter element:1
enter element:3
[1, 1, 2, 3]
Enter the target to be searched:1
Element 1 found at 1
"""
"""
#Test Case-3(Negative numbers as elements)
Enter the size of array: 5
enter element:-1
enter element:-3
enter element:-5
enter element:-6
enter element:-2
[-6, -5, -3, -2, -1]
Enter the target to be searched:-5
Element -5 found at 1
"""
n=int(input("Enter the size of array: "))
a=[]
for i in range(n):
    a.append(int(input("enter element:")))
a.sort()
print(a)
target=int(input("Enter the target to be searched:"))
low =0
high=len(a)-1
mid=(low+high)//2
if a[mid]==target:
    print(f' Element {target} found at {mid}')
elif a[mid]<target:
    low=mid+1
    for i in range(low,high+1):
        if a[i]==target:
             print(f' Element {target} found at {i}')
             break
elif  a[mid]>target:
    low=0
    high=mid
    for i in range(low,high):
        if a[i]==target:
            print(f' Element {target} found at {i}')
            break
else:
    print("Element not found")