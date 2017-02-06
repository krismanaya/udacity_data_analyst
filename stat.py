import math

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
