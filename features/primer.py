def design_primers(sequence):

    sequence = sequence.upper()

    if len(sequence) < 40:
        return {
            "error": "Sequence should be at least 40 bases long."
        }

    forward = sequence[:20]

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reverse = ""

    for base in reversed(sequence[-20:]):
        reverse += complement[base]

    return {
        "forward_primer": forward,
        "reverse_primer": reverse,
        "primer_length": 20
    }