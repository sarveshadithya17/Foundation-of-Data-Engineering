import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = e^(-x^2)
def f(x):
    return np.exp(-x**2)

# Define its derivative f'(x) = -2x * e^(-x^2)
def f_derivative(x):
    return -2 * x * np.exp(-x**2)

# Generate x values
x = np.linspace(-3, 3, 500)

# Compute y values
y = f(x)
y_prime = f_derivative(x)

# Plotting
plt.figure(figsize=(10, 5))

# Plot f(x)
plt.plot(x, y, label=r'$f(x) = e^{-x^2}$', color='blue')

# Plot f'(x)
plt.plot(x, y_prime, label=r"$f'(x) = -2x e^{-x^2}$", color='red', linestyle='--')

# Formatting
plt.title("Function and Derivative: $f(x) = e^{-x^2}$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
