import math
import pandas as pd


# x is defined as a list of data points or the mean depending on the defenition it's provided. 
# z is the z-score primarly they z-score for the 95 or 98% (CI)
# x_bar is a sample mean withint the normal distribution
# n is the sample size for the normal distribution, excpet in the midpoint function where it is the length. 



def make_a_list(): 
    """Easier way to copy an excel column and make it into a list."""
    #df = pd.read_clipboard(header=None)
    x = [i for i in df[0]]
    return x 

def mode(x): 
    mode_list = []
    for number in x: 
        mode_list.append((x.count(number),int(number)))  
    return max(mode_list)

def mean(x): 
    sum = 0 
    average = 0 
    for i in x: 
        sum += i 
        average = sum/float(len(x))
    return average

def std(x): 
    sum = 0 
    variance = 0 
    std = 0 
    for i in x: 
        sum += (i-mean(x))**2 
        variance = sum/float(len(x))
        std = math.sqrt(variance)
    return std
 
def midpoint(x): 
    n = len(x)
    if n % 2 == 0: 
        median = (x[n/2] + x[n/2 + 1])/float(2)
        return median
    else: 
        median = x[(n-1)/2]
        return median

def standard_error(x,n): 
    sigma = std(x)
    n = math.sqrt(n)
    return sigma/float(n)


def confidence_interval(x,n,x_bar,z): 
    SE = standard_error(x,n)
    return(x_bar-(z*SE),x_bar+(z*SE))


def z_score(x_bar,x,sigma): 
    return(x_bar-x)/float(sigma)
