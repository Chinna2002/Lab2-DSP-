#Checking whether amstrong number or not
print("121910313006","Kadiyala Rohit Bharadwaj")
n=int(input("Enter number of digits:"))
x=int(input("enter a number:"))
temp=x
sum=0
sum1=0
while(temp!=0):
    rem=temp%10
    sum=sum+rem**n
    sum1=sum1+rem
    temp=temp//10
print("sum of cubes of the digits in the number:",sum)
if(x==sum):#Checking whether sum and n are equal or not
    print(x," is amstrong number")
else:
    print(x," is not a amstrong number")
print("Sum of digits in the number is:",sum1)