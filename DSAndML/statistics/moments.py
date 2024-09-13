# Frequency distribution
f = [5, 10, 15, 20, 25, 20, 15, 10, 5]
# f = [1, 8, 28, 56, 70, 56, 28, 8, 1]

# Initialize variables
sum_fx = 0  # To store the sum of f * x
N = sum(f)  # Total frequency N

# Step 1: Calculate the sum of f * x (for mean calculation)
for x in range(len(f)):
    sum_fx += f[x] * x  # f[x] * x for each value

# Step 2: Calculate the mean
mean_ = sum_fx / N  # Mean is sum(f * x) / N

# Initialize variables for higher moments calculations
sum_f_into_x_sub_mean = 0
sum_f_into_x_sub_mean_raise_2 = 0
sum_f_into_x_sub_mean_raise_3 = 0
sum_f_into_x_sub_mean_raise_4 = 0

# Step 3: Calculate summation of f(x - mean), (x - mean)^2, (x - mean)^3, (x - mean)^4
for x in range(len(f)):
    deviation = x - mean_  # Calculate (x - mean) for each value of x
    sum_f_into_x_sub_mean += f[x] * deviation  # Summation of f(x - mean)
    sum_f_into_x_sub_mean_raise_2 += f[x] * (deviation**2)  # Summation of f(x - mean)^2
    sum_f_into_x_sub_mean_raise_3 += f[x] * (deviation**3)  # Summation of f(x - mean)^3
    sum_f_into_x_sub_mean_raise_4 += f[x] * (deviation**4)  # Summation of f(x - mean)^4

# Print the intermediate results
print("N = ", N)
print("Summation of fx = ", sum_fx)
print("Summation of f(x - mean) = ", sum_f_into_x_sub_mean)
print("Summation of f(x - mean)^2 = ", sum_f_into_x_sub_mean_raise_2)
print("Summation of f(x - mean)^3 = ", sum_f_into_x_sub_mean_raise_3)
print("Summation of f(x - mean)^4 = ", sum_f_into_x_sub_mean_raise_4)

# Step 4: Calculate moments about the actual mean
m1 = sum_f_into_x_sub_mean / N  # First moment (about the mean, m1 should be close to 0)
m2 = sum_f_into_x_sub_mean_raise_2 / N  # Second moment (variance)
m3 = sum_f_into_x_sub_mean_raise_3 / N  # Third moment (skewness related)
m4 = sum_f_into_x_sub_mean_raise_4 / N  # Fourth moment (kurtosis related)

# Print moments
print("Moments about Actual Mean:")
print("m1 = ", m1)  # Should be close to 0, as it's the first moment about the mean
print("m2 = ", m2)  # Second moment (variance)
print("m3 = ", m3)  # Third moment (for skewness)
print("m4 = ", m4)  # Fourth moment (for kurtosis)

# Step 5: Calculate skewness and kurtosis
skewness = m3 / (m2 ** (3 / 2))  # Skewness is m3 divided by m2 raised to 3/2
kurtosis = m4 / (m2**2)  # Kurtosis is m4 divided by m2 squared

# Print skewness and kurtosis
print("Skewness = ", skewness)
print("Kurtosis = ", kurtosis)

