# Problem 1

# Create an Inverted index. Given a set of documents, an inverted index
# is a dictionary where each word is associated with a list of the document
# identifiers in which that word appears.

# Mapper Input
# The input is a 2-element list: [document_id, text], where document_id is a
# string representing a document identifier and text is a string representing
# the text of the document. The document text may have words in upper or lower
# case and may contain punctuation. You should treat each token as if it was a
# valid word; that is, you can just use value.split() to tokenize the string.

# Reducer Output
# The output should be a (word, document ID list) tuple where word is a String
# and document ID list is a list of Strings.

# You can test your solution to this problem using books.json:
# python inverted_index.py books.json
# You can verify your solution against inverted_index.json.

import MapReduce
import sys

# Part 1
# We create a MapReduce object that is used to pass data between the map
# function and the reduce function, you won't need to use this object directly.
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Part 2
# The mapper function tokenizes each document and emits a key-value pair.
# The input is a 2-element list: [document_id, text], where document_id is a
# string representing a document identifier and text is a string representing
# the text of the document. The document text may have words in upper or lower
# case and may contain punctuation. You should treat each token as if it was a
# valid word; that is, you can just use value.split() to tokenize the string.
# The Mapper Function
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    word_list = list()
    for word in words:
        if word not in word_list:
            word_list.append(word)
            mr.emit_intermediate(word, key)

# Part 3
# The output should be a (word, document ID list) tuple where word is a String
# and document ID list is a list of Strings.
# The Reducer Function
def reducer(key, list_of_values):
    doc_list = list()
    for value in list_of_values:
        if value not in doc_list:
            doc_list.append(value)
    mr.emit((key, doc_list))

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
