import torch
import torch.nn as nn
import torch.optim as optim


# -----------------------------
# 1. Create the XOR dataset
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
# 2. Create the neural network
# -----------------------------

class FeedForwardNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(2, 4),     # Input layer → Hidden layer
            nn.ReLU(),           # Activation function
            nn.Linear(4, 1),     # Hidden layer → Output layer
            nn.Sigmoid()         # Output between 0 and 1
        )

    def forward(self, x):
        return self.network(x)


# Create model
model = FeedForwardNN()


# -----------------------------
# 3. Define loss function
# -----------------------------

criterion = nn.BCELoss()


# -----------------------------
# 4. Define optimizer
# -----------------------------

optimizer = optim.Adam(
    model.parameters(),
    lr=0.01
)


# -----------------------------
# 5. Train the neural network
# -----------------------------

epochs = 5000

for epoch in range(epochs):

    # Forward pass
    predictions = model(X)

    # Calculate loss
    loss = criterion(predictions, y)

    # Clear previous gradients
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Update weights
    optimizer.step()

    # Display progress
    if (epoch + 1) % 500 == 0:
        print(
            f"Epoch [{epoch + 1}/{epochs}], "
            f"Loss: {loss.item():.4f}"
        )


# -----------------------------
# 6. Test the model
# -----------------------------

print("\nFinal Predictions:")
print("------------------")

with torch.no_grad():

    predictions = model(X)

    for i in range(len(X)):

        probability = predictions[i].item()

        predicted_class = 1 if probability >= 0.5 else 0

        print(
            f"Input: {X[i].tolist()} "
            f"-> Probability: {probability:.4f} "
            f"-> Prediction: {predicted_class} "
            f"-> Actual: {int(y[i].item())}"
        )