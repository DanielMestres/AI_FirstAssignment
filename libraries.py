import numpy as np

# Code provided by chatgpt. Funciona bien.

# Define two 2D arrays
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiply the two arrays using dot product
C = np.dot(A, B)
# Alternatively, you can use the @ operator
# C = A @ B

print(C)
