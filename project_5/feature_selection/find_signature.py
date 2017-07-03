#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()
names = vectorizer.get_feature_names() 
print names[21323] #prints the name of feature_importance

### example:  print "feature no. {}: {} ({})".format(i+1,features_list[indices[i]+1],importances[indices[i]])
### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here

### Tree classifier
def classify(features_train, labels_train): 
    from sklearn import tree # import dt

    clf = tree.DecisionTreeClassifier() # create classifier
    clf = clf.fit(features_train, labels_train) # fit training set 
    

    return clf

### Metrics 
def DTAccuracy(features_test, labels_test): 
    from sklearn.metrics import accuracy_score #accuracy score
    from time import time



    t0 = time() # intial run time
    clf = classify(features_train,labels_train) #create classifier
    print "training time:", round(time() - t0, 3), "s"

    t1 = time() #create time 
    pred = clf.predict(features_test) #create prediction
    print "predictive time:", round(time() - t1, 3), "s"

    accuracy = accuracy_score(labels_test, pred) # accuracy test

    return {"You accuracy is": accuracy}

def features_importance(): 
    clf = classify(features_train, labels_train) # call classifier
    
    import_features = [] # gives me a list of importance features
    for importance in clf.feature_importances_: 
        if importance >= 0.2: #threshhold of important words
            import_features.append(importance)
            import_features.append(numpy.where(clf.feature_importances_ == importance)) #where function
    return (import_features)


def main():

    from sklearn.feature_extraction.text import TfidfVectorizer 
   
    clf = classify(features_train, labels_train)
    accuracy = DTAccuracy(features_test,labels_test)
    print clf 
    print accuracy
    print features_importance()[1]

##### run code ##### 

if __name__ == '__main__':
    main() #show output.     