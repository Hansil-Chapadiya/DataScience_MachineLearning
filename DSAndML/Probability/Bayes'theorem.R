bayes_theorem_multiple <- function(priors, likelihoods) {
    # Calculate P(B) using the law of total probability
    p_b <- sum(priors * likelihoods)

    # Calculate P(A_i|B) for each event A_i
    posteriors <- (priors * likelihoods) / p_b

    return(posteriors)
}

# Example data:
priors <- c(0.2, 0.5, 0.3) # Prior probabilities for A1, A2, A3
likelihoods <- c(0.8, 0.6, 0.4) # Likelihoods P(B|A1), P(B|A2), P(B|A3)

# Calculate posteriors
posteriors <- bayes_theorem_multiple(priors, likelihoods)

# Print results
len <- length((posteriors))
for (i in 1:len) {
    cat(sprintf("The posterior probability P(A%d|B) is %.4f\n", i, posteriors[i]))
}


# Chatgpt code
# Define probabilities
P_D <- 0.01           # Prior probability of having the disease
P_T_given_D <- 0.90   # Probability of testing positive given having the disease
P_T_given_Dc <- 0.05  # Probability of testing positive given not having the disease
P_Dc <- 1 - P_D       # Probability of not having the disease

# Calculate the marginal probability of testing positive
P_T <- (P_T_given_D * P_D) + (P_T_given_Dc * P_Dc)

# Calculate the posterior probability of having the disease given a positive test result
P_D_given_T <- (P_T_given_D * P_D) / P_T

# Print the result
print(P_D_given_T)
