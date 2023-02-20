import time
import numpy as np

# Define two 2D arrays
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Add exec time measurement
start_time = time.time()

# Multiply the two arrays using dot product
C = np.dot(A, B)

end_time = time.time()

print(C)
print("Execution time: ", end_time - start_time, " seconds")
