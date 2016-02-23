# Problem 4
# The relationship "friend" is often symmetric, meaning that if
# I am your friend, you are my friend. Implement a MapReduce algorithm
# to check whether this property holds. Generate a list of all
# non-symmetric friend relationships.

# Map Input
# Each input record is a 2 element list [personA, personB] where personA
# is a string representing the name of a person and personB is a string
# representing the name of one of personA's friends. Note that it may or
# may not be the case that the personA is a friend of personB.

# Reduce Output
# The output should be all pairs (friend, person) such that (person, friend)
# appears in the dataset but (friend, person) does not.

# You can test your solution to this problem using friends.json:
# $ python asymmetric_friendships.py friends.json
# You can verify your solution by comparing your result with the file
# asymmetric_friendships.json.

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
# The Mapper Functions
def mapper(record):
    # key: person identifier
    person = sorted(record)[0]
    friend = sorted(record)[1]
    frienship = str(person + "," + friend)
    mr.emit_intermediate(frienship,1)

# Part 3
# The output should be all pairs (friend, person) such that (person, friend)
# appears in the dataset but (friend, person) does not.
# The Reducer Function

def reducer(frienship, list_of_values):
    # key: person
    # value: list of friends
    # List the friends of that person
    total = 0
    friend = frienship.split(",")
    for val in list_of_values:
        total = total + val

    if (total == 1)  :
        mr.emit((friend[0],friend[1]))
        mr.emit((friend[1],friend[0]))


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