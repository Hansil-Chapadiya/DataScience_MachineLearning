import numpy as np

data_set = [5, 2, 3, 4, 1, 6, 7, 8, 10]
data_set_length = len(data_set)
data_set.sort()

# i. Range
data_range = data_set[-1] - data_set[0]
print("Range = ", data_range)

# ii. Variance
# Calculate the mean
mean = sum(data_set) / data_set_length
print("Mean = ", mean)

variance = 0
for i in range(data_set_length):
    variance += (data_set[i] - mean) ** 2  # Square the difference from the mean

variance = variance / data_set_length  # Average of the squared differences (variance)
print("Variance = ", variance)

# iii. Standard Deviation
# Calculate the standard deviation (square root of variance)
standard_deviation = variance**0.5
print("Standard Deviation = ", standard_deviation)

# iv. Mean Deviation
# Calculate the mean deviation (summation of |x - mean|) / n
mean_deviation = sum(abs(data_set[i] - mean) for i in range(data_set_length))
print("Mean Deviation = ", mean_deviation / data_set_length)

# v. Quartile Deviation (Semi-Interquartile Range)

# First Quartile (Q1)
Q1 = (
    data_set[data_set_length // 4]
    if data_set_length % 2 == 0
    else (data_set[data_set_length // 4] + data_set[(data_set_length // 4) + 1]) / 2
)

# Third Quartile (Q3)
Q3 = (
    data_set[3 * data_set_length // 4]
    if data_set_length % 2 == 0
    else (data_set[3 * data_set_length // 4] + data_set[(3 * data_set_length // 4) + 1])
    / 2
)

# Quartile Deviation
quartile_deviation = (Q3 - Q1) / 2
print("First Quartile (Q1) = ", Q1)
print("Third Quartile (Q3) = ", Q3)
print("Quartile Deviation = ", quartile_deviation)

# v. Quartile Deviation (Manual Calculation)
Q1 = np.percentile(data_set, 25)  # First Quartile (25th percentile)
Q3 = np.percentile(data_set, 75)  # Third Quartile (75th percentile)
quartile_deviation = (Q3 - Q1) / 2
print("First Quartile (Q1) = ", Q1)
print("Third Quartile (Q3) = ", Q3)
print("Quartile Deviation = ", quartile_deviation)
