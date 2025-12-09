# 1. Manually using dictionary to count frequencies
data_set = [1, 2, 3, 4, 4, 6, 7, 8, 4, 2, 2]

# Count frequency of each element
frequency = {}
for item in data_set:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

# Find the maximum frequency
max_frequency = max(frequency.values())

# Find all items with maximum frequency
modes = [key for key, value in frequency.items() if value == max_frequency]

print('Mode(s) manually = ', modes)

# 2. Using collections.Counter
from collections import Counter

# Count frequencies
frequency_counter = Counter(data_set)

# Find maximum frequency
max_frequency = max(frequency_counter.values())

# Find modes
modes = [key for key, value in frequency_counter.items() if value == max_frequency]

print('Mode(s) using Counter = ', modes)

# 3. Using statistics module
import statistics

print('Mode using statistics = ', statistics.mode(data_set))

# For multimodal data, use statistics.multimode() (Python 3.8+)
try:
    print('Multimode using statistics = ', statistics.multimode(data_set))
except AttributeError:
    print('multimode() not available in this Python version')

# 4. Using scipy.stats (if available)
try:
    from scipy import stats

    # scipy.stats.mode returns mode and count
    mode_result = stats.mode(data_set, keepdims=True)
    print('Mode using scipy = ', mode_result.mode[0])
    print('Mode count using scipy = ', mode_result.count[0])
except ImportError:
    print('scipy not available')

# 5. Function to find mode manually with edge cases
def find_mode(data):
    """
    Find mode(s) in a dataset
    Returns a list of modes (can be multiple in case of tie)
    """
    if not data:
        return []

    # Count frequencies
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1

    # Find maximum frequency
    max_freq = max(frequency.values())

    # Return all items with maximum frequency
    modes = [key for key, freq in frequency.items() if freq == max_freq]

    return modes

# Test with different datasets
print("\n--- Testing custom function ---")

# Single mode
data1 = [1, 2, 3, 4, 4, 4, 5]
print(f"Data: {data1}")
print(f"Mode(s): {find_mode(data1)}")

# Multiple modes (bimodal)
data2 = [1, 1, 2, 2, 3]
print(f"Data: {data2}")
print(f"Mode(s): {find_mode(data2)}")

# No mode (all elements appear once)
data3 = [1, 2, 3, 4, 5]
print(f"Data: {data3}")
print(f"Mode(s): {find_mode(data3)}")

# Using fractions
from fractions import Fraction as fr

data4 = [fr(1, 2), fr(1, 2), fr(3, 4), fr(2, 3)]
print(f"Data with fractions: {data4}")
print(f"Mode(s): {find_mode(data4)}")

# String data
data5 = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
print(f"String data: {data5}")
print(f"Mode(s): {find_mode(data5)}")