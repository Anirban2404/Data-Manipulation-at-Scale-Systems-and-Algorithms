import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

# Part 1
# We create a MapReduce object that is used to pass data between the map
# function and the reduce function, you won't need to use this object directly.
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Part 2
# The mapper function tokenizes each document and emits a key-value pair.
# The key is a word formatted as a string and the value is the integer 1
# to indicate an occurrence of word.
# The Mapper Function
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, 1)

# Part 3
# The reducer function sums up the list of occurrence counts and emits
# a count for word. Since the mapper function emits the integer 1 for each
# word, each element in the list_of_values is the integer 1.

# The list of occurrence counts is summed and a (word, total) tuple is
# emitted where word is a string and total is an integer.
# The Reducer Function
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

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
        input_file = "data\\books.json"
        inputdata = open(input_file)
    mr.execute(inputdata, mapper, reducer)
