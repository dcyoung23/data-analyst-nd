#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string
from pprint import pprint

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)
        #print text_string
        ### project part 2: comment out the line below
        #words = text_string
        text_string = text_string.replace("\n"," ")
        text_string = text_string.replace("\r"," ")

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        stemmer = SnowballStemmer("english")

        #l = text_string.split(" ")
        l = text_string.strip().split()
        #pprint(l)

        #print words
        for word in l:
            #word = word.strip()
            #print 'A:' + word + ':A'
            if len(word) > 0:
                word_stem = stemmer.stem(word)

                #print 'A:' + word_stem + ':A'
                #print word
                if len(words) == 0:
                    words = words + word_stem
                else:
                    words = words + " " + word_stem
        
    return words

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()

