# -*- coding: utf-8 -*-
"""
Data Mining with Twitter.
Term Frequencies.
Author: Ryan Nanson.
"""

import operator 
import json
from collections import Counter
from nltk.corpus import stopwords
import string
from nltk import bigrams 
 
fname = 'mytweets.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_all = [term for term in preprocess(tweet['text'])]
        # Update the counter
        count_all.update(terms_all)
    # Print the first 5 most frequent words
    print(count_all.most_common(5))

## Remove stop strings (rt=retweet, via=via author)
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]

# Count terms only once, equivalent to Document Frequency
terms_single = set(terms_all)

# Count hashtags only
terms_hash = [term for term in preprocess(tweet['text']) 
              if term.startswith('#')]
              
# Count terms without hashtags or mentions
terms_only = [term for term in preprocess(tweet['text']) 
              if term not in stop and
              not term.startswith(('#', '@'))] 
              # mind the ((double brackets))
              # startswith() takes a tuple (not a list) if 
              # we pass a list of inputs

## Count tuples using adjacent tokens
terms_bigram = bigrams(terms_stop)
