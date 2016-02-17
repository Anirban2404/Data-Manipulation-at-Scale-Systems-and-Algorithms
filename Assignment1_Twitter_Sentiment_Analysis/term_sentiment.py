# Problem 3: Derive the sentiment of new terms
# In this part you will be creating a script that computes the sentiment
# for the terms that do not appear in the file AFINN-111.txt.

# Here's how you might think about the problem: We know we can use the
# sentiment-carrying words in AFINN-111.txt to deduce the overall sentiment of a tweet.
# Once you deduce the sentiment of a tweet, you can work backwards to deduce
# the sentiment of the non-sentiment carrying words that do not appear in AFINN-111.txt.
# For example, if the word soccer always appears in proximity with positive words
# like great and fun, then we can deduce that the term soccer itself carries a positive sentiment.

# Don't feel obligated to use it, but the following paper may be helpful for developing
# a sentiment metric. Look at the Opinion Estimation subsection of the Text Analysis section in particular.

# O'Connor, B., Balasubramanyan, R., Routedge, B., & Smith, N.
# From Tweets to Polls: Linking Text Sentiment to Public Opinion Time Series. (ICWSM), May 2010.

# You are provided with a skeleton file term_sentiment.py which accepts the same
# two arguments as tweet_sentiment.py and can be executed using the following command:

# $ python term_sentiment.py AFINN-111.txt output.txt
# Your script should print output to stdout. Each line of output should contain a term,
# followed by a space, followed by the sentiment. That is, each line should be in the
# format <term:string> <sentiment:float>

# For example, if you have the pair ("foo", 103.256) in Python, it should appear in the output as:
# foo 103.256
# The order of your output does not matter.

# What to turn in: The file term_sentiment.py
# How we will grade Part 3: We will run your script on a file that contains
# strongly positive and strongly negative tweets and verify that the non-sentiment-carrying
# terms in the strongly positive tweets are assigned a higher score than the
# non-sentiment-carrying terms in negative tweets. Your scores need not (and likely will not)
# exactly match any specific solution.

# If the grader is returning "Formatting error: ", make note of the line of text returned
# in the message. This line corresponds to a line of your output. The grader will generate
# this error if line.split() does not return exactly two items. One common source of this
# error is to not remove the two calls to the "lines" function in the solution template;
# this function prints the number of lines in each file. Make sure to check the first two
# lines of your output! (Some terms in AFINN are short phrases; we will not test your script
# using any multi-word combinations.)

import sys
import json

def term_sentiment_analysis(sent_file,tweet_file):
    print 'Analyzing Term Sentiments...'
   # initialize an empty dictionary
    scores = dict()
    # Initiating dictionary
    new_words = dict()
    counts = dict()
    # Filling the dictionary with emotion score
    for line in sent_file:
        term,score = line.split("\t")
        scores[term] = int(score)

    # Parsing the JSON line by line
    for line in tweet_file:
        tweet = json.loads(line)
        sentiment = 0
        if 'text' in tweet:
            # Extracting the text from each line
            text = tweet['text'].strip().lower().encode('utf-8')
            # Extracting the words
            words = text.split()
            for word in words:
                # If the emotion_score file has the word
                if scores.has_key(word):
                    # Calculating the sentiment value
                    sentiment = sentiment + scores[word]
                    counts[word] = counts.get(word,0) + 1

                else:
                    # If word exists increment the count,
                    # else enlist new word
                    counts[word] = counts.get(word,0) + 1

            for word in words:
                if sentiment > 0:
                    new_words[word] = new_words.get(word,0) + 1
                elif sentiment < 0:
                    new_words[word] = new_words.get(word,0) - 1
                else:
                    new_words[word] = new_words.get(word,0)

    # Printing by calculating term sentiment
    for word,sentiment in new_words.items():
        print word, float(sentiment/counts[word])
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
        # tweet_file = open("output.txt")
        tweet_file = open("problem_1_submission.txt")

    # Calling the function for Sentiment Analysis
    term_sentiment_analysis(sent_file,tweet_file)
    # Setting the file pointer at initial position
    sent_file.seek(0)
    tweet_file.seek(0)
    # Length of each file
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()