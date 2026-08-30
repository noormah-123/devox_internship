# Week 5 - K-Means Clustering From Scratch
# Iris Dataset + Elbow Method

from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------
# 1. Load the Iris dataset
# -------------------------------------------------

iris = load_iris()

X = iris.data

# Use two features so we can visualize the clusters
X = X[:, [2, 3]]   # Petal length and petal width


# -------------------------------------------------
# 2. Implement K-Means from scratch
# -------------------------------------------------

def kmeans(X, k, max_iterations=100):

    # Randomly select k data points as initial centroids
    np.random.seed(42)

    random_indices = np.random.choice(
        len(X),
        k,
        replace=False
    )

    centroids = X[random_indices]

    for iteration in range(max_iterations):

        # Calculate distance from every point to every centroid
        distances = np.sqrt(
            ((X[:, np.newaxis] - centroids) ** 2).sum(axis=2)
        )

        # Assign each point to the nearest centroid
        labels = np.argmin(distances, axis=1)

        # Calculate new centroids
        new_centroids = np.array([
            X[labels == cluster].mean(axis=0)
            if np.any(labels == cluster)
            else centroids[cluster]
            for cluster in range(k)
        ])

        # Check whether centroids have stopped changing
        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    return labels, centroids


# -------------------------------------------------
# 3. Calculate Within-Cluster Sum of Squares (WCSS)
# -------------------------------------------------

def calculate_wcss(X, labels, centroids):

    wcss = 0

    for cluster in range(len(centroids)):

        cluster_points = X[labels == cluster]

        if len(cluster_points) > 0:

            distances = np.sum(
                (cluster_points - centroids[cluster]) ** 2
            )

            wcss += distances

    return wcss


# -------------------------------------------------
# 4. Elbow Method
# -------------------------------------------------

wcss_values = []

k_values = range(1, 11)

for k in k_values:

    labels, centroids = kmeans(X, k)

    wcss = calculate_wcss(
        X,
        labels,
        centroids
    )

    wcss_values.append(wcss)


# -------------------------------------------------
# 5. Plot the Elbow Curve
# -------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    k_values,
    wcss_values,
    marker="o"
)

plt.xlabel("Number of Clusters (k)")
plt.ylabel("WCSS")
plt.title("Elbow Method for Choosing k")

plt.xticks(k_values)

plt.grid(True)

plt.savefig(
    "elbow_method.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -------------------------------------------------
# 6. Choose k
# -------------------------------------------------

# For the Iris dataset, k = 3 is a reasonable choice.
best_k = 3

labels, centroids = kmeans(
    X,
    best_k
)


# -------------------------------------------------
# 7. Visualize the Clusters
# -------------------------------------------------

plt.figure(figsize=(10, 6))

for cluster in range(best_k):

    cluster_points = X[labels == cluster]

    plt.scatter(
        cluster_points[:, 0],
        cluster_points[:, 1],
        label=f"Cluster {cluster + 1}"
    )


# Plot centroids
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="X",
    s=200,
    label="Centroids"
)

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("K-Means Clustering From Scratch (k=3)")

plt.legend()

plt.savefig(
    "kmeans_clusters.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -------------------------------------------------
# 8. Print Results
# -------------------------------------------------

print("K-Means Clustering From Scratch")
print("--------------------------------")

print("Selected k:", best_k)

print("\nCentroids:")

for i, centroid in enumerate(centroids):

    print(
        f"Cluster {i + 1}: "
        f"Petal Length = {centroid[0]:.2f}, "
        f"Petal Width = {centroid[1]:.2f}"
    )

print("\nWCSS values:")

for k, wcss in zip(k_values, wcss_values):

    print(f"k = {k}: {wcss:.2f}")