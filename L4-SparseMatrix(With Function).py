print("121910313006","Kadiyala Rohit Bharadwaj")
def dispmatrix(a):#function1(For dispalying matrix)
    for row in matrix:
        for ele in row:
            print(ele, end=" ")
        print()
def sparse(a):#function2(For converting to sparse matrix)
    sparseMatrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[2])):
            if (matrix[i][j] != 0):
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])
                sparseMatrix.append(temp)
    print()
    # displaying output
    print("SparseMatrix:")
    for row in sparseMatrix:
        for ele in row:
            print(ele, end=" ")
        print()
matrix=[[0,10,0,0],
        [0,0,20,0],
        [30,0,0,0],
        [0,0,0,40]]
dispmatrix(matrix)
sparse(matrix)