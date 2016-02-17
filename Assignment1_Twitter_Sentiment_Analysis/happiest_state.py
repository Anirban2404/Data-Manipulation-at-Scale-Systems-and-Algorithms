# Problem 5: Which State is happiest?

# Write a Python script happiest_state.py that returns
# the name of the happiest state as a string.

# Your script happiest_state.py should take a file of tweets as input.
# It will be called from the command line like this:

# $ python happiest_state.py <sentiment_file> <tweet_file>
# The file AFINN-111.txt contains a list of pre-computed sentiment score.

# Assume the tweet file contains data formatted the
# same way as the livestream data.

# It's a good idea to make use of your solution to Problem 2.
# There are different ways you might assign a location to a tweet. Here are three:

# Use the coordinates field (a part of the place object, if it exists),
# to geocode the tweet. This method gives the most reliable location information,
# but unfortunately this field is not always available and you must figure out
# some way of translating the coordinates into a state.

# Use the other metadata in the place field. Much of this information is
# hand-entered by the twitter user and may not always be present or reliable,
# and may not typically contain a state name.

# Use the user field to determine the twitter user's home city and state.
# This location does not necessarily correspond to the location where the
# tweet was posted, but it's reasonable to use it as a proxy.

# You are free to develop your own strategy for determining
# the state that each tweet originates from.

# You may find it useful to use this python dictionary of state abbreviations.

# You can ignore any tweets for which you cannot assign a location in the United States.

# In this file, each line is a Tweet object, as described in the twitter documentation.

# Note: Not every tweet will have a text field --- again, real data is dirty!
# Be prepared to debug, and feel free to throw out tweets that your code can't
# handle to get something working. For example, you might choose to ignore
# all non-English tweets.

# Your script should print the two letter state abbreviation of the state with
# the highest average tweet sentiment to stdout.

# Note that you may need a lot of tweets in order to get enough tweets with
# location data. Let the live stream run for a while if you wish.

# Your script will not have access to the Internet, so you cannot rely on
# third party services to resolve geocoded locations!

# What to turn in: The file happiest_state.py

import sys
import json

def happy_analysis(sent_file,tweet_file):
    print 'Finding Happiest State...'
   # initialize an empty dictionary
    scores = dict()
    counts = dict()
    # Filling the dictionary with emotion score
    for line in sent_file:
        term,score = line.split("\t")
        scores[term] = int(score)

    # Parsing the JSON line by line
    for line in tweet_file:
        tweet = json.loads(line)
        sentiment = 0
        if 'place' in tweet and 'text' in tweet:
            # Extracting the text from wach line
            if tweet['place'] is not None:
                place = tweet['place']['full_name'].strip().encode('utf-8')
                #print place
                if tweet['place']['country'] == 'United States':
                    # print place
                    # Extracting the states
                    states = place.strip().encode('utf-8').split(',')
                    if len(states[1].strip()) == 2:
                        state= states[1]
                        # Extracting text from tweets
                        text = tweet['text'].lower().strip()
                        # Extracting the words
                        words = text.split()
                        for word in words:
                            # If the emotion_score file has the word
                             #print word
                            if scores.has_key(word):
                                # Calculating the sentiment value
                                sentiment = sentiment + scores[word]
                                counts[state] = counts.get(state,0) + sentiment

    max_happy_score = 0
    # Finding the maximum happy score and state
    for state, happy_score in counts.items():
        if happy_score > max_happy_score:
            max_happy_score = happy_score
            most_happy_state = state
    print 'HAPPIEST STATE:', most_happy_state, 'with SCORE:', max_happy_score
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
        # tweet_file = open("problem_1_submission.txt")

    # Calling the function for Sentiment Analysis
    happy_analysis(sent_file,tweet_file)

    # Setting the file pointer at initial position
    sent_file.seek(0)
    tweet_file.seek(0)

    # Length of each file
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()