def needleman_wunsch(seq1, seq2):

    seq1 = seq1.upper()
    seq2 = seq2.upper()

    match = 1
    mismatch = -1
    gap = -2

    rows = len(seq1) + 1
    cols = len(seq2) + 1

    score = [[0 for _ in range(cols)] for _ in range(rows)]


    # Initialize matrix

    for i in range(rows):
        score[i][0] = i * gap

    for j in range(cols):
        score[0][j] = j * gap


    # Fill matrix

    for i in range(1, rows):

        for j in range(1, cols):

            diagonal = score[i-1][j-1] + (
                match if seq1[i-1] == seq2[j-1]
                else mismatch
            )

            delete = score[i-1][j] + gap

            insert = score[i][j-1] + gap

            score[i][j] = max(
                diagonal,
                delete,
                insert
            )


    # Traceback

    align1 = ""
    align2 = ""

    i = len(seq1)
    j = len(seq2)


    while i > 0 and j > 0:

        current = score[i][j]

        if current == score[i-1][j-1] + (
            match if seq1[i-1] == seq2[j-1]
            else mismatch
        ):

            align1 = seq1[i-1] + align1
            align2 = seq2[j-1] + align2

            i -= 1
            j -= 1


        elif current == score[i-1][j] + gap:

            align1 = seq1[i-1] + align1
            align2 = "-" + align2

            i -= 1


        else:

            align1 = "-" + align1
            align2 = seq2[j-1] + align2

            j -= 1


    similarity = 0

    length = len(align1)

    for a, b in zip(align1, align2):

        if a == b:
            similarity += 1


    similarity_percentage = (similarity / length) * 100


    return {
        "alignment_1": align1,
        "alignment_2": align2,
        "score": score[-1][-1],
        "similarity": round(similarity_percentage, 2)
    }