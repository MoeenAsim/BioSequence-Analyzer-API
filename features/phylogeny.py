def calculate_distance(seq1, seq2):

    seq1 = seq1.upper()
    seq2 = seq2.upper()

    length = min(len(seq1), len(seq2))

    differences = 0

    for i in range(length):

        if seq1[i] != seq2[i]:
            differences += 1

    distance = differences / length

    return round(distance, 3)



def create_distance_matrix(records):

    matrix = {}

    for record1 in records:

        name1 = record1["name"]

        matrix[name1] = {}

        for record2 in records:

            name2 = record2["name"]

            if name1 == name2:
                matrix[name1][name2] = 0

            else:
                matrix[name1][name2] = calculate_distance(
                    record1["sequence"],
                    record2["sequence"]
                )

    return matrix



def create_newick(records):

    names = []

    for record in records:
        names.append(record["name"])

    tree = "(" + ",".join(names) + ");"

    return tree