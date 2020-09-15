#Finding smallest of three numbers
print("121910313006","Kadiyala Rohit Bharadwaj")
#Creating integer variables
n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))

#logic
if(n1<n2 and n1<n3):
    print(n1,"is smallest of the given three numbers")
elif(n2<n3):
    print(n2,"is smallest of the given three numbers")
else:
    print(n3,"is smallest of the given three numbers")


