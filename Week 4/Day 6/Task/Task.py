# Decision Boundary Visualization
# Simple Classifier on a 2D Toy Dataset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from matplotlib.colors import ListedColormap

# Create Toy Dataset 
X, y = make_classification(
    n_samples=200,
    n_features=2,          # 2D for visualization
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=42
)

print("✅ Dataset Created")
print(f"Shape of X: {X.shape}")
print(f"Shape of y: {y.shape}")

# Train Classifier 
model = LogisticRegression()
model.fit(X, y)

print("✅ Model Trained Successfully")
print(f"Accuracy on Training Data: {model.score(X, y):.4f}")

# Create a Mesh Grid 
# We'll cover the whole feature space with tiny points
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 300),
    np.linspace(y_min, y_max, 300)
)

# Predict Over Grid
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot Decision Boundary
cmap_background = ListedColormap(["#FFAAAA", "#AAAAFF"])
cmap_points = ListedColormap(["#FF0000", "#0000FF"])

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.4, cmap=cmap_background)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_points, edgecolor="k", s=50)

plt.title("Decision Boundary - Logistic Regression")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()