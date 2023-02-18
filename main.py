from array import *

# Arrays should be m*n and n*k to be product compatible
def iterative_Product(a1, a2):
    r_a1 = len(a1)
    c_a1 = len(a1[0])
    r_a2 = len(a2)
    c_a2 = len(a2[0])

    # Check for compatibility
    if(c_a1 != r_a2):
        print("Arrays not product compatible!")
        return

    # Declare product array with correct dimensions
    result = [[0 for x in range(c_a2)] for y in range(r_a1)]

    # Calculate product
    for i in range(r_a1):
        for j in range(c_a2):
            for k in range(c_a1):
                result[i][j] += a1[i][k] * a2[k][j]

    print(result)


# Declare 1d and 2d arrays
test_array_1 = [[1, 2, 3, 4]]
test_array_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

iterative_Product(test_array_1, test_array_2)

