import pandas as pd
from itertools import product

def sampling_dist(population, sample_size):
    N = len(population)  # Size of population
    n = sample_size  # Sample size
    k = N ** n  # Total number of samples (with replacement)

    # Create all possible samples of size `n` with replacement
    samples = list(product(population, repeat=n))

    # Collect rows in a list
    rows = []

    # Iterate through all samples to calculate the required values
    for sample in samples:
        total = sum(sample)  # Sum of the sample
        sample_mean = total / n  # Mean of the sample

        # Append the results as a dictionary to the list
        rows.append({"Sample": sample, "Total": total, "SampleMean": sample_mean})

    # Convert the list of dictionaries into a DataFrame
    sample_mean_calculate_table = pd.DataFrame(rows)

    # Calculate mean and standard deviation of sample means
    sample_mean_values = sample_mean_calculate_table["SampleMean"]
    mean_of_sample_means = sample_mean_values.mean()
    std_dev_of_sample_means = sample_mean_values.std()

    return sample_mean_calculate_table, mean_of_sample_means, std_dev_of_sample_means


# Example Usage
population = [3, 7, 11, 15]
sample_size = 2
result, mean_of_sample_means, std_dev_of_sample_means = sampling_dist(population, sample_size)

# Display the results
print(result)
print("\nMean of Sample Means:", mean_of_sample_means)
print("Standard Deviation of Sample Means:", std_dev_of_sample_means)
