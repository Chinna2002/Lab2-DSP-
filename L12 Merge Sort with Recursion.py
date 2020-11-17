print("121910313006","Kadiyala Rohit Bharadwaj")
print("****MERGE SORT WITH RECURSION******")
def Merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    Lft, Right = Merge(arr[:mid]), Merge(arr[mid:])
    return merge(Lft, Right)
def merge(Lft, Right):
    result = []
    i = j = 0
    while j < len(Lft) and i < len(Right):
        if Lft[j] <= Right[i]:
            result.append(Lft[j])
            j = j + 1
        else:
            result.append(Right[i])
            i = i + 1
    result.extend(Lft[j:])
    result.extend(Right[i:])
    return result
lst = []
num = int(input("Enter number of elements : "))
for i in range(0, num):
    ele = int(input("Enter Element:"))
    lst.append(ele)
print("Present List/Array:")
print(lst)
print("Array/list after Merge Sort:")
print(Merge(lst))