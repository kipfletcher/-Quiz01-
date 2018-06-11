# Kip Fletcher  MATH 4330  06-09-2018
# Quiz 1

# matVec takes a matrix and a vector and returns the matrix vector product.

def matVec(matrix, vector):
    '''
    This function takes a matrix and a vector as its arguments. It then
    creates a new matrix by multiplying the input matrix by the input vector
    and returns the new matrix. 
    '''
    new_matrix = []         # holds the matrix vector product.
    for i in range(len(vector)):
        row_product = 0     # holds the product of each matrix row.
        for j in range(len(matrix)):
            row_product += (matrix[i][j]*vector[j])
        new_matrix.append(row_product) # adds each row product entry to new matrix.
    return new_matrix

# These are the test variables initialized to test the function matVec.

test_vector01 =  [2,3]
test_matrix01 = [[1,3],
                 [1,4]]

test_vector02 =  [2,4,3]
test_matrix02 = [[4,3,1],
                 [1,4,2],
                 [3,2,1]]

test_vector03 = [[4,3,1],
                 [1,4,2],
                 [3,2,1]]
test_matrix03 =  [2,4,3]

test_vector04 = 5
test_matrix04 = "Are we having fun yet?"

# These are test cases for the function matVec with only one in use at a time.

#print(matVec(test_matrix01,test_vector01))
print(matVec(test_matrix02,test_vector02))
#print(matVec(test_matrix03,test_vector03))
#print(matVec(test_matrix04,test_vector04))
