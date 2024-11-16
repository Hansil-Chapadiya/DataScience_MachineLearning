import math
from fractions import Fraction  # Import Fraction for precise fractional calculations


def f():
    try:
        # Prompt user to input the number of trials (n)
        n = int(input("Enter number of trials (n): "))
        if n < 0:
            raise ValueError("Number of trials (n) must be a non-negative integer.")

        # Prompt user to input the probability of success (p)
        p = input("Enter probability of success (as a fraction, e.g., 1/2): ")
        p = Fraction(p)  # Convert to Fraction for precision
        if p < 0 or p > 1:
            raise ValueError("Probability must be between 0 and 1.")

        # Calculate the probability of failure (q = 1 - p)
        q = 1 - p

        # Prompt user to input the number of successes (x)
        x = int(input("Enter number of successes (x): "))
        if x < 0 or x > n:
            raise ValueError("Number of successes (x) must be between 0 and n.")

        # Calculate the combination (nCr) and the binomial probability
        combination = math.comb(n, x)
        result = combination * (p**x) * (q ** (n - x))  # Binomial probability

        # Display the result in both fraction and decimal forms
        print(f"Mean = {n * p}")
        print(f"Variance = {n * p * q}")
        print(f"Binomial probability as a fraction: {result}")
        print(f"Binomial probability as a decimal: {float(result)}")

        return result

    except ValueError as e:
        print(f"Error: {e}")
        return None


# Call the function
f()
