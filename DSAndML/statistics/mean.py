#1. manually
data_set = [1,2,3,4,4,6,7,8]

summation = sum(data_set);
list_len = sum(1 for i in data_set)

print('Mean = ' , (summation/list_len))

#2.len function

summation = sum(data_set)
list_len = len(data_set)

print('Mean = ', (summation / list_len))

#3. import statistics

import statistics

print('Mean = ',statistics.mean(data_set))


#4. function from the statistics module

# Importing the statistics module
from statistics import mean

# Importing fractions module as fr
# Enables to calculate mean of a
# set in Fraction
from fractions import Fraction as fr


# tuple of positive integer numbers
data1 = (17, 13, 18, 15, 27, 92, 12)

# tuple of a negative set of integers
data2 = (-12, -25, -14, -17, -12, -25)

# tuple of mixed range of numbers
data3 = (-1, -13, -6, 4, 5, 19, 9)

# tuple of a set of fractional numbers
data4 = (fr(1, 2), fr(44, 12), fr(10, 3), fr(2, 3))

# dictionary of a set of values
# Only the keys are taken in
# consideration by mean()
data5 = {1:"one", 2:"two", 3:"three"}


# Printing the mean of above datasets
print("Mean of data set 1 is % s" % (mean(data1)))
print("Mean of data set 2 is % s" % (mean(data2)))
print("Mean of data set 3 is % s" % (mean(data3)))
print("Mean of data set 4 is % s" % (mean(data4)))
print("Mean of data set 5 is % s" % (mean(data5)))


