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
