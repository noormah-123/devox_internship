# Week 5 - DBSCAN vs K-Means
# Iris Dataset

from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------
# 1. Load the same Iris dataset
# -------------------------------------------------

iris = load_iris()

# Same features used in the K-Means task
X = iris.data[:, [2, 3]]

print("Dataset shape:", X.shape)


# -------------------------------------------------
# 2. K-Means from scratch
# -------------------------------------------------

def kmeans(X, k, max_iterations=100):

    np.random.seed(42)

    random_indices = np.random.choice(
        len(X),
        k,
        replace=False
    )

    centroids = X[random_indices]

    for iteration in range(max_iterations):

        # Calculate distances
        distances = np.sqrt(
            ((X[:, np.newaxis] - centroids) ** 2).sum(axis=2)
        )

        # Assign each point to nearest centroid
        labels = np.argmin(distances, axis=1)

        # Calculate new centroids
        new_centroids = np.array([
            X[labels == cluster].mean(axis=0)
            if np.any(labels == cluster)
            else centroids[cluster]
            for cluster in range(k)
        ])

        # Stop if centroids do not change
        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    return labels, centroids


# -------------------------------------------------
# 3. Run K-Means
# -------------------------------------------------

k = 3

kmeans_labels, kmeans_centroids = kmeans(X, k)


# -------------------------------------------------
# 4. Apply DBSCAN
# -------------------------------------------------

dbscan = DBSCAN(
    eps=0.4,
    min_samples=5
)

dbscan_labels = dbscan.fit_predict(X)


# -------------------------------------------------
# 5. Display DBSCAN Results
# -------------------------------------------------

unique_labels = set(dbscan_labels)

print("\nDBSCAN Results")
print("--------------")

for label in sorted(unique_labels):

    if label == -1:
        print(
            "Noise points:",
            np.sum(dbscan_labels == -1)
        )
    else:
        print(
            f"Cluster {label + 1}:",
            np.sum(dbscan_labels == label),
            "points"
        )


# -------------------------------------------------
# 6. Compare Number of Clusters
# -------------------------------------------------

kmeans_clusters = len(set(kmeans_labels))

dbscan_clusters = len(
    set(dbscan_labels) - {-1}
)

print("\nCluster Comparison")
print("------------------")

print("K-Means clusters :", kmeans_clusters)
print("DBSCAN clusters  :", dbscan_clusters)


# -------------------------------------------------
# 7. Silhouette Scores
# -------------------------------------------------

kmeans_score = silhouette_score(
    X,
    kmeans_labels
)

print("\nSilhouette Score")
print("----------------")

print(
    f"K-Means : {kmeans_score:.3f}"
)


# Calculate DBSCAN silhouette only if
# there are at least 2 clusters
dbscan_cluster_labels = dbscan_labels[
    dbscan_labels != -1
]

dbscan_data = X[
    dbscan_labels != -1
]

if (
    len(set(dbscan_cluster_labels)) >= 2
    and len(dbscan_data) > 1
):

    dbscan_score = silhouette_score(
        dbscan_data,
        dbscan_cluster_labels
    )

    print(
        f"DBSCAN  : {dbscan_score:.3f}"
    )

else:

    print(
        "DBSCAN  : Cannot calculate "
        "silhouette score"
    )


# -------------------------------------------------
# 8. Visualize K-Means
# -------------------------------------------------

plt.figure(figsize=(10, 6))

for cluster in range(k):

    cluster_points = X[
        kmeans_labels == cluster
    ]

    plt.scatter(
        cluster_points[:, 0],
        cluster_points[:, 1],
        label=f"Cluster {cluster + 1}"
    )


plt.scatter(
    kmeans_centroids[:, 0],
    kmeans_centroids[:, 1],
    marker="X",
    s=200,
    label="Centroids"
)

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("K-Means Clustering")
plt.legend()
plt.grid(True)

plt.savefig(
    "kmeans_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -------------------------------------------------
# 9. Visualize DBSCAN
# -------------------------------------------------

plt.figure(figsize=(10, 6))

for label in sorted(unique_labels):

    if label == -1:

        # Noise points
        noise_points = X[
            dbscan_labels == -1
        ]

        plt.scatter(
            noise_points[:, 0],
            noise_points[:, 1],
            marker="x",
            s=80,
            label="Noise"
        )

    else:

        cluster_points = X[
            dbscan_labels == label
        ]

        plt.scatter(
            cluster_points[:, 0],
            cluster_points[:, 1],
            label=f"Cluster {label + 1}"
        )


plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("DBSCAN Clustering")
plt.legend()
plt.grid(True)

plt.savefig(
    "dbscan_clusters.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()