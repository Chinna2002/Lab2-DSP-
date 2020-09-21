print("121910313006","Kadiyala Rohit Bharadwaj")

def displaying_sparse_matrix(a):
    sp1 = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != 0:
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(a[i][j])
                sp1.append(temp)

    print('''The Sparse Matrix Representation :
    Row\tCol\tValue\t''')
    for i in sp1:
        for x in i:
            print(x, end=' \t ')
        print()


def addition_Of_Two_Matrices():
    n = int(input("Enter the Value of N in NxN matrix :"))
    # Inputing the first matrix:
    print("\nEnter the values for the first matrix : ")

    a = []
    for i in range(n):
        print(f'Enter the values for {i}th row : ')
        x = []
        for j in range(n):
            x.append(int(input()))
        a.append(x)

    # Inputing the second Matrix:
    print('\nEnter the values for the Second Matrix :')
    b = []
    for i in range(n):
        print(f'Enter the values for {i}th row : ')
        x = []
        for j in range(n):
            x.append(int(input()))
        b.append(x)

    # Addition of the two matrices:

    # Creating an empty matrix for storing the value of a + b matrices
    s = [[0 for j in range(n)] for i in range(n)]

    for i in range(len(a)):
        for j in range(len(a[0])):
            s[i][j] = a[i][j] + b[i][j]

    print('The sum of the two sparse matrices is :')
    for r in s:
        for y in r:
            print(y, end="  ")
        print()

    displaying_sparse_matrix(s)


def multiplication_of_sparse_matrix():
    n = int(input('Enter the value of N in NxN matrix : '))
    # Taking input of the values of 1st matrix
    print("Enter the values of First Matrix: ")
    a = []
    for i in range(n):
        x = []
        print(f'Enter the values for {i}th row : ')
        for j in range(n):
            x.append(int(input()))
        a.append(x)

    # Taking the inputs for Second Matrix
    print('Enter the values for Second matrix :')
    b = []
    for i in range(n):
        x = []
        print(f'Enter the values for {i}th row: ')
        for j in range(n):
            x.append(int(input()))
        b.append(x)

    # Multiplication of Two Sparce Matrices:

    # Creating an matrix to Store the produt of Matrices
    pro = [[0 for j in range(n)] for i in range(n)]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                pro[i][j] += a[i][k] * b[k][j]
    print("The Product of the Matrices is :")
    for k in pro:
        for i in k:
            print(i, end='  ')

        print()

    displaying_sparse_matrix(pro)


# Transpose of the Matrix
def transpose_of_matrix():
    n = int(input('Enter the value of N in NxN Matrix : '))
    a = []
    for i in range(n):
        x = []
        print(f'Enter the values in {i}th row : ')
        for j in range(n):
            x.append(int(input()))
        a.append(x)

    b = [[a[j][i] for j in range(n)] for i in range(n)]
    print("The Transposed matrix : ")
    for v in b:
        for e in v:
            print(e, end='  ')
        print()

    displaying_sparse_matrix(b)


m = int(input('''Enter the Respective number to Perfrom the Specific operation:
1 - Addition of Two Sparse Matrices
2 - Multiplication of Two Sparse Matrices
3 - Transpose of Sparse Matrix
4 - Displaying the Matrix :\n>'''))

if m == 1:
    addition_Of_Two_Matrices()
elif m == 2:
    multiplication_of_sparse_matrix()
elif m == 3:
    transpose_of_matrix()
elif m == 4:
    n = int(input('Enter the value of N in NxN Matrix : '))
    a = []
    for i in range(n):
        x = []
        print(f'Enter the values in {i}th row : ')
        for j in range(n):
            x.append(int(input()))
        a.append(x)

    displaying_sparse_matrix(a)

else:
    print("Enter an appropriate number")