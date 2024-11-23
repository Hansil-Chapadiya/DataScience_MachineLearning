def f_dist():
    """
    Compute the F-distribution value based on sample sizes and variances.
    Ensures variance_sample1 >= variance_sample2 for a valid calculation.
    """
    try:
        # Get user inputs
        sample1 = int(input("Enter sample 1 size (n1): "))
        sample2 = int(input("Enter sample 2 size (n2): "))

        variance_sample1 = float(input("Enter variance of sample 1: "))
        variance_sample2 = float(input("Enter variance of sample 2: "))

        # Validate sample sizes
        if sample1 <= 1 or sample2 <= 1:
            raise ValueError("Sample sizes must be greater than 1.")

        # Degrees of freedom
        degree_of_freedom1 = sample1 - 1
        degree_of_freedom2 = sample2 - 1

        # Ensure variance_sample1 >= variance_sample2
        if variance_sample1 < variance_sample2:
            print("Swapping variances to ensure variance_sample1 >= variance_sample2.")
            variance_sample1, variance_sample2 = variance_sample2, variance_sample1
            degree_of_freedom1, degree_of_freedom2 = degree_of_freedom2, degree_of_freedom1

        # Compute F-distribution
        f_distribution = variance_sample1 / variance_sample2
        print(f"\nDegrees of Freedom: df1 = {degree_of_freedom1}, df2 = {degree_of_freedom2}")
        print(f"F-distribution = {f_distribution:.4f}")

    except ValueError as v:
        print(f"ValueError: {v}")
    except Exception as e:
        print(f"Error: {e}")


# Call the function
f_dist()
