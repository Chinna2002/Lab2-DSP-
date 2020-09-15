print("121910313006","Kadiyala Rohit Bharadwaj" )
#printing prime numbers up to given range
s1=int(input("Enter starting limit:")) #Start Value
s2=int(input("Enter ending limit:")) #End Value

print("Prime numbers between the given range are:")
#logic
for num in range(s1, s2 + 1):
# all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)