#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
import pprint
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL") ### remove the total key 
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

for person in data_dict:
    salary = data_dict[person]["salary"]
    bonus = data_dict[person]["bonus"]
    #below, we need to ignore NaN values which were removed in the data array but not in 
    #the dictionary
    if salary != 'NaN' and bonus != 'NaN' and salary >= 5000000 and bonus > 1000000:
        print person


for key in data_dict: 
    salary = data_dict[key]['salary']
    bonus = data_dict[key]['bonus']
    if (salary != 'NaN' and bonus != "NaN") and salary >= 1000000 and bonus > 5000000: 
        print ((key,salary,bonus))  

## loop through the data and collect the salary and bonus 
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter(salary,bonus)

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()


