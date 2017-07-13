#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
from time import time
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
### in labels_test True = 1, False = 0. 


from sklearn import cross_validation

### create a test an train cv
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size = 0.3, random_state = 42)


### Decision Tree Clssifier

def classify(features_train, labels_train): 

    from sklearn import tree 

    clf = tree.DecisionTreeClassifier() ### classifier 
    clf = clf.fit(features_train, labels_train) #### fit training set 
    
    return clf


### Create Accuracy Metric

def DTAccuracy(features_test, labels_test): 
    from sklearn.metrics import accuracy_score #accuracy score
    from sklearn.metrics import confusion_matrix


    t0 = time() # intial run time
    clf = classify(features_train,labels_train) #create classifier
    print "training time:", round(time() - t0, 3), "s"

    t1 = time() #create time 
    pred = clf.predict(features_test) #create prediction
    print "predictive time:", round(time() - t1, 3), "s"

    accuracy = accuracy_score(labels_test, pred) # accuracy test

    return {"You accuracy is": accuracy}


def main():
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import precision_score
    from sklearn.metrics import recall_score
    
    clf = classify(features_train, labels_train)
    accuracy = DTAccuracy(features_test,labels_test)
    pred = clf.predict(features_test) #create prediction
    print "confusion matrix", confusion_matrix(labels_test,pred)
    print "precision score", precision_score(labels_test, pred)
    print "recall score", recall_score(labels_test,pred)
    print clf 
    print accuracy

    predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
    true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
    print "practice cm", confusion_matrix(true_labels, predictions)
    print "practice precision", precision_score(true_labels, predictions)
    print "practice recall", recall_score(true_labels, predictions)
    precision = precision_score(true_labels, predictions)
    recall = recall_score(true_labels, predictions)
    F_1 = 2*(precision*recall)/(precision + recall)
    print "F-1 score", F_1
    
    # count_poi = 0 
    # not_poi = 0
    # for poi in labels_test: 
    #     if poi == 1.0: 
    #         count_poi += 1
    #     else: 
    #         not_poi += 1
    # print "total", count_poi + not_poi
    # print "not_poi", not_poi
    # print "accuracy", not_poi / float(len(labels_test))
    # print "poi", count_poi

    # count_train_poi = 0 
    # count_train_not_poi  = 0 
    # for train_poi in labels_train: 
    #     if train_poi == 1.0: 
    #         count_train_poi += 1 
    #     else: 
    #         count_train_not_poi +=1
    # print "poi", count_train_poi
    # print "not poi", count_train_not_poi



    
##### run code ##### 

if __name__ == '__main__':
    main() 
