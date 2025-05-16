

import numpy as np
from numpy.linalg import eig

'''
1. Create a 3 x 3 matrix A and a 3 x 1 vector B :
   A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
   B = np.array([1, 2, 3])
   Tasks:
   - Perform matrix-vector multiplication  A X B.
   - Calculate the trace of matrix  A  (sum of diagonal elements).
   - Find the eigenvalues and eigenvectors of A.
'''

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([1, 2, 3])

#Matrix-Vector multiplication
AxB = A @ B

#Trace of Matrix A (diagonal)
trace_A = np.trace(A)

#Eigenvalues and eigenvectors of A
eigenvalues_A, eigenvectors_A = eig(A)

#displaying the values 
print("\nMultiplication of matrix :",AxB)
print("\nTrace of Matrix (diagonal):", trace_A)
print("\nEigenvalues :\n", eigenvalues_A)
print("\nEigenvectors :\n", eigenvectors_A)

'''
2. Replace the last row of matrix A with [10, 11, 12] and:
   - Compute the determinant of the updated matrix A.
   - Identify if the updated matrix is singular or non-singular.
'''

#Replacing the last row of the matrix A 
A[-1] = [10,11,12]
print("\nUpdated Matrix:\n",A)

# Calculating the Determinant
det = np.linalg.det(A) 

#Check if Singular
if np.isclose(det, 0):
    print("\nMatrix is singular (non-invertible).")
else:
    print("\nMatrix is non-singular (invertible).")

'''
1. Verify the invertibility of the updated matrix A:
   - Check if the determinant is non-zero.
   - If invertible, calculate the inverse of A.
'''

#After verifying in the previous model. Now Inverse it.
if np.isclose(det, 0):
    print("\nMatrix is singular (non-invertible).")
else:
    A_inv = np.linalg.inv(A)
    print("\nInverse of A:\n", A_inv) #This print statement would not work since the updated matrix is singular

'''
2. Solve a system of linear equations A x X = B, where:
   - A is the updated matrix.
'''


if np.isclose(det, 0):
    print("\nMatrix A is singular (non-invertible). Cannot solve the system.")
else:
    # Solve for X
    X = np.linalg.solve(A, B)
    print("\nSolution X:", X)# Aga9n this would not print because matrix A is singular. The determinant is 0

'''
1. Create a 4 x 4 matrix C with random integers between 1 and 20:
  
C = np.random.randint(1, 21, size=(4, 4))

Tasks
- Compute the rank of C.
- Extract the submatrix consisting of the first 2 rows and last 2 columns of C.
- Calculate the Frobenius norm of C.
'''

C = np.random.randint(1, 21, size=(4, 4))

#Computing the Rank of C
rank_C = np.linalg.matrix_rank(C)
print("\nRank of C:", rank_C)
print ("\nMatrix C:\n",C)

#Extracting the Submatrix
submatrix = C[:2, -2:]
print("\nSubmatrix of matrix C:\n",submatrix)

#Calculating the Frobenius norm . Why such complicated name . I just have to square every individual element and then add each element, then square root it .huh!
fro_norm = np.linalg.norm(C, 'fro')
print("\n Frobenious Norm:",fro_norm)


'''
2. Perform matrix multiplication between A (updated to 3 x 3) and C (trimmed to 3 x 3):
- Check if the multiplication is valid. If not, reshape C to make it compatible with A.
'''

# Check shapes
# print("Shape of A:", A.shape)
# print("Shape of C:", C.shape)

C = C[:3, :3]
# Multiply if valid
if A.shape[1] == C.shape[0]:
    result = np.dot(A, C)  # or A @ C
    print("Matrix Multiplication Result:\n", result)
else:
    print("Matrix shapes are incompatible. Reshaping needed.")

'''
1. Create a dataset as a 5 x 5 matrix D, where each column represents a feature, and each row represents a data point:
D = np.array([[3, 5, 7, 9, 11],
              [2, 4, 6, 8, 10],
              [1, 3, 5, 7, 9],
              [4, 6, 8, 10, 12],
              [5, 7, 9, 11, 13]])
Tasks
- Standardize D column-wise (mean = 0, variance = 1).
- Compute the covariance matrix of D.
- Perform Principal Component Analysis (PCA):
- Find the eigenvalues and eigenvectors of the covariance matrix.
- Reduce D to 2 principal components.
'''

D = np.array([[3, 5, 7, 9, 11],
                [2, 4, 6, 8, 10],
                [1, 3, 5, 7, 9],
                [4, 6, 8, 10, 12],
                [5, 7, 9, 11, 13]])

# Standardize each column
D_mean = D.mean(axis=0)
D_std = D.std(axis=0)

D_standardized = (D - D_mean) / D_std
print("\nStandardized D:\n", D_standardized)

# Compute the covariance matrix
cov_matrix_D = np.cov(D, rowvar=False)
print("\nCovariance Matrix of D:\n", cov_matrix_D)

#Find the eigenvalues and eigenvectors of the covariance matrix.
eigenvalues_D, eigenvectors_D = eig(cov_matrix_D)
print("\nEigenvalues :\n", eigenvalues_D)
print("\nEigenvectors :\n", eigenvectors_D)

# Step 2: Compute the covariance matrix
cov_matrix = np.cov(D_standardized, rowvar=False)
print("\nCovariance Matrix of D:\n", cov_matrix)

# Step 3: Find the eigenvalues and eigenvectors of the covariance matrix
eigenvalues_D_standardized, eigenvectors_D_standardized = eig(cov_matrix)
print("\nEigenvalues :\n", eigenvalues_D_standardized)
print("\nEigenvectors :\n", eigenvectors_D_standardized)

# Step 4: Sort the eigenvalues and eigenvectors in descending order
sorted_indices = np.argsort(eigenvalues_D_standardized)[::-1]
eigenvalues_D_sorted = eigenvalues_D_standardized[sorted_indices]
eigenvectors_D_sorted = eigenvectors_D_standardized[:, sorted_indices]

# Step 5: Select the top 2 eigenvectors (principal components)
top_2_eigenvectors = eigenvectors_D_sorted[:, :2]
print("\nTop 2 Eigenvectors (Principal Components):\n", top_2_eigenvectors)

# Step 6: Project the standardized data onto the top 2 principal components
D_reduced = D_standardized @ top_2_eigenvectors
print("\nData reduced to 2 principal components:\n", D_reduced)

