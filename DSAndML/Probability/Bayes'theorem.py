def bayes_theorem_multiple(priors, likelihoods):
    """
    priors: List of prior probabilities for each event A_i
    likelihoods: List of P(B|A_i) for each event A_i
    """
    # Calculate P(B) using the law of total probability
    p_b = sum([likelihoods[i] * priors[i] for i in range(len(priors))])

    # Calculate P(A_i|B) for each event A_i
    posteriors = [(likelihoods[i] * priors[i]) / p_b for i in range(len(priors))]

    return posteriors


# Example:
priors = [0.2, 0.5, 0.3]  # Prior probabilities for A1, A2, A3
likelihoods = [0.8, 0.6, 0.4]  # Likelihoods P(B|A1), P(B|A2), P(B|A3)

posteriors = bayes_theorem_multiple(priors, likelihoods)

for i, posterior in enumerate(posteriors):
    print(f"The posterior probability P(A{i+1}|B) is {posterior:.4f}")

'''
enumerate is a built-in Python function that allows us to loop over a list and get both the index and the value at each step of the iteration.
'''