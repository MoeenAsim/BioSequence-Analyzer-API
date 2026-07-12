import joblib


# Saved model load karna
model = joblib.load("model.pkl")


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

    return [features]


# New DNA sequence
sequence = "ATGCGTACGTA"


# Features banana
features = extract_features(sequence)


# Prediction
prediction = model.predict(features)


# Result
if prediction[0] == 1:
    print("Prediction: Promoter")
else:
    print("Prediction: Non-Promoter")