# Decision Tree Classifier
# Week 5 - ML Foundations II

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Load the Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 3. Create the Decision Tree classifier
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

# 4. Train the model
model.fit(X_train, y_train)

# 5. Make predictions
y_pred = model.predict(X_test)

# 6. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Decision Tree Classifier")
print("------------------------")
print("Accuracy:", accuracy)

# 7. Visualize the Decision Tree
plt.figure(figsize=(15, 10))

plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True
)

plt.title("Decision Tree Classifier - Iris Dataset")
plt.show()