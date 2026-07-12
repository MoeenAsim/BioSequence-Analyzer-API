def calculate_molecular_weight(sequence):

    sequence = sequence.upper()

    weights = {
        "A": 313.21,
        "T": 304.2,
        "G": 329.21,
        "C": 289.18
    }

    molecular_weight = 0

    for base in sequence:
        molecular_weight += weights[base]

    return round(molecular_weight, 2)



def calculate_tm(sequence):

    sequence = sequence.upper()

    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    tm = (2 * (a_count + t_count)) + (4 * (g_count + c_count))

    return tm