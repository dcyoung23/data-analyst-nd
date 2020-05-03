#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# Test
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

print features_train.head()
print labels_train.head()
print features_test.head()

#########################################################
### your code goes here ###
from sklearn import svm

clf = svm.SVC(kernel='rbf',C=10000.0)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score

print accuracy_score(labels_test, pred)

#answer1 = pred[10]
#answer2 = pred[26]
#answer3 = pred[50]
#print answer1, answer2, answer3

Chris = [x for x in pred if x == 1]
print len(Chris)

#########################################################


