print("121901313006","Rohit Bharadwaj Kadiyala")
l1=[] #creating a array1
n1=int(input("Enter array1 size:"))
for i in range(0,n1):
    l1.append(int(input("Enter element:")))
l2=[] #creating a array1
n2=int(input("Enter array2 size:"))
for i in range(0,n2):
    l2.append(int(input("Enter element:")))
#Concatination of the arrays
"#Method1"
z=[]
z=l1+l2 #using addition operator for concatinating two arrays
print("Concatinated array:",z)
"#Method2"
#using extend() function
l1.extend(l2)
print("Concatinated array by extend function:",l1)
