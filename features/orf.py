def find_orf(sequence):

    sequence = sequence.upper()

    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    orfs = []

    start_position = sequence.find(start_codon)

    while start_position != -1:

        for i in range(start_position + 3, len(sequence), 3):

            codon = sequence[i:i+3]

            if codon in stop_codons:

                orfs.append({
                    "start_position": start_position + 1,
                    "stop_position": i + 3,
                    "sequence": sequence[start_position:i+3],
                    "length": i + 3 - start_position
                })

                break

        start_position = sequence.find(start_codon, start_position + 1)

    return orfs