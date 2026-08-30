# Logistic Regression Classifier
# Evaluate with Accuracy, Precision, and Recall
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    confusion_matrix, classification_report
)
import seaborn as sns

# Load Dataset
# Built-in Breast Cancer dataset (binary classification)
data = load_breast_cancer()
X = data.data
y = data.target   # 0 = malignant, 1 = benign

print("✅ Dataset Loaded")
print(f"Total Samples : {X.shape[0]}")
print(f"Features      : {X.shape[1]}")
print(f"Classes       : {data.target_names}")
print("-" * 45)

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# Predictions 
y_pred = model.predict(X_test)

# Evaluation Metrics 
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("📊 Model Evaluation:")
print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print("-" * 45)

#  Detailed Report
print("📋 Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=data.target_names,
            yticklabels=data.target_names)
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()