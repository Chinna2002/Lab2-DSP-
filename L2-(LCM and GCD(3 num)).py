#GCD and LCM of three numbers
print("121910313006","Kadiyala Rohit Bharadwaj")
from math import gcd
#Creating a function
def compute(a,b,c):
    g1=gcd(b,c)
    g2=gcd(a,g1)
    l1=(b*c)/g1
    l2=(a*l1)/g2
    return g2,l2
x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
z=int(input("Enter z value:"))
res1,res2=compute(x,y,z)


#Displaying the results
print("GCD is",res1)
print("LCM is",res2)
