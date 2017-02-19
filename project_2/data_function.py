import unicodecsv 
from datetime import datetime as dt

def read_csv(filename): 
    """this reads the data in a csv files and stores it in a list of dictionaries."""
    with open(filename,'rb') as f: 
        reader = unicodecsv.DictReader(f)
        return list(reader)

def parse_date(date): 
    """takes a string and returns a Python datetime object"""
    if date = '': 
        return None 
    else: 
        return dt.strptime(date, '%Y-%m-%d')

def parse_may_int(i): 
    """Takes a string which is either an empy string or represents an integer, 
       and returns int or None."""
    if i = '': 
        return None 
    else: 
        return int(i)

def get_unique_students(data): 
    """ takes the acct of unique students in the dataset, writes a set
        and returns the set of students."""
    unique_students = set()
    for data_point in data: 
        unique_students.add(data['account_key'])
        return unique_students

def remove_udacity_accounts(data):
    """Give some data with account_key field, removes any records corresponding to Udacity test accounts."""
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data