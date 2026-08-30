# Week 5 - K-Fold Cross-Validation
# Random Forest Classifier

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score
import numpy as np


# -------------------------------------------------
# 1. Load the Iris dataset
# -------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target


# -------------------------------------------------
# 2. Create the Random Forest model
# -------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# -------------------------------------------------
# 3. Create 5-Fold Cross-Validation
# -------------------------------------------------

kfold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


# -------------------------------------------------
# 4. Run Cross-Validation
# -------------------------------------------------

scores = cross_val_score(
    model,
    X,
    y,
    cv=kfold,
    scoring="accuracy"
)


# -------------------------------------------------
# 5. Display Individual Fold Scores
# -------------------------------------------------

print("Random Forest - 5-Fold Cross-Validation")
print("----------------------------------------")

for i, score in enumerate(scores):
    print(f"Fold {i + 1} Accuracy: {score:.4f}")


# -------------------------------------------------
# 6. Calculate Average Accuracy
# -------------------------------------------------

average_score = np.mean(scores)

print("\nCross-Validation Results")
print("------------------------")

print(f"Average Accuracy: {average_score:.4f}")
print(f"Average Accuracy: {average_score * 100:.2f}%")

print(f"Standard Deviation: {np.std(scores):.4f}")