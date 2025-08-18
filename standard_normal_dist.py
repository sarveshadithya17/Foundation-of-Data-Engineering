from scipy.stats import norm

# Standard normal distribution: mean=0, std=1
mean = 0
std = 1

# P(0)
p0 = norm.cdf(0, loc=mean, scale=std)
print(f"P(x <= 0): {p0}")

# P(-1 < x <= 1)
p1 = norm.cdf(1, loc=mean, scale=std) - norm.cdf(-1, loc=mean, scale=std)
print(f"P(-1 < x <= 1): {p1}")

# P(-2 < x <= 2)
p2 = norm.cdf(2, loc=mean, scale=std) - norm.cdf(-2, loc=mean, scale=std)
print(f"P(-2 < x <= 2): {p2}")

# P(-3 < x <= 3)
p3 = norm.cdf(3, loc=mean, scale=std) - norm.cdf(-3, loc=mean, scale=std)
print(f"P(-3 < x <= 3): {p3}")