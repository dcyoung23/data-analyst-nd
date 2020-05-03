pred = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
labels_test = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

from sklearn.metrics import precision_score
print precision_score(labels_test, pred)  

from sklearn.metrics import recall_score
print recall_score(labels_test, pred)

combined = labels_test + pred

print combined

