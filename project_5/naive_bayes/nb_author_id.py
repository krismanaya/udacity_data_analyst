#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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




#########################################################
### your code goes here ###
def NBAccuracy(features_train, features_test, labels_train, labels_test): 
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score

    
    clf  = GaussianNB() # create classifier 
    t0 = time() #create initial time 
    clf.fit(features_train, labels_train) #create the fitness of classifier 
    print "training time:", round(time() - t0, 3), "s"

    t1 = time() #create time 
    pred = clf.predict(features_test)
    print "predictive time:", round(time() - t1, 3), "s"


    accuracy = accuracy_score(labels_test, pred)

    return {"You accuracy is": accuracy}
#########################################################

def main(): 
    accuracy = NBAccuracy(features_train, features_test, labels_train, labels_test)
    print accuracy

##### run code ##### 

if __name__ == '__main__':
    main() #show output. 


