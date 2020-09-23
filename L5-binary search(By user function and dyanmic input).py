def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

            # If we reach here, then the element was not present
    return -1
# Test array
#Taking input
array=[]
n=int(input("Enter size of the array:"))
for i in range(n):
    array.append(int(input("Enter element:")))
array.sort()# sorting the array
search=int(input("Enter element to be searched:"))
# Function call
result = binary_search(array, search)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")