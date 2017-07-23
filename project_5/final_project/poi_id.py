#!/usr/bin/python

import sys
import pickle
import pprint
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import pprint
# import warnings
# warnings.filterwarnings('ignore')
from time import time 

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### import classifiers,

from sklearn import tree                                   ### Decision Tree 


### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

features_list =  ['poi', 'total_stock_value', 'to_poi_ratio', 'restricted_ratio','from_this_person_to_poi']

# You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### dump data_dict into pandas df for EDA. 

### create df from list of values, create a series of employees and index

df = pd.DataFrame.from_records(list(data_dict.values()))
employees = pd.Series(list(data_dict.keys()))
df.set_index(employees, inplace = True)

### Replace "NaN" values for Zero.
df.replace("NaN", 0, inplace= True)

### Task 2: Remove outliers

### Drop Total and TAITP 

df = df.drop(["TOTAL", 'THE TRAVEL AGENCY IN THE PARK'])

### Replace 0 to np.nan 

df.replace(0, np.nan, inplace= True)

### Task 3: Create new feature(s)
### Below are new financial features ['salary_bonus_ratio', 
###                                    'exercised_ratio', 'total_sp_ratio', 
###                                    'restricted_ratio','to_poi_ratio', 'from_poi_ratio'] 

### financial features 

df['salary_bonus_ratio'] = df['salary'] / df['bonus']

df['exercised_ratio']    = df['exercised_stock_options'] / df['total_stock_value']

df['total_sp_ratio']     = df['total_payments'] / df['total_stock_value']

df['restricted_ratio']   = df['restricted_stock'] / df['total_stock_value']

### email features 
df['to_poi_ratio']   = df['from_this_person_to_poi'] / df['from_messages']

df['from_poi_ratio'] = df["from_poi_to_this_person"] / df['to_messages']


### Step 1 - replace np.nan --> "NaN" 
df.replace(np.nan, "NaN", inplace = True)

### Step 2 - Create dictionary 
data_dict = df.to_dict('index')

### Step 3 - Store to my_dataset for easy export below.
my_dataset = data_dict


### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
# from sklearn.naive_bayes import GaussianNB
# clf = GaussianNB()

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html
### Please see Ipython notebook for details on how I tuned.

# Example starting point. Try investigating other evaluation techniques!
### create a test an train cv using 30% test_size
# features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, 
#                                                                                              labels, 
#                                                                                              test_size = 0.3, 
#                                                                                              random_state = 42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.
### fixed value error for min_samples_split. Chose 0.99 not 1.

clf = tree.DecisionTreeClassifier(class_weight='balanced', criterion='gini', max_depth=1,
            max_features=None, max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=42, splitter='best')

dump_classifier_and_data(clf, my_dataset, features_list)