from scipy.stats import norm

# Standard normal distribution: mean=0, std=1
mean = 7
std = 13

# P(0)
p0 = norm.cdf(mean, loc=mean, scale=std)
print(f"P(x <= 0): {p0}")

# P(-1 < x <= 1)
p1 = norm.cdf(mean - std, loc=mean, scale=std) - norm.cdf(mean + std, loc=mean, scale=std)
print(f"P(-1 < x <= 1): {p1}")

# P(-2 < x <= 2)
p2 = norm.cdf(mean + 2*std, loc=mean, scale=std) - norm.cdf(mean - 2*std, loc=mean, scale=std)
print(f"P(-2 < x <= 2): {p2}")

# P(-3 < x <= 3)
p3 = norm.cdf(mean + 3*std, loc=mean, scale=std) - norm.cdf(mean - 3*std, loc=mean, scale=std)
print(f"P(-3 < x <= 3): {p3}")