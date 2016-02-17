# Problem 6: Top ten hash tags

# Write a Python script top_ten.py that computes the ten most frequently
# occurring hashtags from the data you gathered in Problem 1.

# Your script will be run from the command line like this:

# $ python top_ten.py <tweet_file>
# You should assume the tweet file contains data formatted the same way
# as the livestream data.

# In the tweet file, each line is a Tweet object, as described in the twitter
# documentation. To find the hashtags, you should not parse the text field;
# the hashtags have already been extracted by twitter.

# Your script should print to stdout each hashtag-count pair,
# one per line, in the following format:

# Your script should print output to stdout. Each line of output should contain
# a hashtag, followed by a space, followed by the frequency of that hashtag in
# the entire file. There should be one line per unique hashtag in the entire file.
# Each line should be in the format <hashtag:string> <frequency:float>

# For example, if you have the pair (bar, 30) in Python it should appear in the output as:
# bar 30
# What to turn in: the file top_ten.py

import sys
import json

def top_ten(tweet_file):
    print 'Finding Top10 hashtags...'
    # initialize an empty dictionary
    counts = dict()

    # Parsing the JSON line by line
    for line in tweet_file:
        tweet = json.loads(line)
        # Extracting the hashtag from JSON
        if 'entities' in tweet:
            if 'hashtags' in tweet['entities']:
                if len (tweet['entities']['hashtags']) > 0:
                    hashtags = tweet['entities']['hashtags']
                    for hashtag in hashtags:
                        tag = str(hashtag['text'].encode('utf-8'))
                        # Count frequency of every hashtag
                        counts[tag] = counts.get(tag,0) + 1

    # The required top number of tags
    top = 10
    # Compute top ten hashtags
    for top_tag in range(top):
        # Sort the hashtags
		print sorted(counts.items(), key=lambda top_tag:top_tag[1], reverse=True)[top_tag][0],
		print ' ',
		print float(sorted(counts.items(), key=lambda top_tag:top_tag[1], reverse=True)[top_tag][1])
    return

def lines(fp):
    print "Length:", str(len(fp.readlines()))

def main():
    try:
        # Pass the second file name
        tweet_file = open(sys.argv[1])
    except:
        # If the input is blank
        tweet_file = open("output.txt")
        # tweet_file = open("problem_1_submission.txt")

    # Calling the function for Sentiment Analysis
    top_ten(tweet_file)
    # Setting the file pointer at initial position
    tweet_file.seek(0)
    # Length of each file
    lines(tweet_file)

if __name__ == '__main__':
    main()