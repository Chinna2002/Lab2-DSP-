def add(A1,A2):
    sum = []
    l1 = len(A1)
    l2 = len(A2)
    if l1==0 : sum = A2
    if l2==0 : sum = A1
    i = 0
    j = 0
    while l1>0 and l2>0:
        if A1[i][0]==A2[j][0] and A1[i][1]==A2[j][1]:
            sum.append([A1[i][0],A1[i][1],A1[i][2]+A2[j][2]])
            i += 1
            j += 1
        else:
            m = min(A1[i],A2[j])
            sum.append(m)
            if m==A1[i]:
                i += 1
            else:
                j += 1
        if i>=l1:
            for x in range(j,l2):
                sum.append(A2[x])
            break
        if j>=l2:
            for x in range(i,l1):
                sum.append(A1[x])
            break
    return sum
def dispmatrix(a):#Function1(For dispalying matrix)
    for row in matrix:
        for ele in row:
            print(ele, end=" ")
        print()
def sparse(a):#Function2(For converting to sparse matrix)
    sparseMatrix = []
    Threshold=int(input("Enter threshold value:"))
    for i in range(len(matrix)):
        for j in range(len(matrix[2])):
            if (matrix[i][j]<=Threshold):
                matrix[i][j]=0
            if(matrix[i][j]!=0):
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])
                sparseMatrix.append(temp)
    return sparseMatrix


#Taking Input
row1 = int(input("Enter the number of rows:"))
col1 = int(input("Enter the number of columns:"))
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
for i in range(row1):  # A for loop for row entries
    a = []
    for j in range(col1):  # A for loop for column entries
        a.append(int(input()))
    print()
    matrix.append(a)
#for array 1
dispmatrix(matrix)#Calling Funtion1
x=sparse(matrix)#Calling Fuction2
print("SparseMatrix1:",x)
#For array2
#Taking Input
print("Matrix2")
row2 = int(input("Enter the number of rows:"))
col2 = int(input("Enter the number of columns:"))
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
for i in range(row1):  # A for loop for row entries
    a = []
    for j in range(col1):  # A for loop for column entries
        a.append(int(input()))
    print()
    matrix.append(a)
dispmatrix(matrix)#Calling Funtion1
y=sparse(matrix)#Calling Fuction2
print("SparseMatrix2:",y)
z=add(x,y)
print("Addition of two SparseMatrix is:")
for row in z:
    for ele in row:
        print(ele,end=" ")
    print()