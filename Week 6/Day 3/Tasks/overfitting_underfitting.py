import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error


# -----------------------------
# 1. Create a toy dataset
# -----------------------------

np.random.seed(42)

X = np.linspace(-3, 3, 30).reshape(-1, 1)

# Actual relationship
y = np.sin(X).ravel()

# Add some random noise
y = y + np.random.normal(0, 0.15, size=len(y))


# -----------------------------
# 2. Split into train and test
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)


# -----------------------------
# 3. Try different model
#    complexity levels
# -----------------------------

degrees = range(1, 16)

train_errors = []
test_errors = []


for degree in degrees:

    # Create polynomial regression model
    model = make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression()
    )

    # Train the model
    model.fit(X_train, y_train)

    # Predictions
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    # Calculate errors
    train_error = mean_squared_error(
        y_train,
        train_predictions
    )

    test_error = mean_squared_error(
        y_test,
        test_predictions
    )

    train_errors.append(train_error)
    test_errors.append(test_error)


# -----------------------------
# 4. Plot train vs test error
# -----------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    degrees,
    train_errors,
    marker="o",
    label="Training Error"
)

plt.plot(
    degrees,
    test_errors,
    marker="o",
    label="Test Error"
)

plt.xlabel("Model Complexity (Polynomial Degree)")
plt.ylabel("Mean Squared Error")

plt.title("Overfitting vs Underfitting")

plt.legend()
plt.grid(True)

plt.show()