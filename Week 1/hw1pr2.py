# Filename: hw1pr2.py
# Name: Stephanie Ramirez
# Problem description: First few functions!

from math import*

def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
    """
    return 2*x

def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x

def sq(x):
    """Results: sq returns square of its argument
       Argument x: a number (int or float)
    """
    return x**2

def interp(low, hi, fraction):
    """Results: floating-point value that is fraction of the way between low and hi.
       Arugment x: a three numbers (int or float)
    """
    diff = hi - low
    answer = (fraction * diff) + low 
    return answer

def checkends(s):
    """Results: returns True if the first character is the same as the last character 
       Argument x: a string
    """
    return s[0] == s[-1]

def flipside(s):
    """Result: accepts a string s and returns a string whose first half is s's second half and whose second half is s's first half.
       Argument x: a string
    """
    mid = len(s) // 2 
    return s[mid:] + s[:mid]

def convertFromSeconds(s):
    """Result:  takes in a nonnegative integer number of seconds s and returns a list of days, hours, minutes, and seconds
       Arguemnt x: a number (int)
    """
    days = s // (24 * 60 * 60)  # Number of days
    s = s % (24 * 60 * 60)      # The leftover
    hours = s // (60 * 60)      # Number of hours
    s = s % (60 * 60)           # The leftover
    minutes = s // 60           # Number of minutes
    s = s % 60                  # The leftover
    seconds = s                 # Number of seconds
    return [days, hours, minutes, seconds]