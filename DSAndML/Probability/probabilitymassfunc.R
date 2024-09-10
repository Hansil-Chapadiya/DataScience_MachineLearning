probability_mass_func <- function(prob_list, tol = 1e-9) {
    total <- sum(prob_list)
    cat("Sum of probabilities: ", total, "\n")

    # Check if all probabilities are between 0 and 1 and sum to 1
    all_valid <- all(prob_list >= 0 & prob_list <= 1)
    close_to_one <- abs(total - 1) < tol

    return(all_valid && close_to_one)
}
prob_list <- c(0.2, 0.3, 0.5)
print(probability_mass_func(prob_list))


# Using R's fraction Library for Exact Arithmetic
library(MASS)

probability_mass_func_fraction <- function(prob_list) {
    # Convert the list to fractions
    total <- sum(fractions(prob_list))
    cat("Sum of probabilities (as fraction):", total, "\n")

    return(total == 1)
}

print(probability_mass_func_fraction(prob_list))


# Manual Normalization and Validation
probability_mass_func_normalized <- function(prob_list) {
    total <- sum(prob_list)
    normalized <- prob_list / total

    # Check if normalized probabilities sum to 1
    valid_sum <- isTRUE(all.equal(sum(normalized), 1))

    # Check if all probabilities are between 0 and 1
    all_valid <- all(normalized >= 0 & normalized <= 1)

    return(all_valid && valid_sum)
}

print(probability_mass_func_normalized(prob_list)) # Should return TRUE
