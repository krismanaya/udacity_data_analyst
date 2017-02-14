
import math
import pandas as pd

# x is defined as a list of data points or the mean depending on the defenition it's provided. 
# z is the z-score primarly they z-score for the 95 or 98% (CI)
# x_bar is a sample mean withint the normal distribution
# n is the sample size for the normal distribution, excpet in the midpoint function where it is the length. 

def make_a_list(): 
    #Make x
    """Easier way to copy an excel column and make it into a list."""
    df = pd.read_clipboard(header=None)
    x = [i for i in df[0]]
    return x 

def mode(x):
    #x is a list
    """the left hand side is the count of numbers and the right is the greatest number in the histogram."""
    mode_list = []
    for number in x: 
        mode_list.append((x.count(number),number))  
    return max(mode_list)

def mean(x):
    #x is a list  
    sum = 0 
    average = 0 
    for i in x: 
        sum += i 
        average = sum/float(len(x))
    return average

def variance(x): 
    sum = 0
    for i in x: 
        sum += (i-mean(x))**2
    return sum

def pooled_variance(x_1,x_2): 
    ss_1 = variance(x_1)
    ss_2 = variance(x_2)
    df_1 = len(x_1)-1
    df_2 = len(x_2)-1
    return (ss_1 + ss_2)/(df_1 + df_2) 


def std(x):
    #x is a list  
    sum = 0 
    variance = 0 
    std = 0 
    for i in x: 
        sum += (i-mean(x))**2 
        variance = sum/len(x)
        std = math.sqrt(variance)
    return std

def std_indy(x_1,x_2): 
    s_1 = std(x_1)
    s_2 = std(x_2) 
    return math.sqrt(s_1**2 + s_2**2)
 
def midpoint(x): 
    #x is a list
    n = len(x)
    if n % 2 == 0: 
        median = (x[n/2] + x[n/2 + 1])/float(2)
        return median
    else: 
        median = x[(n-1)/2]
        return median

def standard_error(x,n): 
    #x is a list and n is a sample
    sigma = std(x)
    n = math.sqrt(n)
    return sigma/float(n)

def standard_sample_error(x,n): 
    sigma = bessels_correction(x)
    n = math.sqrt(n)
    return sigma/float(n)

def independent_standard_error(x_1,x_2,n_1,n_2): 
    s_1 = bessels_correction(x_1)
    s_2 = bessels_correction(x_2)
    return math.sqrt(s_1**2/float(n_1) + s_2**2/float(n_2))

def corrected_standard_error(x_1,x_2,n_1,n_2): 
    """Corrected standard error using the pooled variance"""
    s_p = pooled_variance(x_1,x_2)
    df_1 = n_1 - 1
    df_2 = n_2 - 1 
    SE = math.sqrt(s_p/n_1 + s_p/n_2)
    return SE 

def margin_error(z,s,n): 
    """always calculate the the margin of error on a two-tailed test."""
    return z*(s/float(math.sqrt(n)))

def confidence_interval(x_bar,z,s,n):
    #x_bar is a sample mean, z or t is the margin of error  score, s is the standard deviation 
    # and n is the sample size
    SE = s/float(math.sqrt(n))
    return(x_bar-(z*SE),x_bar+(z*SE))

def confidence_interval_indy(x_bar_1,x_bar_2,z,s_1,s_2,n_1,n_2): 
    SE = math.sqrt(s_1**2/float(n_1) + s_2**2/float(n_2))
    diff = (x_bar_1 - x_bar_2)
    return(diff-(z*SE), diff + (z*SE))

def z_score(x_bar,x,sigma): 
    #x_bar is a sample mean, x is a mean and sigma is the standard deviation 
    return(x_bar-x)/float(sigma)

def t_stat(x_bar,x,s,n):
    #x_bar is a sample mean, x is a mean, s is the standard deviation and n is the sample size
    SE = s/float(math.sqrt(n)) 
    return(x_bar-x)/SE

def t_stat_indy(x_bar_1,x_bar_2,x_1,x_2,s_1,s_2,n_1,n_2): 
    SE = math.sqrt(s_1**2/float(n_1) + s_2**2/float(n_2))
    return(((x_bar_1-x_bar_2)-(x_1-x_2))/SE)

def t_stat_indy_pool(x_bar_1,x_bar_2,x_1,x_2,SE): 
    """pooled variance for the t_test. Normally we use thsi one."""
    return(((x_bar_1-x_bar_2)-(x_1-x_2))/SE)
   
def cohens_d(x_bar,x,s): 
    #s := as the standard deviation of the sample mean x_bar. 
    d = (x_bar-x)/float(s)
    return d

def difference(x,y): 
    """this function takes two lists x and y respectively and outputs the difference as a list."""
    diff = []
    for i,j in zip(x,y): 
        diff.append(i-j)
    return diff 

def bessels_correction(x):
    #x is a list
    sum = 0 
    variance = 0 
    S = 0 
    for i in x: 
        sum += (i-mean(x))**2
        variance = sum/float(len(x)-1)
        S = math.sqrt(variance)
    return S

def degrees_of_freedom(x):
    #x is a list  
    """the left hand side is the sample and the right is the DOF."""
    return (len(x),len(x)-1)

def degrees_of_freedom_indy(x_1,x_2): 
    n_1 = len(x_1) 
    n_2 = len(x_2)
    df = n_1 + n_2 - 2
    return (((n_1,n_2), df))

def r_squared(x_bar,x,s,n): 
    """this is for the t-test r squared were we look at the degrees of freedom"""
    t = t_stat(x_bar,x,s,n) #this is the t-statistic 
    df = (n-1) #this is the degrees of freed of the sample size. 
    r_squared = t**2/(t**2 + df) #this is r^2  
    return r_squared 

