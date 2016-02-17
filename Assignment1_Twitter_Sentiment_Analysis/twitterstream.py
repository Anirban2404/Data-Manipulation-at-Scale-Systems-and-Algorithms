# Problem 1: Get Twitter Data
# Run the following and make sure you see data flowing and that no errors occur.
# $ python twitterstream.py > output.txt
# This command pipes the output to a file. Stop the program with Ctrl-C,
# but wait at least 3 minutes for data to accumulate.
# Keep the file output.txt for the duration of the assignment; we will be reusing it in later problems.
# Don't use someone else's file; we will check for uniqueness in other parts of the assignment.

import oauth2 as oauth
import urllib2 as urllib

# See assignment1.html instructions or README for how to get these credentials
# Twitter Details
api_key = "jd7XRRkik0Bh8ovGdTmyNCT4F"
api_secret = "uhBPOYcxQmozusO1IRbUPWKCy9LPrhE8klN4qTtspUdoT7CWjl"
access_token_key = "89170652-4G3W9s09dH7UQUBpeh1dk0OYyf0OCVQFd6J9SVeAx"
access_token_secret = "MufnQJbguKZXpeAu6OkjH7YhUhoGLSmfIPD18TiqWSG39"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

# Writing the data to file
filename = "output.txt"
target = open(filename, 'w')
def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  count =0
  for line in response:
    #print line.strip()
    line = line.strip()
    target.write(line)
    target.write("\n")
    count = count + 1
    if count == 5000: exit()

if __name__ == '__main__':
  fetchsamples()
