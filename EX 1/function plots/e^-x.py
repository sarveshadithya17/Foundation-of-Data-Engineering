import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = e^(-x)
def f(x):
    return np.exp(-x)

# Define its derivative f'(x) = -e^(-x)
def f_derivative(x):
    return -np.exp(-x)

# Generate x values
x = np.linspace(-5, 5, 500)

# Compute y values
y = f(x)
y_prime = f_derivative(x)

# Plotting
plt.figure(figsize=(10, 5))

# f(x) Plot
plt.plot(x, y, label=r'$f(x) = e^{-x}$', color='blue')

# f'(x) Plot
plt.plot(x, y_prime, label=r"$f'(x) = -e^{-x}$", color='red', linestyle='--')

# Formatting
plt.title("Function and Derivative: $f(x) = e^{-x}$")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
