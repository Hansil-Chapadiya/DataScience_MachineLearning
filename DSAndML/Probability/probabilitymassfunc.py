def probabilitymassfunc(prob_list, tol=1e-9):
    total = sum(prob_list)
    print(f"Sum of probabilities: {total}")

    # Check if the sum of probabilities is close enough to 1, within a tolerance
    return abs(total - 1) < tol


prob_list = [0.5, 0.5]
print(probabilitymassfunc(prob_list))

"""
Tolerance Check (tol=1e-9): This allows for small floating-point differences, so instead of checking if sum(prob_list) == 1, it checks if the sum is close enough to 1 (within the tolerance of 1e-9).
abs(total - 1) < tol: This checks whether the difference between the sum and 1 is smaller than the tolerance, allowing for floating-point inaccuracies.
"""

# using numpy

import numpy as np


def probability_mass_func_numpy(prob_list):
    total = np.sum(prob_list)
    print(f"Sum of probabilities: {total}")

    # Use numpy's built-in tolerance for floating-point comparisons
    return np.isclose(total, 1)


print(probability_mass_func_numpy(prob_list))


# Check if Probabilities Are Between 0 and 1
def probability_mass_func(prob_list):
    # Ensure all probabilities are between 0 and 1
    if all(0 <= p <= 1 for p in prob_list):
        total = sum(prob_list)
        print(f"Sum of probabilities: {total}")

        # Check if the sum is 1
        return abs(total - 1) < 1e-9  # Adjusted tolerance
    else:
        return False


# Example usage:
prob_list = [0.4, 0.6]
print(probability_mass_func(prob_list))

# Using fractions.Fraction for Exact Arithmetic

from fractions import Fraction


def probability_mass_func_fraction(prob_list):
    prob_list_fraction = [Fraction(p).limit_denominator() for p in prob_list]
    total = sum(prob_list_fraction)

    print(f"Sum of probabilities (as fraction): {total}")

    return total == 1


print(probability_mass_func_fraction(prob_list))

# Normalize manually

def probability_mass_func_normalized(prob_list):
    # Normalize the probabilities by dividing by the sum
    total = sum(prob_list)
    normalized = [p / total for p in prob_list]

    # Check if the sum of normalized probabilities equals 1
    return sum(normalized) == 1

print(probability_mass_func_normalized(prob_list))

