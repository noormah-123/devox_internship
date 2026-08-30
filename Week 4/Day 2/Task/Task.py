
# Simple Linear Regression from Scratch
# Using Manual Gradient Descent (No sklearn)

import numpy as np
import matplotlib.pyplot as plt

# Sample Dataset
# y ≈ 2x + 1 (with some noise)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
Y = np.array([3, 5, 7, 9, 11, 13, 15, 17, 19, 21], dtype=float)

# Initialize Parameters
m = 0.0      # slope
b = 0.0      # intercept
lr = 0.01    # learning rate
epochs = 1000  # number of iterations
n = len(X)

# Gradient Descent
loss_history = []

for epoch in range(epochs):
    # Predictions
    y_pred = m * X + b

    # Error
    error = Y - y_pred

    # Loss (Mean Squared Error)
    loss = np.mean(error ** 2)
    loss_history.append(loss)

    # Gradients
    dm = (-2 / n) * np.sum(X * error)
    db = (-2 / n) * np.sum(error)

    # Update parameters
    m = m - lr * dm
    b = b - lr * db

    # Print progress every 100 steps
    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch+1}: Loss={loss:.4f}, m={m:.4f}, b={b:.4f}")

# Final Result
print("\nFinal Trained Model:")
print(f"Slope (m)     : {m:.4f}")
print(f"Intercept (b) : {b:.4f}")
print(f"Equation      : y = {m:.2f}x + {b:.2f}")

# Plot Results
plt.figure(figsize=(10, 4))

# Regression line
plt.subplot(1, 2, 1)
plt.scatter(X, Y, color="blue", label="Actual Data")
plt.plot(X, m * X + b, color="red", label="Best Fit Line")
plt.title("Linear Regression (From Scratch)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# Loss curve
plt.subplot(1, 2, 2)
plt.plot(loss_history, color="green")
plt.title("Loss Curve (MSE over Epochs)")
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.tight_layout()
plt.show()