import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a numeric dataset
data = {
    "Age": [18, 19, 20, 21, 22, 23, 24, 25],
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [70, 75, 80, 85, 90, 92, 95, 98],
    "Marks": [55, 62, 68, 75, 82, 88, 94, 97]
}

df = pd.DataFrame(data)

# Select only numeric columns
numeric_df = df.select_dtypes(include="number")

# Calculate correlation matrix
correlation_matrix = numeric_df.corr()

# Create heatmap
plt.figure(figsize=(10, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.show()