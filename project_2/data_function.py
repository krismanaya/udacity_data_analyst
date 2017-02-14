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