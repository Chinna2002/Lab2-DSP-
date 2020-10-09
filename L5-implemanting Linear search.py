#Linear Search
print("121910313006","Kadiyala Rohit Bharadwaj")
l=[1,2,21,8,9,77,50]#array
flag=0#initialising to zer0
search=int(input("enter an element to be searched:"))
for i in range(len(l)):
    if(search==l[i]):
        flag=1
        break
if(flag==1):
    print("Search element found at index location",i)
else:
    print("Search element not found")
