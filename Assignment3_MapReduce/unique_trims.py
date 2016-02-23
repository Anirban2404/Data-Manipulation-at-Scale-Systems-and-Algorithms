# Problem 5

# Consider a set of key-value pairs where each key is sequence id
# and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....

# Write a MapReduce query to remove the last 10 characters from each
# string of nucleotides, then remove any duplicates generated.

# Map Input
# Each input record is a 2 element list [sequence id, nucleotides]
# where sequence id is a string representing a unique identifier for the
# sequence and nucleotides is a string representing a sequence of nucleotides

# Reduce Output
# The output from the reduce function should be the unique trimmed nucleotide strings.

# You can test your solution to this problem using dna.json:
# $ python unique_trims.py dna.json
# You can verify your solution by comparing your result with the file unique_trims.json.

import MapReduce
import sys

# Part 1
# We create a MapReduce object that is used to pass data between the map
# function and the reduce function, you won't need to use this object directly.
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Part 2
# Each input record is a 2 element list [sequence id, nucleotides]
# where sequence id is a string representing a unique identifier for the
# sequence and nucleotides is a string representing a sequence of nucleotides
# The Mapper Function
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    length =  len(value)
    trim_val = value[:length - 10]
    mr.emit_intermediate(trim_val,1)

# Part 3
# The output from the reduce function should be the unique trimmed nucleotide strings.
# The Reducer Function
def reducer(key, list_of_values):
   mr.emit((key))

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
        input_file = "data\\dna.json"
        inputdata = open(input_file)
    mr.execute(inputdata, mapper, reducer)