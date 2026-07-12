import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load dataset
data = pd.read_csv("dataset.csv")


# DNA sequence ko features me convert karna
def extract_features(sequence):
    sequence = sequence.upper()

    features = [
        len(sequence),
        sequence.count("A"),
        sequence.count("T"),
        sequence.count("G"),
        sequence.count("C"),
        (sequence.count("G") + sequence.count("C")) / len(sequence)
    ]

    # 2-mer features
    kmers = [
        "AA","AT","AG","AC",
        "TA","TT","TG","TC",
        "GA","GT","GG","GC",
        "CA","CT","CG","CC"
    ]

    for kmer in kmers:
        count = 0

        for i in range(len(sequence)-1):
            if sequence[i:i+2] == kmer:
                count += 1

        features.append(count)

    return features

# Features aur labels
X = np.array([extract_features(seq) for seq in data["sequence"]])
y = data["label"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


# Model
model = RandomForestClassifier(random_state=42)

# Training
model.fit(X_train, y_train)


# Testing
prediction = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("Model Accuracy:", accuracy)


# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, prediction))


# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, prediction))


# Model save
joblib.dump(model, "model.pkl")

print("Model saved successfully!")