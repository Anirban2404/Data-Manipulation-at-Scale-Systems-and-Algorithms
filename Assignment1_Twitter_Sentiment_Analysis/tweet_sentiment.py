# Problem 2: Derive the sentiment of each tweet

# For this part, you will compute the sentiment of each tweet based
# on the sentiment scores of the terms in the tweet. The sentiment of
# a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.
#
# You are provided with a skeleton file tweet_sentiment.py which accepts
# two arguments on the command line: a sentiment file and a tweet file like
# the one you generated in Problem 1. You can run the skeleton program like this:

# $ python tweet_sentiment.py AFINN-111.txt output.txt
# The file AFINN-111.txt contains a list of pre-computed sentiment scores.
# Each line in the file contains a word or phrase followed by a sentiment score.
# Each word or phrase that is found in a tweet but not found in AFINN-111.txt should be
# given a sentiment score of 0. See the file AFINN-README.txt for more information.

# To use the data in the AFINN-111.txt file, you may find it useful to build
# a dictionary. Note that the AFINN-111.txt file format is tab-delimited, meaning
# that the term and the score are separated by a tab character. A tab character can be
# identified a "\t".The following snippet may be useful:

'''
afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

print scores.items() # Print every (term, score) pair in the dictionary
'''

# The data in the tweet file you generated in Problem 1 is represented as JSON,
# which stands for JavaScript Object Notation. It is a simple format for representing
# nested structures of data --- lists of lists of dictionaries of lists of .... you get the idea.

# Each line of output.txt represents a streaming message. Most, but not all, will be tweets.
# (The skeleton program will tell you how many lines are in the file.)

# It is straightforward to convert a JSON string into a Python data structure;
# there is a library to do so called json.

# To use this library, add the following to the top of tweet_sentiment.py
# import json
# Then, to parse the data in output.txt, you want to apply the function
# json.loads to every line in the file.

# This function will parse the json data and return a python data stucture;
# in this case, it returns a dictionary. If needed, take a moment to read the
# documentation for Python dictionaries.

# You can read the Twitter documentation to understand what information each tweet
# contains and how to access it, but it's not too difficult to deduce the structure
# by direct inspection.

# Your script should print to stdout the sentiment of each tweet in the file,
# one numeric sentiment score per line. The first score should correspond to the
# first tweet, the second score should correspond to the second tweet, and so on.
# If you sort the scores, they won't match up. If you sort the tweets,
# they won't match up. If you put the tweets into a dictionary, the order will not be preserved.
# Once again: The nth line of the file you submit should contain only a single number
# that represents the score of the nth tweet in the input file!

# NOTE: You must provide a score for every tweet in the sample file, even if that score is zero.
# You can assume the sample file will only include English tweets and no other types of streaming messages.

# To grade your submission, we will run your program on a tweet file formatted the same
# way as the output.txt file you generated in Problem 1.

# Hint: This is real-world data, and it can be messy! Refer to the twitter documentation
# to understand more about the data structure you are working with. Don't get discouraged,
# and ask for help on the forums if you get stuck!

# What to turn in: The file tweet_sentiment.py after you've verified that it returns the correct answers.

import sys
import json

def sentiment_analysis(sent_file,tweet_file):
    print 'Analyzing Sentiments...'
   # initialize an empty dictionary
    scores = dict()
    # Filling the dictionary with emotion score
    for line in sent_file:
        term,score = line.split("\t")
        scores[term] = int(score)

    # Parsing the JSON line by line
    for line in tweet_file:
        tweet = json.loads(line)
        sentiment = 0
        if 'text' in tweet:
            # Extracting the text from wach line
            text = tweet['text'].lower().strip()
            # Extracting the words
            words = text.split()
            for word in words:
                # If the emotion_score file has the word
                if scores.has_key(word):
                    # Calculating the sentiment value
                    sentiment = sentiment + scores[word]

        print sentiment
    return

def lines(fp):
    print "Length:", str(len(fp.readlines()))

def main():
    try:
        # Pass the first file name
        sent_file = open(sys.argv[1])
    except:
        # If the input is blank
        sent_file = open("AFINN-111.txt")
    try:
        # Pass the second file name
        tweet_file = open(sys.argv[2])
    except:
        # If the input is blank
        tweet_file = open("output.txt")

    # Calling the function for Sentiment Analysis
    sentiment_analysis(sent_file,tweet_file)
    # Setting the file pointer at initial position
    sent_file.seek(0)
    tweet_file.seek(0)
    # Length of each file
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()