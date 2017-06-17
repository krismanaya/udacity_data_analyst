#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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


########################################################
def DTAccuracy(features_test, labels_test): 
    from sklearn.metrics import accuracy_score #accuracy score



    t0 = time() # intial run time
    clf = classify(features_train,labels_train) #create classifier
    print "training time:", round(time() - t0, 3), "s"

    t1 = time() #create time 
    pred = clf.predict(features_test) #create prediction
    print "predictive time:", round(time() - t1, 3), "s"

    accuracy = accuracy_score(labels_test, pred) # accuracy test

    return {"You accuracy is": accuracy}


def classify(features_train, labels_train): 
    from sklearn import tree # import dt

    clf = tree.DecisionTreeClassifier(min_samples_split = 40) # create classifier
    clf = clf.fit(features_train, labels_train) # fit training set 
    
    return clf

#########################################################

def main():
    
    clf = classify(features_train, labels_train)
    accuracy = DTAccuracy(features_test,labels_test)
    print len(features_train[0]) #length of the rows of features
    print clf 
    print accuracy
    
##### run code ##### 

if __name__ == '__main__':
    main() #show output. 


########################################################

