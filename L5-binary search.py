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