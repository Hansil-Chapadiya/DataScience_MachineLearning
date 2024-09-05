data_set <- c(5, 2, 3, 4, 1, 6, 7, 8, 10)

# i. Range
data_range <- max(data_set) - min(data_set)
print(paste("Range =", data_range))

# ii. Variance
variance <- var(data_set)
print(paste("Variance =", variance))

# iii. Standard Deviation
standard_deviation <- sd(data_set)
print(paste("Standard Deviation =", standard_deviation))

# iv. Mean Absolute Deviation
mad_value <- mad(data_set, center = mean(data_set))
print(paste("Mean Absolute Deviation =", mad_value))

# v. Quartile Deviation
quartiles <- quantile(data_set)
q1 <- quartiles[2]  # First Quartile
q3 <- quartiles[4]  # Third Quartile
quartile_deviation <- (q3 - q1) / 2
print(paste("First Quartile (Q1) =", q1))
print(paste("Third Quartile (Q3) =", q3))
print(paste("Quartile Deviation =", quartile_deviation))

# Interquartile Range (IQR)
iqr_value <- IQR(data_set)
print(paste("Interquartile Range (IQR) =", iqr_value))

# manually
data_set <- sort(data_set)
data_set_length <- length(data_set)

# i. Range
data_range <- data_set[data_set_length] - data_set[1]
print(paste("Range =", data_range))

# ii. Mean
mean_value <- sum(data_set) / data_set_length
print(paste("Mean =", mean_value))

# iii. Variance (Manual Calculation)
variance <- 0
for (i in 1:data_set_length) {
  variance <- variance + (data_set[i] - mean_value)^2
}
variance <- variance / data_set_length
print(paste("Variance =", variance))

# iv. Standard Deviation (Manual Calculation)
standard_deviation <- sqrt(variance)
print(paste("Standard Deviation =", standard_deviation))

# v. Mean Absolute Deviation (MAD)
mean_deviation <- 0
for (i in 1:data_set_length) {
  mean_deviation <- mean_deviation + abs(data_set[i] - mean_value)
}
mean_deviation <- mean_deviation / data_set_length
print(paste("Mean Absolute Deviation =", mean_deviation))

# vi. Quartile Deviation
# First Quartile (Q1)
q1_index <- ceiling(data_set_length / 4)
q1 <- data_set[q1_index]

# Third Quartile (Q3)
q3_index <- ceiling(3 * data_set_length / 4)
q3 <- data_set[q3_index]

# Quartile Deviation
quartile_deviation <- (q3 - q1) / 2
print(paste("First Quartile (Q1) =", q1))
print(paste("Third Quartile (Q3) =", q3))
print(paste("Quartile Deviation =", quartile_deviation))
