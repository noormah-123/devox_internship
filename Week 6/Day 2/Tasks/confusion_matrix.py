from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Actual labels
y_actual = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Model predictions
y_predicted = [0, 0, 1, 0, 1, 1, 0, 1, 1, 1]

# Calculate confusion matrix
cm = confusion_matrix(y_actual, y_predicted)

print("Confusion Matrix:")
print(cm)

# Display the confusion matrix
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Not Spam", "Spam"]
)

display.plot()
plt.title("Confusion Matrix")
plt.show()