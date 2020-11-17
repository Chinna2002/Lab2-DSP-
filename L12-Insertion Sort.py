def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
l=[]
n=int(input("Enter size of the list:"))
for i in range(n):
    l.append(int(input("Enter Element:")))
print("List:",l)
insertionSort(l)
print("Sorted list",l)
