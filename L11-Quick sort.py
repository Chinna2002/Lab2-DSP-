#Quick Sort
L=list(map(int,input().split()))
def QuickSort(l):
    k=len(l)
    if k<2:
        return l
    c=0
    for i in range(1,k):
        if l[i]<=l[0]:
            c+=1
            l[c],l[i]=l[i],l[c]
    l[0],l[c]=l[c],l[0]
    left=QuickSort(l[0:c])
    right=QuickSort(l[c+1:])
    return left+[l[c]]+right
print("Sorted array is: ",QuickSort(L))