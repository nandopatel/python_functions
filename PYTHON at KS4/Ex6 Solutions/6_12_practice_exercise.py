#12)Define a function called standard_deviation() that returns the standard deviation
#of a list. Feel free to use the functions defined in questions 10 and 11 above.
#a) Find the mean
#b) List of deviation
#c) Squares of the deviation
#d) Sum of the squares of deviation
#e)Divided by one less than the number of items
#f)Square root of this number
# use sqrt(), which is defined in the math module

import math

z = [1, 4, 5, 7, 9, 20]

def sum_list(l):
    total =0
    for element in l:
        total = total + element
    return total

def mean_list(l):
    return sum_list(l)/len(l)

mean=mean_list(z)
#List of deviations
def list_of_deviation(l):
    for index in range(len(l)):
        l[index] = l[index]- mean
        
#Now square of deviations
def square_list(l):
    for index in range(len(l)):
        l[index] = l[index]*l[index]

def standard_dev(l):
    #mean=mean_list(l)
    list_of_deviation(l)
    square_list(l)
    variance = sum_list(l)
    return math.sqrt(variance/(len(l)-1))

std_dev = standard_dev(z)
print(std_dev)
