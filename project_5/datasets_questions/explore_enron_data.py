#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint 



# enron email + financial datasets (dictionary) load.
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print enron_data[enron_data.keys()[0]] # print the first person of the datasets features.

#print len(enron_data) # prints the length of the people. 

def count_features(): 
    count_features = len([features for features in enron_data[enron_data.keys()[0]].keys()]) 
    return count_features

#print count_features()

def count_poi(): 
    count_poi = 0 
    count_not_poi = 0
    for names in enron_data:
    #if someone is under investigation  
        if enron_data[names]['poi'] == True : 
            count_poi = 1 + count_poi # count poi
        else: 
            count_not_poi = 1 + count_not_poi
    return(count_poi, count_not_poi)

# print count_poi()

def poi_names(filename):
    poi_names = open(filename, "r") #sear for poi names
    poi_names = poi_names.read().split("\n") #split into a list
    return len(poi_names[2:-1]) # count 

#print poi_names("../final_project/poi_names.txt")



# investigate enron workers and solve following questions on udacity. 
def investigate_file(name):
    print name, "File:"
    for features in enron_data[name]: 
        print features, ":", enron_data[name][features]

#print investigate_file("SKILLING JEFFREY K")
#print investigate_file("LAY KENNETH L")
#print investigate_file("FASTOW ANDREW S")

#counts the salary
def salary_count(): 
    count_salary = 0 

    for names in enron_data: 
        if enron_data[names]['salary'] != "NaN": 
            count_salary = 1 + count_salary
    return count_salary

#counts the eamil
def email_count(): 
    count_email = 0 
    for names in enron_data: 
        if enron_data[names]['email_address'] != "NaN": 
            count_email = 1 + count_email
    return count_email


def NaN_salary_count_percentage(): 
    NaN_salary_count = 0
    for names in enron_data: 
        if enron_data[names]["total_payments"] == "NaN": 
            NaN_salary_count = 1 + NaN_salary_count
    total_percentage = NaN_salary_count/float(len(enron_data)) #find the average of percentage
    return total_percentage


#print salary_count() 
#print email_count()
#print NaN_salary_count_percentage()
#pprint.pprint(enron_data)

