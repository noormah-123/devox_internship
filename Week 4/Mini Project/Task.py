# Mini Project
# Marks Predictor & Pass/Fail Classifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    mean_absolute_error, mean_squared_error, r2_score,
    accuracy_score, precision_score, recall_score,
    confusion_matrix, classification_report
)
# Create Dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 4.2],
    "Marks": [15, 25, 35, 45, 55, 65, 75, 85, 90, 95,
              20, 30, 40, 50, 60, 70, 80, 88, 92, 48]
}

df = pd.DataFrame(data)
df["Pass"] = (df["Marks"] >= 50).astype(int)   # 1 = Pass, 0 = Fail

print("✅ Dataset Preview:")
print(df.head(10))
print("-" * 55)

# REGRESSION MODEL — Predict Marks
X = df[["Hours"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

reg_model = LinearRegression()
reg_model.fit(X_train, y_train)
y_pred = reg_model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📈 REGRESSION MODEL — Marks Predictor")
print(f"Equation : Marks = {reg_model.coef_[0]:.2f} * Hours + {reg_model.intercept_:.2f}")
print(f"MAE : {mae:.2f}")
print(f"MSE : {mse:.2f}")
print(f"R²  : {r2:.4f}")
print("-" * 55)

# Predict example
hours_example = [[6.5]]
predicted_marks = reg_model.predict(hours_example)[0]
print(f"🎯 Predicted Marks for 6.5 study hours: {predicted_marks:.2f}")

# CLASSIFICATION MODEL — Pass / Fail
X_cls = df[["Hours"]]
y_cls = df["Pass"]

Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    X_cls, y_cls, test_size=0.2, random_state=42
)

clf_model = LogisticRegression()
clf_model.fit(Xc_train, yc_train)
yc_pred = clf_model.predict(Xc_test)

acc = accuracy_score(yc_test, yc_pred)
prec = precision_score(yc_test, yc_pred, zero_division=0)
rec = recall_score(yc_test, yc_pred, zero_division=0)

print("\n✅ CLASSIFICATION MODEL — Pass/Fail Predictor")
print(f"Accuracy  : {acc:.4f}")
print(f"Precision : {prec:.4f}")
print(f"Recall    : {rec:.4f}")
print("\n📋 Classification Report:")
print(classification_report(yc_test, yc_pred, zero_division=0))

# Predict example
hours_example = [[4]]
prediction = clf_model.predict(hours_example)[0]
status = "PASS ✅" if prediction == 1 else "FAIL ❌"
print(f"🎯 Prediction for 4 study hours: {status}")

# STEP 4: VISUALIZATIONS
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# --- Regression Plot ---
axes[0].scatter(df["Hours"], df["Marks"], color="blue", label="Actual")
axes[0].plot(df["Hours"], reg_model.predict(df[["Hours"]]),
             color="red", label="Regression Line")
axes[0].set_title("Marks Predictor (Linear Regression)")
axes[0].set_xlabel("Study Hours")
axes[0].set_ylabel("Marks")
axes[0].legend()
axes[0].grid(True)

# --- Classification Plot ---
hours_range = np.linspace(0, 11, 200).reshape(-1, 1)
probs = clf_model.predict_proba(hours_range)[:, 1]

axes[1].scatter(df["Hours"], df["Pass"], color="black", label="Actual (0/1)")
axes[1].plot(hours_range, probs, color="green", label="Pass Probability")
axes[1].axhline(0.5, color="red", linestyle="--", label="Decision Boundary (0.5)")
axes[1].set_title("Pass/Fail Classifier (Logistic Regression)")
axes[1].set_xlabel("Study Hours")
axes[1].set_ylabel("Probability of Passing")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()

# STEP 5: EVALUATION SUMMARY
print("\n" + "=" * 55)
print("📊 FINAL EVALUATION SUMMARY")
print("=" * 55)
print(f"""
📈 Regression Model (Marks Predictor)
- Predicts student marks based on study hours.
- MAE: {mae:.2f}, MSE: {mse:.2f}, R²: {r2:.4f}
- The model fits the data very well and can accurately
  estimate marks for a given number of study hours.

✅ Classification Model (Pass/Fail Predictor)
- Predicts if a student will pass (≥50 marks) or fail.
- Accuracy: {acc:.2f}, Precision: {prec:.2f}, Recall: {rec:.2f}
- The model successfully separates passing and failing
  students using study hours as the deciding factor.

🎯 Conclusion:
Study hours are a strong predictor of both marks and
pass/fail outcomes. This project shows how regression
and classification can work together to solve real-world
problems.
""")