# Problem 3

# Consider a simple social network dataset consisting of a set of
# key-value pairs (person, friend) representing a friend relationship
# between two people. Describe a MapReduce algorithm to count the
# number of friends for each person.

# Map Input
# Each input record is a 2 element list [personA, personB] where personA
# is a string representing the name of a person and personB is a string
# representing the name of one of personA's friends. Note that it may or
# may not be the case that the personA is a friend of personB.

# Reduce Output
# The output should be a pair (person, friend_count) where person is a
# string and friend_count is an integer indicating the number of friends
# associated with person.

# You can test your solution to this problem using friends.json:
# $ python friend_count.py friends.json
# You can verify your solution by comparing your result with the file friend_count.json.

import MapReduce
import sys

# Part 1
# We create a MapReduce object that is used to pass data between the map
# function and the reduce function, you won't need to use this object directly.
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Part 2
# Each input record is a 2 element list [personA, personB] where personA
# is a string representing the name of a person and personB is a string
# representing the name of one of personA's friends. Note that it may or
# may not be the case that the personA is a friend of personB.
# The Mapper Function
def mapper(record):
    # key: person identifier
    key = record[0]
    mr.emit_intermediate(key, 1)

# Part 3
# The output should be a pair (person, friend_count) where person is a
# string and friend_count is an integer indicating the number of friends
# associated with person.
# The Reducer Function
def reducer(key, list_of_values):
    # key: friend
    # value: list of friends
    total = 0
    for value in list_of_values:
      total += value
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
        input_file = "data\\friends.json"
        inputdata = open(input_file)
    mr.execute(inputdata, mapper, reducer)
