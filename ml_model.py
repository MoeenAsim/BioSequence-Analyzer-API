import joblib


# Trained model load karna
model = joblib.load("ml/model.pkl")


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

    return [features]


def predict_sequence(sequence):

    features = extract_features(sequence)

    prediction = model.predict(features)

    probability = model.predict_proba(features)

    confidence = max(probability[0]) * 100

    if prediction[0] == 1:
        result = "Promoter"
    else:
        result = "Non-Promoter"

    return {
        "prediction": result,
        "confidence": round(confidence, 2)
    }