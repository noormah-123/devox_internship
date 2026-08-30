import tensorflow as tf
import matplotlib.pyplot as plt

# Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

print("Original Training Data Shape:", x_train.shape)
print("Original Test Data Shape:", x_test.shape)

# Use a small subset
x_train = x_train[:1000]
y_train = y_train[:1000]

x_test = x_test[:200]
y_test = y_test[:200]

# Normalize pixel values from 0-255 to 0-1
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Convert labels to 1D
y_train = y_train.flatten()
y_test = y_test.flatten()

print("\nAfter Preprocessing:")
print("Training Images Shape:", x_train.shape)
print("Training Labels Shape:", y_train.shape)
print("Test Images Shape:", x_test.shape)
print("Test Labels Shape:", y_test.shape)

print("\nPixel Value Range:")
print("Minimum:", x_train.min())
print("Maximum:", x_train.max())

# CIFAR-10 class names
class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]

# Display 10 sample images
plt.figure(figsize=(12, 6))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i])
    plt.title(class_names[y_train[i]])
    plt.axis("off")

plt.tight_layout()
plt.show()