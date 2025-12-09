"""
Comprehensive Probability Distributions Implementation
This file demonstrates various probability distributions including:
1. Normal Distribution
2. Poisson Distribution
3. Bernoulli Distribution
4. Binomial Distribution
5. Exponential Distribution
6. Uniform Distribution

Each distribution includes:
- Mathematical implementation
- Random sampling
- Visualization using Matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math
from collections import Counter
import seaborn as sns

# Set style for better plots
plt.style.use('seaborn-v0_8')
np.random.seed(42)  # For reproducible results

class ProbabilityDistributions:
    """Class containing various probability distribution implementations"""

    @staticmethod
    def normal_distribution(mu=0, sigma=1, size=1000):
        """
        Normal Distribution Implementation
        Parameters:
        - mu: mean
        - sigma: standard deviation
        - size: number of samples
        """
        print("="*60)
        print("NORMAL DISTRIBUTION")
        print("="*60)
        print(f"Parameters: μ = {mu}, σ = {sigma}")

        # Generate random samples
        samples = np.random.normal(mu, sigma, size)

        # Theoretical PDF
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
        pdf = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

        # Create visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Histogram with PDF overlay
        ax1.hist(samples, bins=50, density=True, alpha=0.7, color='skyblue',
                edgecolor='black', label='Sample Data')
        ax1.plot(x, pdf, 'r-', linewidth=2, label=f'Theoretical PDF\nμ={mu}, σ={sigma}')
        ax1.axvline(np.mean(samples), color='green', linestyle='--',
                   label=f'Sample Mean = {np.mean(samples):.2f}')
        ax1.set_title('Normal Distribution - Histogram vs PDF')
        ax1.set_xlabel('Value')
        ax1.set_ylabel('Density')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Q-Q plot to check normality
        stats.probplot(samples, dist="norm", plot=ax2)
        ax2.set_title('Q-Q Plot (Normal Distribution)')
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

        # Statistics
        print(f"Sample Statistics:")
        print(f"Mean: {np.mean(samples):.4f} (Expected: {mu})")
        print(f"Standard Deviation: {np.std(samples, ddof=1):.4f} (Expected: {sigma})")
        print(f"Variance: {np.var(samples, ddof=1):.4f} (Expected: {sigma**2})")

        return samples

    @staticmethod
    def poisson_distribution(lam=3, size=1000):
        """
        Poisson Distribution Implementation
        Parameters:
        - lam: rate parameter (λ)
        - size: number of samples
        """
        print("\n" + "="*60)
        print("POISSON DISTRIBUTION")
        print("="*60)
        print(f"Parameter: λ = {lam}")

        # Generate random samples
        samples = np.random.poisson(lam, size)

        # Theoretical PMF
        k_max = max(samples) + 5
        k = np.arange(0, k_max)
        pmf = (lam**k * np.exp(-lam)) / np.array([math.factorial(i) for i in k])

        # Create visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Histogram with PMF overlay
        unique, counts = np.unique(samples, return_counts=True)
        ax1.bar(unique, counts/size, alpha=0.7, color='lightgreen',
               edgecolor='black', label='Sample Data')
        ax1.plot(k, pmf, 'ro-', linewidth=2, markersize=4,
                label=f'Theoretical PMF\nλ={lam}')
        ax1.axvline(np.mean(samples), color='blue', linestyle='--',
                   label=f'Sample Mean = {np.mean(samples):.2f}')
        ax1.set_title('Poisson Distribution - Histogram vs PMF')
        ax1.set_xlabel('Value (k)')
        ax1.set_ylabel('Probability')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Cumulative distribution
        sample_counts = Counter(samples)
        k_sample = sorted(sample_counts.keys())
        cdf_sample = np.cumsum([sample_counts[k]/size for k in k_sample])
        cdf_theoretical = stats.poisson.cdf(k, lam)

        ax2.step(k_sample, cdf_sample, where='post', label='Sample CDF', linewidth=2)
        ax2.plot(k, cdf_theoretical, 'r-', label='Theoretical CDF', linewidth=2)
        ax2.set_title('Cumulative Distribution Function')
        ax2.set_xlabel('Value (k)')
        ax2.set_ylabel('P(X ≤ k)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

        # Statistics
        print(f"Sample Statistics:")
        print(f"Mean: {np.mean(samples):.4f} (Expected: {lam})")
        print(f"Variance: {np.var(samples, ddof=1):.4f} (Expected: {lam})")
        print(f"Min: {np.min(samples)}, Max: {np.max(samples)}")

        return samples

    @staticmethod
    def bernoulli_distribution(p=0.3, size=1000):
        """
        Bernoulli Distribution Implementation
        Parameters:
        - p: probability of success
        - size: number of trials
        """
        print("\n" + "="*60)
        print("BERNOULLI DISTRIBUTION")
        print("="*60)
        print(f"Parameter: p = {p}")

        # Generate random samples
        samples = np.random.binomial(1, p, size)

        # Calculate sample proportions
        successes = np.sum(samples)
        failures = size - successes
        sample_p = successes / size

        # Create visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Bar plot
        categories = ['Failure (0)', 'Success (1)']
        sample_probs = [failures/size, successes/size]
        theoretical_probs = [1-p, p]

        x = np.arange(len(categories))
        width = 0.35

        ax1.bar(x - width/2, sample_probs, width, label='Sample',
               alpha=0.7, color='lightcoral')
        ax1.bar(x + width/2, theoretical_probs, width, label='Theoretical',
               alpha=0.7, color='lightblue')
        ax1.set_title('Bernoulli Distribution - Sample vs Theoretical')
        ax1.set_xlabel('Outcome')
        ax1.set_ylabel('Probability')
        ax1.set_xticks(x)
        ax1.set_xticklabels(categories)
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Time series of trials
        cumulative_avg = np.cumsum(samples) / np.arange(1, size + 1)
        ax2.plot(cumulative_avg, color='purple', linewidth=1)
        ax2.axhline(y=p, color='red', linestyle='--', linewidth=2,
                   label=f'True p = {p}')
        ax2.axhline(y=sample_p, color='green', linestyle='--', linewidth=2,
                   label=f'Sample p = {sample_p:.3f}')
        ax2.set_title('Law of Large Numbers - Convergence to True Probability')
        ax2.set_xlabel('Number of Trials')
        ax2.set_ylabel('Cumulative Average')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

        # Statistics
        print(f"Sample Statistics:")
        print(f"Successes: {successes} out of {size} trials")
        print(f"Sample probability: {sample_p:.4f} (Expected: {p})")
        print(f"Sample mean: {np.mean(samples):.4f} (Expected: {p})")
        print(f"Sample variance: {np.var(samples, ddof=1):.4f} (Expected: {p*(1-p):.4f})")

        return samples

    @staticmethod
    def binomial_distribution(n=20, p=0.3, size=1000):
        """
        Binomial Distribution Implementation
        Parameters:
        - n: number of trials
        - p: probability of success
        - size: number of experiments
        """
        print("\n" + "="*60)
        print("BINOMIAL DISTRIBUTION")
        print("="*60)
        print(f"Parameters: n = {n}, p = {p}")

        # Generate random samples
        samples = np.random.binomial(n, p, size)

        # Theoretical PMF
        k = np.arange(0, n + 1)
        pmf = stats.binom.pmf(k, n, p)

        # Create visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Histogram with PMF overlay
        unique, counts = np.unique(samples, return_counts=True)
        ax1.bar(unique, counts/size, alpha=0.7, color='orange',
               edgecolor='black', label='Sample Data', width=0.8)
        ax1.plot(k, pmf, 'ro-', linewidth=2, markersize=4,
                label=f'Theoretical PMF\nn={n}, p={p}')
        ax1.axvline(np.mean(samples), color='green', linestyle='--',
                   label=f'Sample Mean = {np.mean(samples):.2f}')
        ax1.set_title('Binomial Distribution - Histogram vs PMF')
        ax1.set_xlabel('Number of Successes (k)')
        ax1.set_ylabel('Probability')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Box plot and violin plot
        ax2.boxplot(samples, patch_artist=True,
                   boxprops=dict(facecolor='lightblue', alpha=0.7))
        ax2.set_title('Binomial Distribution - Box Plot')
        ax2.set_ylabel('Number of Successes')
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

        # Statistics
        theoretical_mean = n * p
        theoretical_var = n * p * (1 - p)

        print(f"Sample Statistics:")
        print(f"Mean: {np.mean(samples):.4f} (Expected: {theoretical_mean})")
        print(f"Variance: {np.var(samples, ddof=1):.4f} (Expected: {theoretical_var})")
        print(f"Standard Deviation: {np.std(samples, ddof=1):.4f} (Expected: {np.sqrt(theoretical_var):.4f})")

        return samples

    @staticmethod
    def exponential_distribution(lam=1.5, size=1000):
        """
        Exponential Distribution Implementation
        Parameters:
        - lam: rate parameter (λ)
        - size: number of samples
        """
        print("\n" + "="*60)
        print("EXPONENTIAL DISTRIBUTION")
        print("="*60)
        print(f"Parameter: λ = {lam}")

        # Generate random samples
        samples = np.random.exponential(1/lam, size)

        # Theoretical PDF and CDF
        x = np.linspace(0, np.max(samples), 1000)
        pdf = lam * np.exp(-lam * x)
        cdf = 1 - np.exp(-lam * x)

        # Create visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Histogram with PDF overlay
        ax1.hist(samples, bins=50, density=True, alpha=0.7, color='salmon',
                edgecolor='black', label='Sample Data')
        ax1.plot(x, pdf, 'b-', linewidth=2, label=f'Theoretical PDF\nλ={lam}')
        ax1.axvline(np.mean(samples), color='green', linestyle='--',
                   label=f'Sample Mean = {np.mean(samples):.2f}')
        ax1.set_title('Exponential Distribution - Histogram vs PDF')
        ax1.set_xlabel('Value')
        ax1.set_ylabel('Density')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # CDF comparison
        sample_sorted = np.sort(samples)
        sample_cdf = np.arange(1, len(sample_sorted) + 1) / len(sample_sorted)
        theoretical_cdf = 1 - np.exp(-lam * sample_sorted)

        ax2.plot(sample_sorted, sample_cdf, 'g-', linewidth=2, label='Sample CDF')
        ax2.plot(sample_sorted, theoretical_cdf, 'r--', linewidth=2, label='Theoretical CDF')
        ax2.set_title('Cumulative Distribution Function')
        ax2.set_xlabel('Value')
        ax2.set_ylabel('P(X ≤ x)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

        # Statistics
        theoretical_mean = 1/lam
        theoretical_var = 1/(lam**2)

        print(f"Sample Statistics:")
        print(f"Mean: {np.mean(samples):.4f} (Expected: {theoretical_mean:.4f})")
        print(f"Variance: {np.var(samples, ddof=1):.4f} (Expected: {theoretical_var:.4f})")
        print(f"Median: {np.median(samples):.4f} (Expected: {np.log(2)/lam:.4f})")

        return samples

    @staticmethod
    def uniform_distribution(a=0, b=10, size=1000):
        """
        Uniform Distribution Implementation
        Parameters:
        - a: lower bound
        - b: upper bound
        - size: number of samples
        """
        print("\n" + "="*60)
        print("UNIFORM DISTRIBUTION")
        print("="*60)
        print(f"Parameters: a = {a}, b = {b}")

        # Generate random samples
        samples = np.random.uniform(a, b, size)

        # Theoretical PDF
        pdf_value = 1/(b-a)

        # Create visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Histogram with PDF overlay
        ax1.hist(samples, bins=30, density=True, alpha=0.7, color='gold',
                edgecolor='black', label='Sample Data')
        ax1.axhline(y=pdf_value, color='red', linewidth=3,
                   label=f'Theoretical PDF = {pdf_value:.3f}')
        ax1.axvline(np.mean(samples), color='green', linestyle='--',
                   label=f'Sample Mean = {np.mean(samples):.2f}')
        ax1.axvline((a+b)/2, color='blue', linestyle=':',
                   label=f'Theoretical Mean = {(a+b)/2:.2f}')
        ax1.set_title('Uniform Distribution - Histogram vs PDF')
        ax1.set_xlabel('Value')
        ax1.set_ylabel('Density')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim(a-1, b+1)

        # Scatter plot to show randomness
        ax2.scatter(range(len(samples[:100])), samples[:100], alpha=0.6, color='purple')
        ax2.axhline(y=(a+b)/2, color='red', linestyle='--', label=f'Mean = {(a+b)/2}')
        ax2.axhline(y=a, color='gray', linestyle=':', label=f'Lower bound = {a}')
        ax2.axhline(y=b, color='gray', linestyle=':', label=f'Upper bound = {b}')
        ax2.set_title('First 100 Random Samples')
        ax2.set_xlabel('Sample Index')
        ax2.set_ylabel('Value')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

        # Statistics
        theoretical_mean = (a + b) / 2
        theoretical_var = (b - a)**2 / 12

        print(f"Sample Statistics:")
        print(f"Mean: {np.mean(samples):.4f} (Expected: {theoretical_mean})")
        print(f"Variance: {np.var(samples, ddof=1):.4f} (Expected: {theoretical_var:.4f})")
        print(f"Min: {np.min(samples):.4f} (Expected: ≥ {a})")
        print(f"Max: {np.max(samples):.4f} (Expected: ≤ {b})")

        return samples

def compare_distributions():
    """Compare multiple distributions side by side"""
    print("\n" + "="*80)
    print("DISTRIBUTION COMPARISON")
    print("="*80)

    # Generate samples from different distributions
    normal_samples = np.random.normal(0, 1, 1000)
    poisson_samples = np.random.poisson(3, 1000)
    exponential_samples = np.random.exponential(1, 1000)
    uniform_samples = np.random.uniform(-3, 3, 1000)

    # Create comparison plot
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    # Normal
    axes[0,0].hist(normal_samples, bins=50, density=True, alpha=0.7, color='skyblue')
    axes[0,0].set_title('Normal Distribution\nμ=0, σ=1')
    axes[0,0].set_xlabel('Value')
    axes[0,0].set_ylabel('Density')
    axes[0,0].grid(True, alpha=0.3)

    # Poisson
    axes[0,1].hist(poisson_samples, bins=range(0, max(poisson_samples)+2),
                  density=True, alpha=0.7, color='lightgreen')
    axes[0,1].set_title('Poisson Distribution\nλ=3')
    axes[0,1].set_xlabel('Value')
    axes[0,1].set_ylabel('Density')
    axes[0,1].grid(True, alpha=0.3)

    # Exponential
    axes[1,0].hist(exponential_samples, bins=50, density=True, alpha=0.7, color='salmon')
    axes[1,0].set_title('Exponential Distribution\nλ=1')
    axes[1,0].set_xlabel('Value')
    axes[1,0].set_ylabel('Density')
    axes[1,0].grid(True, alpha=0.3)

    # Uniform
    axes[1,1].hist(uniform_samples, bins=50, density=True, alpha=0.7, color='gold')
    axes[1,1].set_title('Uniform Distribution\na=-3, b=3')
    axes[1,1].set_xlabel('Value')
    axes[1,1].set_ylabel('Density')
    axes[1,1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

def main():
    """Main function to demonstrate all distributions"""
    print("PROBABILITY DISTRIBUTIONS IMPLEMENTATION AND VISUALIZATION")
    print("="*80)
    print("This program demonstrates various probability distributions with:")
    print("- Mathematical implementation")
    print("- Random sampling")
    print("- Statistical analysis")
    print("- Visual comparisons")
    print()

    # Create instance of the class
    dist = ProbabilityDistributions()

    # Demonstrate each distribution
    normal_samples = dist.normal_distribution(mu=5, sigma=2, size=1000)
    poisson_samples = dist.poisson_distribution(lam=4, size=1000)
    bernoulli_samples = dist.bernoulli_distribution(p=0.4, size=1000)
    binomial_samples = dist.binomial_distribution(n=15, p=0.6, size=1000)
    exponential_samples = dist.exponential_distribution(lam=0.5, size=1000)
    uniform_samples = dist.uniform_distribution(a=2, b=8, size=1000)

    # Compare all distributions
    compare_distributions()

    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print("All probability distributions have been successfully implemented and visualized!")
    print("Key features demonstrated:")
    print("1. Normal Distribution - Bell curve, symmetric")
    print("2. Poisson Distribution - Discrete, counts of events")
    print("3. Bernoulli Distribution - Binary outcomes")
    print("4. Binomial Distribution - Sum of Bernoulli trials")
    print("5. Exponential Distribution - Waiting times, skewed")
    print("6. Uniform Distribution - Equal probability over interval")

if __name__ == "__main__":
    main()