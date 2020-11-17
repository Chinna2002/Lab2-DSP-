print("121910313006","Kadiyala Rohit Bharadwaj")
print("Merge Sort ")
# Function for Merge sort
def mergesort(list):
    if len(list) < 2: return list
    mi = int(len(list)/2)
    le = mergesort(list[:mi])
    ri = mergesort(list[mi:])
    return merge(le, ri)

def merge(le, ri):
    if not len(le) or not len(ri): return le or ri
    result = []
    i, j = 0, 0
    while (len(result) < len(le) + len(ri)):
        if le[i] < ri[j]:
            result.append(le[i])
            i+= 1
        else:
            result.append(ri[j])
            j+= 1
        if i == len(le) or j == len(ri):
            result.extend(le[i:] or ri[j:])
            break
    return result
lst = []
num = int(input("Enter number of elements : "))
for i in range(0, num):
    ele = int(input("Enter Element:"))
    lst.append(ele)
print("Present List/Array:")
print(lst)
print("Array/list after Merge Sort:")
print(mergesort(lst))
