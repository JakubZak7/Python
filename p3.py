# (p3.py) A two-dimensional array contains the same number of rows and columns.
# Define a function f(array2D) that, for the given two-dimensional array array2D,
# returns True when the sum of the values in each row of the array is equal to the
# sum of the values in the corresponding column
# (e.g., the sum of the values in row 3 is equal to the sum of the values in column 3) ,
# and False otherwise. Example:

# f([[3,7,2],[4,2,5],[5,2,1]])  True
# f([[3,7,2],[4,2,5],[9,2,1]])  False

def f(array2D):

    arrayLen = len(array2D)

    for i in range(arrayLen):
        row_sum = sum(array2D[i])
        col_sum = sum(array2D[j][i] for j in range(arrayLen))

        if row_sum != col_sum:
            return False

    return True


if __name__ == '__main__':
    print(f([[3,7,2],
             [4,2,5],
             [5,2,1]]))

    print(f([[3,7,2],
             [4,2,5],
             [9,2,1]]))
