# Sigmoid Function (Implemented Manually)

import numpy as np
import matplotlib.pyplot as plt

# Define Sigmoid
def sigmoid(x):
    """
    Sigmoid Activation Function
    Formula: 1 / (1 + e^(-x))
    Converts any number into a value between 0 and 1.
    """
    return 1 / (1 + np.exp(-x))

# Test With Sample Values 
test_values = [-10, -5, -1, 0, 1, 5, 10]

print("🔹 Sigmoid Function Test Values")
print("-" * 40)
for val in test_values:
    print(f"sigmoid({val:>3}) = {sigmoid(val):.6f}")
print("-" * 40)

# Visualize The Curve 
x = np.linspace(-10, 10, 200)
y = sigmoid(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color="blue", linewidth=2, label="Sigmoid Curve")
plt.axhline(0, color="black", linewidth=0.5)
plt.axhline(1, color="gray", linestyle="--", linewidth=0.7)
plt.axvline(0, color="red", linestyle="--", linewidth=0.7)
plt.title("Sigmoid Function")
plt.xlabel("Input (x)")
plt.ylabel("Output σ(x)")
plt.grid(True)
plt.legend()
plt.show()