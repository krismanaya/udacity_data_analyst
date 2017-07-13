#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from time import time

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

# from sklearn import tree 

# clf = tree.DecisionTreeClassifier() 
# clf = clf.fit(features, labels)

# pred = clf.predict(features)

# from sklearn.metrics import accuracy_score

# print accuracy_score(labels,pred)

### it's all yours from here forward!  

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



    t0 = time() # intial run time
    clf = classify(features_train,labels_train) #create classifier
    print "training time:", round(time() - t0, 3), "s"

    t1 = time() #create time 
    pred = clf.predict(features_test) #create prediction
    print "predictive time:", round(time() - t1, 3), "s"

    accuracy = accuracy_score(labels_test, pred) # accuracy test

    return {"You accuracy is": accuracy}


def main():
    
    clf = classify(features_train, labels_train)
    accuracy = DTAccuracy(features_test,labels_test)
    print clf 
    print accuracy


    
##### run code ##### 

if __name__ == '__main__':
    main() 
