from scipy.integrate import quad


def pdf(x, a, b):
    """
    Uniform probability density function.

    Formula: f(x) = 1 / (b - a) if a <= x <= b, else 0
    """
    if a <= x <= b:
        return 1.0 / (b - a)
    return 0.0


def uniform_pdf():
    """
    Calculate the probability for a Uniform distribution over a specified range.

    Formula: P(a <= X <= b) = ∫[a, b] (1.0/(b - a)) dx
    where:
        - mean = (a + b) / 2
        - variance = (b - a) ** 2 / 12
    """
    try:
        # Input range [a, b]
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b where (b > a): "))
        if b <= a:
            raise ValueError("b must be greater than a.")

        # Calculate mean and variance
        mean = (a + b) / 2.0
        variance = (b - a) ** 2 / 12.0

        # Display calculated parameters
        print(f"\nUniform Distribution Parameters:")
        print(f"  Mean (μ): {mean}")
        print(f"  Variance (σ²): {variance:.4f}\n")

        # Input the integration range
        range_from = float(input("Enter the start of the range (rf >= a): "))
        range_to = float(input("Enter the end of the range (rt <= b): "))
        if range_from < a or range_to > b or range_from > range_to:
            raise ValueError(
                "Invalid integration range. Ensure a <= rf <= rt <= b."
            )

        # Integrate the PDF over the range [range_from, range_to]
        prob, err = quad(pdf, range_from, range_to, args=(a, b))

        # Display results
        print(f"\nProbability for range [{range_from}, {range_to}]:")
        print(f"  P({range_from} <= X <= {range_to}): {prob:.5f}")
        print(f"  Error Estimate: {err:.5e}")

    except ValueError as ve:
        print(f"\nInput Error: {ve}")
    except Exception as e:
        print(f"\nUnexpected Error: {e}")


# Example usage
uniform_pdf()
