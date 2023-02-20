import time
from array import *

# Declare 1d and 2d arrays
test_array_1 = [[1, 2, 3, 4]]
test_array_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

r_a1 = len(test_array_1)
c_a1 = len(test_array_1[0])
r_a2 = len(test_array_2)
c_a2 = len(test_array_2[0])

# Check for compatibility
if(c_a1 != r_a2):
    print("Arrays not product compatible!")
else:
    # Declare product array with correct dimensions
    result = [[0 for x in range(c_a2)] for y in range(r_a1)]

    start_time = time.time()

    # Calculate product
    for i in range(r_a1):
        for j in range(c_a2):
            for k in range(c_a1):
                result[i][j] += test_array_1[i][k] * test_array_2[k][j]

    end_time = time.time()

    print(result)
    print("Execution time: ", end_time - start_time, " seconds")
