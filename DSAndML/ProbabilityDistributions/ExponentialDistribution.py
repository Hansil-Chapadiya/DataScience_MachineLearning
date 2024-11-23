import math
from scipy.integrate import quad


def pdf(x, λ):
    """
    Exponential probability density function.

    Formula: f(x) = λ * exp(-λ * x)
    where:
        - λ > 0 (rate parameter)
        - x >= 0
    """
    if x < 0:
        return 0  # The PDF is 0 for x < 0
    return λ * math.exp(-λ * x)


def exponential_pdf():
    """
    Calculate the probability for an exponential distribution over a specified range.

    Formula: P(a <= X <= b) = ∫[a, b] (λ * exp(-λ * x)) dx
    where:
        - mean = 1 / λ (mean must be > 0)
        - variance = 1 / λ^2
    """
    try:
        # Input the mean
        mean = float(input("Enter the mean (mean > 0): "))
        if mean <= 0:
            raise ValueError("Mean must be greater than 0.")

        # Calculate the rate parameter λ
        λ = 1.0 / mean
        var = 1.0 / (λ**2)

        # Display calculated parameters
        print(f"\nExponential Distribution Parameters:")
        print(f"  Mean (μ): {mean}")
        print(f"  Rate Parameter (λ): {λ:.4f}")
        print(f"  Variance (σ²): {var:.4f}\n")

        # Input the integration range
        a = float(input("Enter the start of the range (a >= 0): "))
        b = float(input("Enter the end of the range (b >= a): "))
        if a < 0 or b < a:
            raise ValueError("Invalid range. Ensure a >= 0 and b >= a.")

        # Integrate the PDF over the range [a, b]
        prob, err = quad(pdf, a, b, args=(λ,))

        # Display results
        print(f"\nProbability for range [{a}, {b}]:")
        print(f"  P({a} <= X <= {b}): {prob:.5f}")
        print(f"  Error Estimate: {err:.5e}")

    except ValueError as ve:
        print(f"\nInput Error: {ve}")
    except Exception as e:
        print(f"\nUnexpected Error: {e}")


# Example usage
exponential_pdf()
