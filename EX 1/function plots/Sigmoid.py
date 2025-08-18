import numpy as np
import matplotlib.pyplot as plt

# Define sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define derivative of sigmoid function
def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

# Generate input values
x = np.linspace(-10, 10, 1000)

# Compute sigmoid and its derivative
y_sigmoid = sigmoid(x)
y_derivative = sigmoid_derivative(x)

# Plotting
plt.figure(figsize=(10, 5))

# Sigmoid Plot
plt.subplot(1, 2, 1)
plt.plot(x, y_sigmoid, label="Sigmoid", color='green')
plt.title("Sigmoid Function")
plt.xlabel("x")
plt.ylabel("σ(x)")
plt.grid(True)
plt.legend()

# Derivative Plot
plt.subplot(1, 2, 2)
plt.plot(x, y_derivative, label="Sigmoid Derivative", color='orange')
plt.title("Derivative of Sigmoid")
plt.xlabel("x")
plt.ylabel("d(σ)/dx")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
