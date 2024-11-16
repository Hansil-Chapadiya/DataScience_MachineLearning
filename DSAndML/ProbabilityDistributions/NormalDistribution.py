import math


def f():
    try:
        # Input mean and variance
        mean = float(input("Enter mean: "))
        variance = float(input("Enter variance: "))

        # Validate mean and variance
        if mean < 0 or variance < 0:
            raise ValueError("Mean and variance must be non-negative numbers.")

        # Calculate standard deviation
        standard_deviation = math.sqrt(variance)

        # Input the value of x
        x = float(
            input("Enter value (x): ")
        )  # x does not need to be an integer for a normal distribution
        if x < 0:
            raise ValueError("x must be non-negative.")

        # Calculate the probability density using the normal distribution formula
        probability_density = (
            1
            / (standard_deviation * math.sqrt(2 * math.pi))
            * math.exp(-((x - mean) ** 2) / (2 * variance))
        )

        # Return the calculated PDF
        return probability_density

    except ValueError as e:
        print(f"Error: {e}")
        return None


print(f"Answer = {f()}")