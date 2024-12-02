#  A two-dimensional array contains different integer numbers.
#  Define a function f(array) that returns True if the row and column numbers
#  for the smallest value in the array are equal, and False otherwise. Example:

# f([[7,8],[5,3],[9,4]])  True     # 3, row 1, col 1
# f([[7,8,5,3],[9,4,2,6]])  False  # 2, row 1, col 2

def f(matrix):
    min = float('inf')
    rowLen = len(matrix)
    columnLen = len(matrix[0])
    row = 0
    column = 0

    for i in range(rowLen):
        for j in range(columnLen):
            if matrix[i][j] < min:
                min = matrix[i][j]
                row = i
                column = j

    if row == column:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f([[7,8],[5,-3],[9,4]]))
    print(f([[7,8,5,3],[9,4,2,6]]))
