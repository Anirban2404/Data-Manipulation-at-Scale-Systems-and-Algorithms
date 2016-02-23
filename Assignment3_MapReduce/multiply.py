# Problem 6
# Assume you have two matrices A and B in a sparse matrix format,
# where each record is of the form i, j, value. Design a MapReduce
# algorithm to compute the matrix multiplication A x B

# Map Input
# The input to the map function will be a row of a matrix represented
# as a list. Each list will be of the form [matrix, i, j, value] where
# matrix is a string and i, j, and value are integers.

# The first item, matrix, is a string that identifies which matrix the
# record originates from. This field has two possible values: "a"
# indicates that the record is from matrix A and "b" indicates that
# the record is from matrix B.

# Reduce Output
# The output from the reduce function will also be a row of the result
# matrix represented as a tuple. Each tuple will be of the form (i, j, value)
# where each element is an integer.

# You can test your solution to this problem using matrix.json:
# $ python multiply.py matrix.json
# You can verify your solution by comparing your result with the file multiply.json.

import MapReduce
import sys

# Part 1
# We create a MapReduce object that is used to pass data between the map
# function and the reduce function, you won't need to use this object directly.
mr = MapReduce.MapReduce()
N = 5
# =============================
# Do not modify above this line

# Part 2
# The input to the map function will be a row of a matrix represented
# as a list. Each list will be of the form [matrix, i, j, value] where
# matrix is a string and i, j, and value are integers.

# The first item, matrix, is a string that identifies which matrix the
# record originates from. This field has two possible values: "a"
# indicates that the record is from matrix A and "b" indicates that
# the record is from matrix B.
# The Mapper Function
def mapper(record):
    # // value is ("a", row_i, col_j, val_ij) or ("b", row_j, col_k, val_jk)
    matrix = record[0]
    if matrix == "a":
        for k in range(N):
            row_i = record[1]
            col_j = record[2]
            val_ij = record[3]
        mr.emit_intermediate((row_i, k), (matrix, col_j, val_ij))
    else:
        for l in range(N):
            row_j = record[1]
            col_k = record[2]
            val_jk = record[3]
        mr.emit_intermediate((l, col_k), (matrix, row_j, val_jk))

# Part 3
# The output from the reduce function will also be a row of the result
# matrix represented as a tuple. Each tuple will be of the form (i, j, value)
# where each element is an integer.
# The Reducer Function
def reducer(key, list_of_values):
    # key: word
    # value: list of matrix values
    left_matrix_value = [(col_j, val_ij) for (matrix, col_j, val_ij) in list_of_values if matrix == 'a']
    right_matrix_value = [(row_j, val_jk) for (matrix, row_j, val_jk) in list_of_values if matrix == 'b']

    sum_result = 0

    for item_Left in left_matrix_value:
        for item_Right in right_matrix_value:
            if item_Left[0] == item_Right[0]:
                sum_result += item_Left[1] * item_Right[1]
    mr.emit((key[0], key[1], sum_result))

# Part 4
# The code loads the json file and executes the MapReduce query which
# prints the result to stdout.
# Do not modify below this line
# =============================
if __name__ == '__main__':
    try:
        # Pass the first file name
        inputdata = open(sys.argv[1])
    except:
        # If the input is blank
        input_file = "data\\matrix.json"
        inputdata = open(input_file)
    mr.execute(inputdata, mapper, reducer)