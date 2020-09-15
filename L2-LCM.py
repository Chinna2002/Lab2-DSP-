#LCM of two numbers
print("121910313006","Kadiyala Rohit Bharadwaj")
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))

#logic
if(a>b):
    greater=a
else:
    greater=b
while(True):
    if(greater%a==0 and greater%b==0):
        lcm=greater
        break
    greater=greater+1
#Displaying LCM of Two numbers
print("LCM of a and b is ",lcm)
