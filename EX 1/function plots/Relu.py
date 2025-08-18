import numpy as np
import matplotlib.pyplot as plt

# Define ReLU function
def relu(x):
    return np.maximum(0, x)

# Define derivative of ReLU
def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Generate input values
x = np.linspace(-10, 10, 1000)

# Compute ReLU and its derivative
y_relu = relu(x)
y_derivative = relu_derivative(x)

# Plotting
plt.figure(figsize=(10, 5))

# ReLU Plot
plt.subplot(1, 2, 1)
plt.plot(x, y_relu, label="ReLU", color='blue')
plt.title("ReLU Function")
plt.xlabel("x")
plt.ylabel("ReLU(x)")
plt.grid(True)
plt.legend()

# Derivative Plot
plt.subplot(1, 2, 2)
plt.plot(x, y_derivative, label="ReLU Derivative", color='red')
plt.title("Derivative of ReLU")
plt.xlabel("x")
plt.ylabel("d(ReLU)/dx")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
