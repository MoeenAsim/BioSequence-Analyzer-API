from fastapi import APIRouter
from models import DNASequence
from analyzer import analyze_dna
from database.crud import get_analysis, get_all_analysis, delete_analysis
from fastapi import HTTPException

from routers import analysis

router = APIRouter()


@router.post("/analyze")
def analyze_sequence(dna: DNASequence):

    return analyze_dna(
        dna.sequence,
        dna.reference
    )


@router.get("/analysis/{analysis_id}")
def get_analysis_by_id(analysis_id: str):

    analysis = get_analysis(analysis_id)
    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="Analysis not found"
            )
    return analysis


@router.get("/analysis")
def get_all():

    analyses = get_all_analysis()

    return {
        "total": len(analyses),
        "analyses": analyses
    }


@router.delete("/analysis/{analysis_id}")
def delete_analysis_by_id(analysis_id: str):

    deleted = delete_analysis(analysis_id)

    if deleted == 0:
        return {
            "message": "Analysis not found"
        }

    return {
        "message": "Analysis deleted successfully"
    }