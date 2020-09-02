#Checking whether amstrong number or not
print("121910313006","Kadiyala Rohit Bharadwaj")
x=int(input("enter a number:"))
sum=0 #initialising sum to zero
temp=x#assigning n value to tempararory variable temp
while(temp>0):
    rem=temp%10
    sum=sum+rem*rem*rem
    temp=temp//10
print("Sum of digits in the number is:",sum)
if(x==sum):#Checking whether sum and n are equal or not
    print("It is an amstrong number")
else:
    print("It is not an amstrong number")
