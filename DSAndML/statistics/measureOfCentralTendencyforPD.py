from cmath import sqrt
from fractions import Fraction as fr

# Function to calculate expected value
def expectedvalue(distribution):
    Mean = 0
    for i in range(len(distribution)):
        Mean += (i + 1) * distribution[i]  # (i + 1) is the outcome, distribution[i] is the probability
    return Mean

# Function to calculate variance
def variance(distribution):
    Mean = expectedvalue(distribution)  # Get the mean (expected value)
    var = 0
    for i in range(len(distribution)):
        X_squared = (i + 1) ** 2  # Square of the outcome (i + 1)
        var += X_squared * distribution[i]  # Multiply by probability P(X)
    return var - Mean ** 2  # Variance = E(X^2) - (E(X))^2

# Define the distribution using fractions
distribution = [fr(1, 36), fr(3, 36), fr(5, 36), fr(7, 36), fr(9, 36), fr(11, 36)]

# Calculate the expected value
expected_val = expectedvalue(distribution)

# Calculate the variance value
var = variance(distribution)

# Print the result in both fraction and decimal form
print(f"Expected Value (Fraction): {expected_val}")
print(f"Expected Value (Decimal): {float(expected_val)}")

# Print the result in both fraction and decimal form
print(f"Variance (Fraction): {var}")
print(f"Variance (Decimal): {float(var)}")

# Print the result in both fraction and decimal form
print(f"Standard Deviation (Fraction): {sqrt(var)}")
print(f"Standard Deviation (Decimal): {sqrt(float(var))}")