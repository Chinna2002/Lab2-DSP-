#Checking whether amstrong number or not
print("121910313006","Kadiyala Rohit Bharadwaj")
x=int(input("enter a number:"))#Var1
temp1=x
rem1=0
sum1=0
c=0
while(temp1>0):
    rem1=temp1%10
    c=c+1
    sum1=sum1+rem1
    temp1=temp1//10
temp2=x
rem2=0
sum2=0
while(temp2>0):
    rem2=temp2%10
    sum2=sum2+rem2**c
    temp2=temp2//10
print("No.of digits is:",c)
print("Sum of digits in the number is:",sum1)
print("Sum of cubes of digits of the number:",sum2)
if(sum2==x):#Checking whether sum and n are equal or not
    print(x," is an Amstrong number")
else:
    print(x," is not an Amstrong number")
