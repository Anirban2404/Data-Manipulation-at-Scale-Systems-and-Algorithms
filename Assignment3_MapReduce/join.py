# Problem 2

# Implement a relational join as a MapReduce query
# Consider the following query:
'''
SELECT *
FROM Orders, LineItem
WHERE Order.order_id = LineItem.order_id
'''
# Your MapReduce query should produce the same result as this SQL query
# executed against an appropriate database.

# You can consider the two input tables, Order and LineItem, as one big
# concatenated bag of records that will be processed by the map function record by record.

# Map Input
# Each input record is a list of strings representing a tuple in the database.
# Each list element corresponds to a different attribute of the table

# The first item (index 0) in each record is a string that identifies the table
# the record originates from. This field has two possible values:

# "line_item" indicates that the record is a line item.
# "order" indicates that the record is an order.
# The second element (index 1) in each record is the order_id.
# LineItem records have 17 attributes including the identifier string.
# Order records have 10 elements including the identifier string.

# Reduce Output
# The output should be a joined record: a single list of length 27 that
# contains the attributes from the order record followed by the fields
# from the line item record. Each list element should be a string.

# You can test your solution to this problem using records.json:
# $ python join.py records.json
# You can can compare your solution with join.json.

import MapReduce
import sys

# Part 1
# We create a MapReduce object that is used to pass data between the map
# function and the reduce function, you won't need to use this object directly.
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Part 2
# Each input record is a list of strings representing a tuple in the database.
# Each list element corresponds to a different attribute of the table

# The first item (index 0) in each record is a string that identifies the table
# the record originates from. This field has two possible values:

# "line_item" indicates that the record is a line item.
# "order" indicates that the record is an order.
# The second element (index 1) in each record is the order_id.
# LineItem records have 17 attributes including the identifier string.
# Order records have 10 elements including the identifier string.
# The Mapper Function
def mapper(record):
    # key: join key
    # value: all others
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

# Part 3
# The output should be a joined record: a single list of length 27 that
# contains the attributes from the order record followed by the fields
# from the line item record. Each list element should be a string.
# The Reducer Function
def reducer(key, list_of_values):
    for value in list_of_values:
        order = list_of_values[0]
        if value is order: continue
        joined_list = order + value
        mr.emit((joined_list))

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
        input_file = "data\\records.json"
        inputdata = open(input_file)
    mr.execute(inputdata, mapper, reducer)
