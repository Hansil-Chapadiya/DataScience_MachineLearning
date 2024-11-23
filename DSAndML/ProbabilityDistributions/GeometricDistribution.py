def geometric_pmf():
    """
    Calculate the probability mass function (PMF) of a geometric distribution.

    Formula: P(X = x) = q^(x-1) * p
    where:
        - p is the probability of success (0 < p <= 1)
        - q = 1 - p is the probability of failure
        - x is the number of trials (x >= 1 and integer)
    """
    try:
        # Input the probability of success
        p = float(input("Enter the probability of success (0 < p <= 1): "))
        if p <= 0 or p > 1:
            raise ValueError("The probability p must be in the range (0, 1].")

        mean = 1.0 / p
        standard_deviation = (1.0 - p) / p**2

        # print Mean
        print(f"Mean = {mean}")

        # print S.D
        print(f"Standard_deviation = {standard_deviation}")

        # Calculate the probability of failure
        q = 1 - p

        # Input the value of x
        x = int(input("Enter the number of trials (x >= 1): "))
        if x < 1:
            raise ValueError("x must be an integer >= 1.")

        # Calculate the PMF
        probability_mass = q ** (x - 1) * p
        return probability_mass

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


# Example usage
result = geometric_pmf()
if result is not None:
    print(f"Result: {result}")
