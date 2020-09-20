# Multiplication of two Sparse matrices
print("121910313006","Kadiyala Rohit Bharadwaj")

n = int(input('Enter the value of N in NxN matrix: '))
print('''This is a Sparse matrix
So Enter High volumes/frequencies of Zero "0" ''')
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

print('The product of the two Sparse Matrices is :')
for p in pro:
    for r in p:
        print(r, end=' ')
    print()

# Representing the product of two matrices in Sparce matrix form :
sparse_matrix = []
for i in range(len(pro)):
    for j in range(len(pro[0])):
        if pro[i][j] != 0:
            temp = []
            temp.append(i)
            temp.append(j)
            temp.append(pro[i][j])
            sparse_matrix.append(temp)

print('''The Sparse Matrix Representation :
Row\tCol\tValue\t''')
for i in sparse_matrix:
    for x in i:
        print(x, end=' \t ')
    print()



