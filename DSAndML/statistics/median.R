#1. manually

data <- c(1, 2, 3, 4, 4, 6, 7, 8, 10)
len <- length(data)

if (len %% 2 == 0) {  # %% is the modulo operator in R
   nthterm <- len / 2
   nplusoneterm <- nthterm + 1
   median_value <- (data[nthterm] + data[nplusoneterm]) / 2
   print(paste("Median =", median_value))
} else {
   median_value <- data[(len + 1) / 2]
   print(paste("Median =", median_value))
}

#2.  Using the median() Function

median_value <- median(data)
print(median_value)

#3. Using the summary() Function
summary(data)

#4. Using Quantile Function
median_value <- quantile(data, 0.5)
print(median_value)

#5. Using floor() and ceiling() with Indexed Data
n <- length(data)
sorted_data <- sort(data)

if (n %% 2 == 0) {
    median_value <- (sorted_data[floor(n/2)] + sorted_data[ceiling(n/2)]) / 2
} else {
    median_value <- sorted_data[ceiling(n/2)]
}
print(median_value)

#6. Using Custom function
calculate_median <- function(data) {
    sorted_data <- sort(data)
    n <- length(sorted_data)
    if (n %% 2 == 0) {
        return((sorted_data[n/2] + sorted_data[n/2 + 1]) / 2)
    } else {
        return(sorted_data[(n + 1) / 2])
    }
}

median_value <- calculate_median(data)
print(median_value)

#7. Using dplyr package
library(dplyr)

data <- data.frame(values = c(1, 2, 3, 4, 4, 6, 7, 8))
median_value <- data %>% summarise(median = median(values)) # %>%> for pipelining
print(median_value)

#8. Using apply package

data <- data.frame(A = c(1, 2, 3), B = c(4, 5, 6), C = c(7, 8, 9))
median_values <- apply(data, 2, median)
print(median_values)

