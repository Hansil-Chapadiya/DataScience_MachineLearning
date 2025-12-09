import matplotlib.pyplot as plt
import numpy as np
import statistics
from collections import Counter

# Sample dataset
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
        3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Calculate measures of central tendency
mean_value = statistics.mean(data)
median_value = statistics.median(data)

# Calculate mode(s)
def find_mode(data):
    """Find mode(s) in the dataset"""
    frequency = Counter(data)
    max_freq = max(frequency.values())
    modes = [key for key, freq in frequency.items() if freq == max_freq]
    return modes

modes = find_mode(data)
mode_value = modes[0] if len(modes) == 1 else modes  # Use first mode for plotting

print(f"Dataset: {sorted(data)}")
print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value}")
print(f"Mode(s): {modes}")

# Create the histogram
plt.figure(figsize=(12, 8))

# Plot histogram
n, bins, patches = plt.hist(data, bins=15, alpha=0.7, color='skyblue',
                           edgecolor='black', density=False)

# Add vertical lines for mean, median, and mode
plt.axvline(mean_value, color='red', linestyle='--', linewidth=2,
           label=f'Mean = {mean_value:.2f}')
plt.axvline(median_value, color='green', linestyle='--', linewidth=2,
           label=f'Median = {median_value}')

# If there's a single mode, plot it
if isinstance(mode_value, (int, float)):
    plt.axvline(mode_value, color='orange', linestyle='--', linewidth=2,
               label=f'Mode = {mode_value}')
else:
    # If multiple modes, plot all of them
    for i, mode in enumerate(modes):
        plt.axvline(mode, color='orange', linestyle='--', linewidth=2,
                   label=f'Mode {i+1} = {mode}' if i == 0 else f'Mode {i+1} = {mode}')

# Customize the plot
plt.title('Histogram with Measures of Central Tendency', fontsize=16, fontweight='bold')
plt.xlabel('Values', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# Add text box with statistics
stats_text = f'Mean: {mean_value:.2f}\nMedian: {median_value}\nMode(s): {modes}'
plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Show the plot
plt.tight_layout()
plt.show()

# Create a second plot with a normal distribution for comparison
print("\n" + "="*50)
print("Creating a second histogram with normal distribution")
print("="*50)

# Generate normal distribution data
np.random.seed(42)
normal_data = np.random.normal(50, 15, 1000)

# Calculate measures for normal data
normal_mean = statistics.mean(normal_data)
normal_median = statistics.median(normal_data)
normal_modes = find_mode([round(x) for x in normal_data])  # Round for mode calculation

print(f"Normal distribution data (n=1000)")
print(f"Mean: {normal_mean:.2f}")
print(f"Median: {normal_median:.2f}")
print(f"Mode(s) of rounded data: {normal_modes[:5]}...")  # Show first 5 modes

# Create second histogram
plt.figure(figsize=(12, 8))

# Plot histogram for normal data
n2, bins2, patches2 = plt.hist(normal_data, bins=30, alpha=0.7, color='lightgreen',
                              edgecolor='black', density=False)

# Add vertical lines
plt.axvline(normal_mean, color='red', linestyle='--', linewidth=2,
           label=f'Mean = {normal_mean:.2f}')
plt.axvline(normal_median, color='green', linestyle='--', linewidth=2,
           label=f'Median = {normal_median:.2f}')

# For normal distribution, mean ≈ median ≈ mode, so we'll show the theoretical mode
plt.axvline(normal_mean, color='orange', linestyle=':', linewidth=2,
           label=f'Mode ≈ {normal_mean:.2f} (theoretical)')

# Customize the plot
plt.title('Normal Distribution Histogram with Measures of Central Tendency',
          fontsize=16, fontweight='bold')
plt.xlabel('Values', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# Add text box with statistics
normal_stats_text = f'Mean: {normal_mean:.2f}\nMedian: {normal_median:.2f}\nMode ≈ Mean (normal dist.)'
plt.text(0.02, 0.98, normal_stats_text, transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

plt.tight_layout()
plt.show()

# Create a third plot showing skewed distribution
print("\n" + "="*50)
print("Creating a third histogram with skewed distribution")
print("="*50)

# Generate skewed data
skewed_data = np.random.exponential(2, 1000)

# Calculate measures for skewed data
skewed_mean = statistics.mean(skewed_data)
skewed_median = statistics.median(skewed_data)
skewed_modes = find_mode([round(x, 1) for x in skewed_data])

print(f"Skewed distribution data (n=1000)")
print(f"Mean: {skewed_mean:.2f}")
print(f"Median: {skewed_median:.2f}")
print(f"Mode(s) of rounded data: {skewed_modes[:5]}...")

# Create third histogram
plt.figure(figsize=(12, 8))

# Plot histogram for skewed data
n3, bins3, patches3 = plt.hist(skewed_data, bins=30, alpha=0.7, color='salmon',
                              edgecolor='black', density=False)

# Add vertical lines
plt.axvline(skewed_mean, color='red', linestyle='--', linewidth=2,
           label=f'Mean = {skewed_mean:.2f}')
plt.axvline(skewed_median, color='green', linestyle='--', linewidth=2,
           label=f'Median = {skewed_median:.2f}')

# For exponential distribution, mode is at 0 (theoretical)
plt.axvline(0, color='orange', linestyle='--', linewidth=2,
           label='Mode = 0 (theoretical)')

# Customize the plot
plt.title('Skewed Distribution Histogram with Measures of Central Tendency',
          fontsize=16, fontweight='bold')
plt.xlabel('Values', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# Add text box with statistics
skewed_stats_text = f'Mean: {skewed_mean:.2f}\nMedian: {skewed_median:.2f}\nMode: 0 (theoretical)\n\nNote: Mean > Median\n(Right-skewed)'
plt.text(0.65, 0.98, skewed_stats_text, transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("Summary of Central Tendency Measures:")
print("="*60)
print("1. MEAN: Average of all values")
print("   - Affected by outliers")
print("   - Best for symmetric distributions")

print("\n2. MEDIAN: Middle value when data is sorted")
print("   - Not affected by outliers")
print("   - Best for skewed distributions")

print("\n3. MODE: Most frequently occurring value(s)")
print("   - Can have multiple modes")
print("   - Best for categorical data")
print("   - May not exist for continuous data")

print("\nIn the plots above:")
print("- Red line: Mean")
print("- Green line: Median")
print("- Orange line: Mode")