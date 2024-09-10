from scipy.integrate import quad

# Define the PDF function
def pdf(x):
    return 1.0/7.0

# Integrate to find the probability between 0.2 and 0.8
prob, err = quad(pdf, 1.0, 8.0)
print(f"Probability: {prob}")
print(f"Error estimate: {err}")
