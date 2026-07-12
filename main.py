from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.analysis import router as analysis_router
from routers.fasta import router as fasta_router


app = FastAPI(
    title="BioSequence Analyzer API",
    description="A simple API for DNA sequence analysis",
    version="7.1.2"
)


# Routers
app.include_router(
    analysis_router,
    prefix="/api/v1"
)

app.include_router(
    fasta_router,
    prefix="/api/v1"
)


# Static charts
app.mount(
    "/charts",
    StaticFiles(directory="charts"),
    name="charts"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to BioSequence Analyzer API!"
    }