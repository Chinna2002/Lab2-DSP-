print("121910313006","Kadiyala Rohit Bharadwaj")
#Input
matrix=[[0,10,0,0],
        [0,0,20,0],
        [30,0,0,0],
        [0,0,0,40]]
#convetring normal matrix to sparse matrix
for row in matrix:
    for ele in row:
        print(ele,end=" ")
    print()
sparseMatrix=[]
for i in range(len(matrix)):
    for j in range(len(matrix[2])):
        if(matrix[i][j]!=0):
            temp=[]
            temp.append(i)
            temp.append(j)
            temp.append(matrix[i][j])
            sparseMatrix.append(temp)
print()
#displaying output
print("SparseMatrix:")
for row in sparseMatrix:
    for ele in row:
        print(ele,end=" ")
    print()