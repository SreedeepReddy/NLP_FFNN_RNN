"""
import subprocess

# Define a list of hidden parameters and epochs to test
hidden_parameters = [32, 64, 128]
epochs = [5, 10, 15]

# Loop through combinations of hidden parameters and epochs
for hidden_dim in hidden_parameters:
    for num_epochs in epochs:
        # Construct the command to run ffnn.py with the chosen hyperparameters
        command = [
            "python",
            "ffnn.py",
            "--hidden_dim", str(hidden_dim),
            "--epochs", str(num_epochs),
            "--train_data", "training.json",  # Update with the actual path
            "--val_data", "validation.json",  # Update with the actual path
        ]

        # Execute the ffnn.py script with the current hyperparameters
        subprocess.run(command)

print("All combinations tested.")
"""

import json

# Load your training data from the training.json file
with open('training.json', 'r') as f:
    training_data = json.load(f)

# Load your validation data from the validation.json file
with open('validation.json', 'r') as f:
    validation_data = json.load(f)

# Load your test data from the test.json file
with open('test.json', 'r') as f:
    test_data = json.load(f)

# Calculate the number of examples in each set
num_training_examples = len(training_data)
num_validation_examples = len(validation_data)
num_test_examples = len(test_data)

print(f"Number of training examples: {num_training_examples}")
print(f"Number of validation examples: {num_validation_examples}")
print(f"Number of test examples: {num_test_examples}")

