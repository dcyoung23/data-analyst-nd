#!/usr/bin/python

import os
import pickle
import re
import sys

from pprint import pprint

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification

    the list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    the actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project

    the data is stored in lists and packed away in pickle files at the end

"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1

        #if temp_counter < 200:
        if temp_counter >= 0:
            path = os.path.join('..', path[:-1])
            #print path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            text = parseOutText(email)
            #if temp_counter == 1:
            #    print text
            #text = text.strip()

            ### use str.replace() to remove any instances of the words
            r = ["sara", "shackleton", "chris", "germani", "sshacklensf", "cgermannsf"]

            for word in r:
                text = text.replace(word,"")

            ### append the text to word_data
            word_data.append(text)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == "sara":
                f = 0
            elif name == "chris":
                f = 1
            from_data.append(f)

            email.close()

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

test = word_data[152]
#test = test.replace("\r","")
#test = test.replace("\n","")

print test

from nltk.corpus import stopwords
sw = stopwords.words("english")


### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tf.fit_transform(word_data)
#print tfidf_matrix
feature_names = tf.get_feature_names()

# 38757
print len(feature_names)

print feature_names[34597]

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(stop_words=sw)
#b = vectorizer.fit(word_data)
#b = vectorizer.transform(word_data)

b = vectorizer.fit_transform(word_data)
#print b

f = vectorizer.get_feature_names()

print len(f)






