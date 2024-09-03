# 1. manually
data_set = [1, 2, 3, 4, 4, 6, 7, 8, 10]

list_len = sum(1 for i in data_set)

if (list_len % 2) == 0:
    nthterm = (int)(list_len / 2) - 1
    nplusoneterm = (int)(list_len / 2)
    print(
        "Median = ", (data_set[nthterm] + data_set[nplusoneterm]) / 2
    )  # (n/2th term + n/2 + 1th term)/2
else:
    print("Median = ", data_set[(int)((list_len) / 2)])  # (n+1/2)th term

# 2. Using integer division

# Find the length of the data set
list_len = len(data_set)

# Calculate the median
if list_len % 2 == 0:
    median = (data_set[list_len // 2 - 1] + data_set[list_len // 2]) / 2
else:
    median = data_set[list_len // 2]

print("Median =", median)

# 3. from statistics module

import statistics

print("Median = ", statistics.median(data_set))

# 4. Using heapq

import heapq

# Get the middle index of the list
mid = len(data_set) // 2

# Check if the length of the list is even or odd
if len(data_set) % 2 == 0:
    # If the length is even, find the median by getting the middle two numbers
    # using nlargest() and nsmallest() from the heapq module
    res = (heapq.nlargest(mid, data_set)[-1] + heapq.nsmallest(mid, data_set)[-1]) / 2
else:
    # If the length is odd, find the median by getting the middle number
    # using nlargest() from the heapq module
    res = heapq.nlargest(mid + 1, data_set)[-1]

# Print the median of the list
print("Median = " + str(res))
