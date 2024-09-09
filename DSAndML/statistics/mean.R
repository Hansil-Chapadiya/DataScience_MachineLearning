#1. using mean function
data <- c(1, 2, 3, 4, 4, 6, 7, 8)
mean_value <- mean(data)
print(mean_value)

#2. Using the sum() and length() functions
data <- c(1, 2, 3, 4, 4, 6, 7, 8)
mean_value <- sum(data) / length(data)
print(mean_value)

#3. Using the colMeans() function for a matrix
data <- matrix(c(1, 2, 3, 4, 4, 6, 7, 8), ncol = 2)
mean_values <- colMeans(data)
print(mean_values)

#4. Using the apply() function
data <- matrix(c(1, 2, 3, 4, 4, 6, 7, 8), ncol = 2)
mean_values <- apply(data, 2, mean) # 2 indicates columns; use 1 for rows
print(mean_values)

#5. Using the aggregate() function
df <- data.frame(value = c(1, 2, 3, 4, 4, 6, 7, 8),
                 group = c("A", "A", "B", "B", "A", "A", "B", "B"))
mean_values <- aggregate(value ~ group, data = df, FUN = mean)
print(mean_values)

#6. Using the dplyr package
library(dplyr)
df <- data.frame(value = c(1, 2, 3, 4, 4, 6, 7, 8),
                 group = c("A", "A", "B", "B", "A", "A", "B", "B"))
mean_values <- df %>% group_by(group) %>% summarize(mean_value = mean(value))
print(mean_values)

#7. Using the tapply() function
df <- data.frame(value = c(1, 2, 3, 4, 4, 6, 7, 8),
                 group = c("A", "A", "B", "B", "A", "A", "B", "B"))
mean_values <- tapply(df$value, df$group, mean)
print(mean_values)

#8. Using the weighted.mean() function
data <- c(1, 2, 3, 4, 4, 6, 7, 8)
weights <- c(1, 1, 1, 1, 1, 1, 1, 2)
weighted_mean_value <- weighted.mean(data, weights)
print(weighted_mean_value)

