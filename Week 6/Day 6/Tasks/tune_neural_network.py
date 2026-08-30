import torch
import torch.nn as nn
import torch.optim as optim


# -----------------------------
# 1. Create XOR dataset
# -----------------------------

X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

y = torch.tensor([
    [0.0],
    [1.0],
    [1.0],
    [0.0]
])


# -----------------------------
# 2. Define the neural network
# -----------------------------

class FeedForwardNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(2, 4),
            nn.ReLU(),
            nn.Linear(4, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.network(x)


# -----------------------------
# 3. Function to train model
# -----------------------------

def train_model(learning_rate, epochs):

    # Create a new model for every experiment
    model = FeedForwardNN()

    # Loss function
    criterion = nn.BCELoss()

    # Optimizer
    optimizer = optim.Adam(
        model.parameters(),
        lr=learning_rate
    )

    # Training
    for epoch in range(epochs):

        predictions = model(X)

        loss = criterion(predictions, y)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

    # -----------------------------
    # Calculate accuracy
    # -----------------------------

    with torch.no_grad():

        predictions = model(X)

        predicted_classes = (
            predictions >= 0.5
        ).float()

        correct = (
            predicted_classes == y
        ).sum().item()

        accuracy = (
            correct / len(y)
        ) * 100

    return accuracy, loss.item()


# -----------------------------
# 4. Test different settings
# -----------------------------

experiments = [
    (0.001, 100),
    (0.001, 1000),
    (0.01, 100),
    (0.01, 1000),
    (0.1, 100),
    (0.1, 1000)
]


print("Learning Rate and Epoch Tuning")
print("--------------------------------")

for learning_rate, epochs in experiments:

    accuracy, loss = train_model(
        learning_rate,
        epochs
    )

    print(
        f"Learning Rate: {learning_rate:<6} "
        f"Epochs: {epochs:<5} "
        f"Accuracy: {accuracy:.2f}% "
        f"Loss: {loss:.4f}"
    )