from pydantic import BaseModel
from typing import List


class DNASequence(BaseModel):
    sequence: str
    reference: str | None = None


class Mutation(BaseModel):
    position: int
    reference_base: str
    sample_base: str
    mutation_type: str


class AnalysisResult(BaseModel):
    length: int
    gc_content: float
    at_content: float
    base_count: dict
    reverse_complement: str
    mutations: List[Mutation]