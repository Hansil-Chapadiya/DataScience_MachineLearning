# Function to calculate expected value
expectedValue <- function(distribution) {
    Mean <- 0
    # Loop through each element of the distribution
    for (i in seq_along(distribution)) {
        Mean <- Mean + ((i) * distribution[i])  # i is the index (which starts at 1 in R)
    }
    return(Mean)
}

expectedValue_1 <- function(distribution) {
    Mean <- 0
    for (i in 1:length(distribution)) {
       Mean <- Mean + (i * distribution[i])
    }
    return(Mean)
}

# Define the distribution using numeric fractions
distribution <- c(1/36, 3/36, 5/36, 7/36, 9/36, 11/36)

# Calculate and print the expected value
expected_val <- expectedValue(distribution)
print(paste("Expected Value:", round(expected_val,2)))

