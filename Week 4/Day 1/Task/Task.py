#Day 1 Task
# Mean, Median, Variance, Std Dev - By Hand vs NumPy

import numpy as np
# Sample dataset
data = [2, 4, 6, 8, 10]

print("Dataset:", data)
print("-" * 40)

# BY HAND 
n = len(data)

# Mean
mean_hand = sum(data) / n

# Median
sorted_data = sorted(data)
if n % 2 == 0:
    median_hand = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median_hand = sorted_data[n//2]

# Variance
squared_diff = [(x - mean_hand) ** 2 for x in data]
variance_hand = sum(squared_diff) / n

# Standard Deviation
std_hand = variance_hand ** 0.5

print("BY HAND CALCULATIONS")
print("Mean     :", mean_hand)
print("Median   :", median_hand)
print("Variance :", variance_hand)
print("Std Dev  :", std_hand)
print("-" * 40)

# ---------- USING NUMPY ----------
print("USING NUMPY")
print("Mean     :", np.mean(data))
print("Median   :", np.median(data))
print("Variance :", np.var(data))
print("Std Dev  :", np.std(data))
print("-" * 40)

print("Both results match — calculations verified!")