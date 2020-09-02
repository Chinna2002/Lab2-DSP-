print("121910313006","Kadiyala Rohit Bharadwaj")
#Printing Twin Primes up to specified range
def prime(n):#Fuction1
    isprime=True
    for i in range(2,n):
        if(n%i==0):
            isprime = False
            break
    return isprime
def twin(a,b):#function2
    for k in range(a,b+1):
        j=k+2
        if (prime ( k ) and prime ( j )) :
            print ( {k , j} )

#Giving input
x=int(input("Enter starting value:"))
y=int(input("Enter Ending value:"))
twin(x,y)