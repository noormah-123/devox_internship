# Mini Segmentation Project
# Student Study Habits using K-Means

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# -------------------------------------------------
# 1. Create a small study-habits dataset
# -------------------------------------------------

# Columns:
# Study Hours Per Day
# Quiz Score (%)

students = np.array([
    [1, 45],
    [1.5, 50],
    [2, 55],
    [2.5, 60],
    [3, 65],

    [4, 72],
    [4.5, 75],
    [5, 78],
    [5.5, 82],
    [6, 85],

    [7, 88],
    [7.5, 90],
    [8, 92],
    [8.5, 94],
    [9, 96]
])


# -------------------------------------------------
# 2. Apply K-Means
# -------------------------------------------------

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(students)


# -------------------------------------------------
# 3. Display cluster assignments
# -------------------------------------------------

print("Student Segmentation")
print("--------------------")

for i, cluster in enumerate(clusters):

    print(
        f"Student {i + 1}: "
        f"Study Hours = {students[i, 0]}, "
        f"Quiz Score = {students[i, 1]}%, "
        f"Cluster = {cluster + 1}"
    )


# -------------------------------------------------
# 4. Calculate cluster profiles
# -------------------------------------------------

print("\nCluster Profiles")
print("----------------")

for cluster in range(3):

    cluster_students = students[
        clusters == cluster
    ]

    average_hours = np.mean(
        cluster_students[:, 0]
    )

    average_score = np.mean(
        cluster_students[:, 1]
    )

    print(
        f"\nCluster {cluster + 1}:"
    )

    print(
        f"Average study hours: "
        f"{average_hours:.2f}"
    )

    print(
        f"Average quiz score: "
        f"{average_score:.2f}%"
    )


# -------------------------------------------------
# 5. Visualize the clusters
# -------------------------------------------------

plt.figure(figsize=(10, 6))

for cluster in range(3):

    cluster_students = students[
        clusters == cluster
    ]

    plt.scatter(
        cluster_students[:, 0],
        cluster_students[:, 1],
        s=100,
        label=f"Cluster {cluster + 1}"
    )


# Plot centroids
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker="X",
    s=250,
    label="Centroids"
)

plt.xlabel("Study Hours Per Day")
plt.ylabel("Quiz Score (%)")

plt.title(
    "Student Segmentation Using K-Means"
)

plt.legend()
plt.grid(True)

plt.savefig(
    "student_segmentation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()