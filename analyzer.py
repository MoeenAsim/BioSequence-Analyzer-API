from fastapi import HTTPException
from features.orf import find_orf
from features.enzymes import find_restriction_sites
from features.properties import calculate_molecular_weight
from features.properties import calculate_tm
from features.alignment import needleman_wunsch
from features.primer import design_primers
from constants.dna import VALID_BASES, COMPLEMENT
from constants.codon_table import CODON_TABLE
from visualization.charts import (
    create_gc_chart,
    create_nucleotide_chart
)
from database.crud import save_analysis
def analyze_dna(sequence: str, reference: str = None):

    sequence = sequence.upper()
    if len(sequence) == 0:
        raise HTTPException(
            status_code=400,
            detail="Sequence cannot be empty."
        )

    # Validate DNA sequence
    for base in sequence:
        if base not in VALID_BASES:
            raise HTTPException(
                status_code=400,
                detail="Invalid DNA sequence. Only A, T, G, and C are allowed."
            )

    # Calculate sequence length
    length = len(sequence)
  
    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    # Calculate GC Content
    gc_content = ((g_count + c_count) / length) * 100
    at_content = ((a_count + t_count) / length) * 100
    gc_chart = create_gc_chart(
        gc_content,
        at_content
        )
    nucleotide_chart = create_nucleotide_chart(
        a_count,
        t_count,
        g_count,
        c_count
    )
    # DNA to RNA Transcription
    rna_sequence = sequence.replace("T", "U")
    # Complete RNA Codon Table
    protein = ""
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3] 
        if len(codon) != 3:
            break
        amino_acid = CODON_TABLE.get(codon, "X")
        if amino_acid == "*":
            break
        protein += amino_acid
    # GC Category
    if gc_content < 40:
      gc_category = "Low GC"

    elif gc_content <= 60: 
      gc_category = "Moderate GC"

    else:
      gc_category = "High GC"
       # Mutation Detection
      
    # Mutation Detection

    # Mutation Detection

    mutations = []

    if reference:
        reference = reference.upper()

        i = 0
        j = 0

        while i < len(reference) and j < len(sequence):

            if reference[i] == sequence[j]:
                i += 1
                j += 1

            else:
                mutations.append({
                    "position": i + 1,
                    "reference_base": reference[i],
                    "sample_base": sequence[j],
                    "mutation_type": "Substitution"
                })

                i += 1
                j += 1


        # Insertion detection
        while j < len(sequence):

            mutations.append({
                "position": i + 1,
                "reference_base": "-",
                "sample_base": sequence[j],
                "mutation_type": "Insertion"
            })

            j += 1


        # Deletion detection
        while i < len(reference):

            mutations.append({
                "position": i + 1,
                "reference_base": reference[i],
                "sample_base": "-",
                "mutation_type": "Deletion"
            })

            i += 1

    # ORF Detection
    orf_analysis = find_orf(sequence)

# Restriction Enzyme Analysis
    restriction_analysis = find_restriction_sites(sequence)
    # properties
    molecular_weight = calculate_molecular_weight(sequence)
    tm = calculate_tm(sequence)
    # Sequence Alignment
    # Primer Design
    primer_analysis = design_primers(sequence)

    alignment_analysis = None
    if reference:
        alignment_analysis = needleman_wunsch(
            reference,
            sequence
            )

    reverse_complement = ""

    for base in reversed(sequence):
     reverse_complement += COMPLEMENT[base]
    # Mutation Summary

    mutation_summary = {
        "total_mutations": len(mutations),
        "substitutions": 0,
        "insertions": 0,
        "deletions": 0
    }

    for mutation in mutations:

        if mutation["mutation_type"] == "Substitution":
            mutation_summary["substitutions"] += 1

        elif mutation["mutation_type"] == "Insertion":
            mutation_summary["insertions"] += 1

        elif mutation["mutation_type"] == "Deletion":
            mutation_summary["deletions"] += 1

    # Return JSON response
    result = {
    "sequence_analysis": {
        "sequence": sequence,
        "length": length,
        "reverse_complement": reverse_complement
    },

    "composition": {
        "A_count": a_count,
        "T_count": t_count,
        "G_count": g_count,
        "C_count": c_count,
        "GC_content": round(gc_content, 2),
        "AT_content": round(at_content, 2),
        "GC_category": gc_category
    },

    "translation": {
        "rna_sequence": rna_sequence,
        "protein": protein
    },

    "mutation_analysis": {
        "mutations": mutations,
        "mutation_summary": mutation_summary
    },
    "orf_analysis": {
    "orfs": orf_analysis
},
"restriction_analysis": {
    "sites": restriction_analysis
},
"sequence_properties": {
    "molecular_weight": molecular_weight,
    "melting_temperature": tm
},
"alignment_analysis": alignment_analysis,

"primer_analysis": primer_analysis,

"visualization": {
    "gc_chart": "http://127.0.0.1:8000/charts/gc_content.png",
    "nucleotide_chart": "http://127.0.0.1:8000/charts/nucleotide_composition.png"
}
}
    analysis_id = save_analysis(result)
    result["analysis_id"] = analysis_id
    return result