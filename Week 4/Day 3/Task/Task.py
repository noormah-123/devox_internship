
# Linear Regression Using scikit-learn
# Evaluate with MAE, MSE, and R²
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Sample Dataset
# Example: Hours studied vs Marks scored
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
Y = np.array([2, 4, 6, 8, 11, 13, 15, 17, 20, 22])

# Split Data 
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, Y_train)

# Predictions
Y_pred = model.predict(X_test)

# Model Info
print(" Model Trained Successfully!")
print(f"Slope (m)     : {model.coef_[0]:.4f}")
print(f"Intercept (b) : {model.intercept_:.4f}")
print(f"Equation      : y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")
print("-" * 45)

# Evaluation Metrics 
mae = mean_absolute_error(Y_test, Y_pred)
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print("📊 Model Evaluation:")
print(f"MAE  (Mean Absolute Error): {mae:.4f}")
print(f"MSE  (Mean Squared Error) : {mse:.4f}")
print(f"R²   (R-squared Score)    : {r2:.4f}")
print("-" * 45)

# Visualization
plt.figure(figsize=(8, 5))
plt.scatter(X, Y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.scatter(X_test, Y_pred, color="green", marker="x", s=100, label="Predicted")
plt.title("Linear Regression using scikit-learn")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.grid(True)
plt.show()