import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = e^(-|x|)
def f(x):
    return np.exp(-np.abs(x))

# Define the derivative of f(x)
def f_derivative(x):
    return np.where(x > 0, -np.exp(-x), np.where(x < 0, np.exp(x), 0))  # 0 at x=0 for visualization

# Generate input values
x = np.linspace(-5, 5, 1000)

# Compute function and derivative
y = f(x)
y_prime = f_derivative(x)

# Plotting
plt.figure(figsize=(10, 5))

# Plot f(x)
plt.plot(x, y, label=r'$f(x) = e^{-|x|}$', color='blue')

# Plot f'(x)
plt.plot(x, y_prime, label=r"$f'(x)$", color='orange', linestyle='--')

# Formatting
plt.title("Function and Derivative: $f(x) = e^{-|x|}$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
