print("121910313006","Kadiyala Rohit Bharadwaj")
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

    print()
    # Displaying output
    print("SparseMatrix:")
    for row in sparseMatrix:
        for ele in row:
            print(ele, end=" ")
        print()

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
dispmatrix(matrix)#Calling Funtion1
sparse(matrix)#Calling Fuction2