# Week 5 - Random Forest vs Decision Tree
# Iris Dataset

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# 2. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------------------------
# 3. Train a Single Decision Tree
# -------------------------------------------------

decision_tree = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

decision_tree.fit(X_train, y_train)

# Predictions
dt_predictions = decision_tree.predict(X_test)

# Accuracy
dt_accuracy = accuracy_score(y_test, dt_predictions)

# Feature importance
dt_importance = decision_tree.feature_importances_


# -------------------------------------------------
# 4. Train a Random Forest
# -------------------------------------------------

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

random_forest.fit(X_train, y_train)

# Predictions
rf_predictions = random_forest.predict(X_test)

# Accuracy
rf_accuracy = accuracy_score(y_test, rf_predictions)

# Feature importance
rf_importance = random_forest.feature_importances_


# -------------------------------------------------
# 5. Display Accuracy Comparison
# -------------------------------------------------

print("Model Accuracy Comparison")
print("-------------------------")
print(f"Decision Tree Accuracy : {dt_accuracy:.2f}")
print(f"Random Forest Accuracy : {rf_accuracy:.2f}")


# -------------------------------------------------
# 6. Display Feature Importance
# -------------------------------------------------

print("\nFeature Importance")
print("-----------------")

for feature, dt_imp, rf_imp in zip(
    iris.feature_names,
    dt_importance,
    rf_importance
):
    print(f"{feature}")
    print(f"  Decision Tree : {dt_imp:.4f}")
    print(f"  Random Forest : {rf_imp:.4f}")


# -------------------------------------------------
# 7. Plot Feature Importance Comparison
# -------------------------------------------------

x = np.arange(len(iris.feature_names))
width = 0.35

plt.figure(figsize=(12, 6))

plt.bar(
    x - width / 2,
    dt_importance,
    width,
    label="Decision Tree"
)

plt.bar(
    x + width / 2,
    rf_importance,
    width,
    label="Random Forest"
)

plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Importance: Decision Tree vs Random Forest")

plt.xticks(
    x,
    iris.feature_names,
    rotation=20
)

plt.legend()
plt.tight_layout()

plt.savefig(
    "feature_importance_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()