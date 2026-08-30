import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Subset

import matplotlib.pyplot as plt


# -----------------------------------
# 1. Device
# -----------------------------------

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Using device:", device)


# -----------------------------------
# 2. Transform MNIST images
# -----------------------------------

transform = transforms.ToTensor()


# -----------------------------------
# 3. Download MNIST dataset
# -----------------------------------

train_dataset = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)


# -----------------------------------
# 4. Use a small subset
# -----------------------------------

train_subset = Subset(
    train_dataset,
    range(5000)
)

test_subset = Subset(
    test_dataset,
    range(1000)
)


# -----------------------------------
# 5. Create DataLoaders
# -----------------------------------

train_loader = DataLoader(
    train_subset,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_subset,
    batch_size=64,
    shuffle=False
)


# -----------------------------------
# 6. Define neural network
# -----------------------------------

class DigitClassifier(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(

            # 28 × 28 image = 784 pixels
            nn.Flatten(),

            # Input layer → hidden layer
            nn.Linear(28 * 28, 128),

            nn.ReLU(),

            # Hidden layer → output layer
            nn.Linear(128, 10)
        )

    def forward(self, x):
        return self.network(x)


model = DigitClassifier().to(device)


# -----------------------------------
# 7. Loss and optimizer
# -----------------------------------

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)


# -----------------------------------
# 8. Train the model
# -----------------------------------

epochs = 5

print("\nTraining model...")

for epoch in range(epochs):

    model.train()

    total_loss = 0

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        # Forward pass
        outputs = model(images)

        # Calculate loss
        loss = criterion(outputs, labels)

        # Clear gradients
        optimizer.zero_grad()

        # Backpropagation
        loss.backward()

        # Update weights
        optimizer.step()

        total_loss += loss.item()

    average_loss = total_loss / len(train_loader)

    print(
        f"Epoch [{epoch + 1}/{epochs}] "
        f"Loss: {average_loss:.4f}"
    )


# -----------------------------------
# 9. Evaluate model
# -----------------------------------

model.eval()

correct = 0
total = 0

misclassified_images = []
misclassified_actual = []
misclassified_predicted = []


with torch.no_grad():

    for images, labels in test_loader:

        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        predictions = torch.argmax(
            outputs,
            dim=1
        )

        total += labels.size(0)

        correct += (
            predictions == labels
        ).sum().item()

        # Find incorrect predictions
        for i in range(len(labels)):

            if predictions[i] != labels[i]:

                if len(misclassified_images) < 5:

                    misclassified_images.append(
                        images[i].cpu()
                    )

                    misclassified_actual.append(
                        labels[i].item()
                    )

                    misclassified_predicted.append(
                        predictions[i].item()
                    )


# -----------------------------------
# 10. Calculate accuracy
# -----------------------------------

accuracy = (
    correct / total
) * 100

print("\nEvaluation Report")
print("-----------------")

print(
    f"Test Accuracy: {accuracy:.2f}%"
)

print(
    f"Correct Predictions: {correct}/{total}"
)

print(
    f"Incorrect Predictions: {total - correct}/{total}"
)


# -----------------------------------
# 11. Display misclassified examples
# -----------------------------------

print("\nMisclassified Examples")
print("----------------------")

for i in range(
    len(misclassified_images)
):

    print(
        f"Example {i + 1}: "
        f"Actual = {misclassified_actual[i]}, "
        f"Predicted = {misclassified_predicted[i]}"
    )


# -----------------------------------
# 12. Plot misclassified images
# -----------------------------------

if len(misclassified_images) > 0:

    plt.figure(figsize=(12, 3))

    for i in range(
        len(misclassified_images)
    ):

        plt.subplot(
            1,
            len(misclassified_images),
            i + 1
        )

        plt.imshow(
            misclassified_images[i].squeeze(),
            cmap="gray"
        )

        plt.title(
            f"Actual: {misclassified_actual[i]}\n"
            f"Pred: {misclassified_predicted[i]}"
        )

        plt.axis("off")

    plt.suptitle(
        "Misclassified MNIST Examples"
    )

    plt.show()