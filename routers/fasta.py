from fastapi import APIRouter, UploadFile, File
from parser import parse_fasta
from analyzer import analyze_dna
from features.multiple_alignment import compare_sequences
from features.phylogeny import create_distance_matrix, create_newick


router = APIRouter()


@router.post("/upload-fasta")
async def upload_fasta(file: UploadFile = File(...)):

    content = await file.read()

    text = content.decode("utf-8")

    records = parse_fasta(text)

    results = []

    for record in records:

        analysis = analyze_dna(
            record["sequence"]
        )

        analysis["name"] = record["name"]

        results.append(analysis)


    comparison = compare_sequences(records)
    distance_matrix = create_distance_matrix(records)
    tree = create_newick(records)


    return {
        "sequence_analysis": results,

        "multiple_alignment": comparison,

        "phylogenetic_analysis": {
            "distance_matrix": distance_matrix,
            "newick_tree": tree
        }
    }