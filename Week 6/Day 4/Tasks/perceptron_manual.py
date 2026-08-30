# Manual Perceptron Implementation

# Step function
def step_function(value):
    if value >= 0:
        return 1
    else:
        return 0


# Perceptron function
def perceptron(inputs, weights, bias):
    # Calculate weighted sum
    weighted_sum = 0

    for i in range(len(inputs)):
        weighted_sum += inputs[i] * weights[i]

    # Add bias
    weighted_sum += bias

    # Apply step function
    output = step_function(weighted_sum)

    return output


# -----------------------------
# Simple AND gate example
# -----------------------------

# Weights
weights = [1, 1]

# Bias
bias = -1.5

# Test cases for AND gate
test_cases = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]


print("AND Gate Perceptron")
print("-------------------")

for inputs in test_cases:

    output = perceptron(
        inputs,
        weights,
        bias
    )

    print(
        f"Input: {inputs} -> Output: {output}"
    )