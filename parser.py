def parse_fasta(text):

    lines = text.splitlines()

    records = []

    current_name = ""

    current_sequence = ""

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith(">"):

            if current_name != "":

                records.append({
                    "name": current_name,
                    "sequence": current_sequence
                })

            current_name = line[1:]

            current_sequence = ""

        else:

            current_sequence += line.upper()

    if current_name != "":

        records.append({
            "name": current_name,
            "sequence": current_sequence
        })

    return records