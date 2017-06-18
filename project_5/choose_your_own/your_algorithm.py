#!/usr/bin/python

import matplotlib.pyplot as plt
from time import time
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


################## KNN ##################

def classify(features_train, labels_train): 
    from sklearn.neighbors import KNeighborsClassifier as knnc

    clf = knnc(n_neighbors = 3, leaf_size = 50,  
                weights = "distance", 
                algorithm = "ball_tree", 
                metric = "chebyshev") # classifier 
    clf = clf.fit(features_train, labels_train)

    return clf

##################KNN-ACCURACY#############################
def KNNAccuracy(features_test, labels_test): 
    from sklearn.metrics import accuracy_score #accuracy score

    t0 = time() # intial run time
    clf = classify(features_train,labels_train) #create classifier
    print "training time:", round(time() - t0, 3), "s"

    t1 = time() #create time 
    pred = clf.predict(features_test) #create prediction
    print "predictive time:", round(time() - t1, 3), "s"

    accuracy = accuracy_score(labels_test, pred) # accuracy test

    return {"You accuracy is": accuracy}



################## Main ##################
def main():

    clf = classify(features_train, labels_train) 
    accuracy = KNNAccuracy(features_test,labels_test)
    print clf
    print accuracy

    try: 
        prettyPicture(clf, features_test, labels_test)
        plt.show()
    except NameError: 
        pass

##### run code ##### 

if __name__ == '__main__':
    main()


