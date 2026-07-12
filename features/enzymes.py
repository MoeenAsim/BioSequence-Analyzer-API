def find_restriction_sites(sequence):

    sequence = sequence.upper()

    enzymes = {
        "EcoRI": "GAATTC",
        "BamHI": "GGATCC",
        "HindIII": "AAGCTT",
        "TaqI": "TCGA"
    }

    results = []

    for enzyme, site in enzymes.items():

        position = sequence.find(site)

        if position != -1:
            results.append({
                "enzyme": enzyme,
                "site": site,
                "position": position + 1
            })

    return results