#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    ### your code goes here
    errors = (net_worths - predictions)**2 # create error 
    cleaned_data = zip(ages,net_worths,errors) # tuple of list
    cleaned_data = sorted(cleaned_data,key=lambda x:x[2][0],reverse=True) # sort third element sorted
    limit = int(len(net_worths)*0.1) # get 90% of data 

    return cleaned_data[limit:]

