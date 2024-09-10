x =(1)
# Probability density function for a normal distribution
dnorm(x, mean = 0, sd = 1)

# Probability density function for a uniform distribution
dunif(x, min = 0, max = 1)

# Probability density function for an exponential distribution
dexp(x, rate = 1)
# PDF for chi-squared distribution
dchisq(x, df = 2)

# Load the MASS package
library(MASS)

data <- c(1,2,3,4,5,5)
# Fit a normal distribution to data
fit <- fitdistr(data, "normal")

# Install the package if not already installed
install.packages("fitdistrplus")

# Load the package
library(fitdistrplus)

# Fit a normal distribution to some data
fit <- fitdist(data, "norm")

# Get the density function
pdf <- function(x) {
  dnorm(x, mean = fit$estimate["mean"], sd = fit$estimate["sd"])
}
