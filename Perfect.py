#Checking whether a number is perfect number or not
print("121910313006","Kadiyala Rohit Bharadwaj")
sum = 0 #initialising sum to zero
n=int(input("Enter a number:"))
#logic
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print(n,"is perfect number")
else:
    print(n,"is not a perfect number")
