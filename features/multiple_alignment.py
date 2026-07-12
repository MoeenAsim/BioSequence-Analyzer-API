from features.alignment import needleman_wunsch


def compare_sequences(records):

    results = []

    for i in range(len(records)):

        for j in range(i + 1, len(records)):

            seq1 = records[i]
            seq2 = records[j]

            alignment = needleman_wunsch(
                seq1["sequence"],
                seq2["sequence"]
            )

            results.append({
                "sequence_1": seq1["name"],
                "sequence_2": seq2["name"],
                "similarity": alignment["similarity"]
            })

    return results