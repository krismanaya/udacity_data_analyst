#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

########################## SVM #################################
### we handle the import statement and SVC creation for you here


def SVMAccuracy(features_train, features_test, labels_train, labels_test): 


    from sklearn.svm import SVC

    #### Create a smaller data set #### 
    #features_train = features_train[:len(features_train)/100] 
    #labels_train = labels_train[:len(labels_train)/100] 

    clf = SVC(C = 10000.0, kernel="rbf") #train classifier with linear kernel. 

    
    t0 = time() #create initial time 
    clf.fit(features_train, labels_train) # create a fit. 
    print "training time:", round(time() - t0, 3), "s" #training time
    
    t1 = time() #create predictive time
    pred = clf.predict(features_test) # prediction from test. 
    print "predictive time:", round(time() - t1, 3), "s" #predictive time

    print("this is pred", (pred, len(pred))) #and an array of predictions. 

    chris_class = [] # list_chris
    sara_class = [] # list _sara

    for event in pred: # loop through predictions
        if event != 0: 
            chris_class.append(event) # append if not sarah
        else: 
            sara_class.append(event)  # append if not chris

    # print lenght of chris and chance
    print ("number of events for chris and percentage:", (len(chris_class),(float(len(chris_class))/float(len(pred))))) 

    # print lenght of sara and chance
    print ("number of events for chris and percentage:", (len(sara_class),(float(len(sara_class))/float(len(pred))))) 






    from sklearn.metrics import accuracy_score #import accuracy.
    acc = accuracy_score(pred, labels_test) #create accuracy

    print("pred[10]: ",pred[10]) #Chris 
    print("pred[26]: ",pred[26]) #Sara
    print("pred[50]: ",pred[50]) #Chris 
    
    return {"Your Accuracy Score": acc}


def main(): 
    print  SVMAccuracy(features_train, 
                       features_test, 
                       labels_train, 
                       labels_test) # create an output. 

#run code
if __name__ == '__main__': 
    main() # print accuracy


