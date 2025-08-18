import numpy as np
import matplotlib.pyplot as plt

# Define tanh function
def tanh(x):
    return np.tanh(x)

# Define derivative of tanh function
def tanh_derivative(x):
    return 1 - np.tanh(x)**2

# Generate input values
x = np.linspace(-10, 10, 1000)

# Compute tanh and its derivative
y_tanh = tanh(x)
y_derivative = tanh_derivative(x)

# Plotting
plt.figure(figsize=(10, 5))

# Tanh Plot
plt.subplot(1, 2, 1)
plt.plot(x, y_tanh, label="Tanh", color='purple')
plt.title("Tanh Function")
plt.xlabel("x")
plt.ylabel("tanh(x)")
plt.grid(True)
plt.legend()

# Derivative Plot
plt.subplot(1, 2, 2)
plt.plot(x, y_derivative, label="Tanh Derivative", color='brown')
plt.title("Derivative of Tanh")
plt.xlabel("x")
plt.ylabel("d(tanh)/dx")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
