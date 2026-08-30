import math
from collections import Counter

# 1. Small 2D Training Dataset
# Each point is: (x, y, class)
dataset = [
    (1, 2, "A"),
    (2, 3, "A"),
    (2, 1, "A"),
    (3, 2, "A"),

    (7, 8, "B"),
    (8, 7, "B"),
    (9, 8, "B"),
    (8, 9, "B")
]

# 2. Euclidean Distance
def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# 3. KNN Prediction
def knn_predict(dataset, new_point, k):
    
    distances = []

    # Calculate distance from new point
    # to every training point
    for x, y, label in dataset:
        distance = euclidean_distance(
            new_point,
            (x, y)
        )

        distances.append((distance, label))

    # Sort by distance
    distances.sort(key=lambda item: item[0])

    # Select K nearest neighbors
    nearest_neighbors = distances[:k]

    # Get their labels
    labels = [label for distance, label in nearest_neighbors]

    # Majority voting
    votes = Counter(labels)

    prediction = votes.most_common(1)[0][0]

    return prediction, nearest_neighbors

# 4. Test the KNN Classifier
new_point = (3, 3)
k = 3

prediction, neighbors = knn_predict(
    dataset,
    new_point,
    k
)

# 5. Display Results
print("New Point:", new_point)
print("K:", k)

print("\nNearest Neighbors:")

for distance, label in neighbors:
    print(
        f"Class: {label}, "
        f"Distance: {distance:.2f}"
    )

print("\nPredicted Class:", prediction)