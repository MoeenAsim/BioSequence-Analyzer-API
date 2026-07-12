# BioSequence Analyzer API

A powerful FastAPI-based Bioinformatics API for DNA sequence analysis. The project provides nucleotide composition analysis, GC/AT content calculation, DNA-to-RNA transcription, protein translation, mutation detection, ORF detection, restriction enzyme analysis, primer design, sequence alignment, phylogenetic analysis, and automated report generation.

The API supports both single-sequence analysis and batch processing through FASTA file uploads, making it useful for bioinformatics research, education, and software development.

## Features

- DNA sequence validation
- Nucleotide composition analysis
- GC & AT content calculation
- DNA → RNA transcription
- Protein translation
- Reverse complement generation
- Mutation detection
- Mutation summary
- ORF (Open Reading Frame) detection
- Restriction enzyme site analysis
- Molecular weight calculation
- Melting temperature (Tm)
- Needleman–Wunsch sequence alignment
- Primer design
- FASTA file upload & batch analysis
- Multiple sequence comparison
- Phylogenetic distance matrix
- Newick tree generation
- JSON report generation
- PDF report generation
- Interactive Swagger API documentation

## Project Structure

```text
BioSequence-Analyzer-API/
│
├── constants/
│   ├── __init__.py
│   ├── codon_table.py
│   └── dna.py
│
├── features/
│   ├── alignment.py
│   ├── enzymes.py
│   ├── multiple_alignment.py
│   ├── orf.py
│   ├── phylogeny.py
│   ├── primer.py
│   └── properties.py
│
├── reports/
│   ├── report_generator.py
│   └── pdf_report.py
│
├── sample_data/
│   └── sample.fasta
│
├── analyzer.py
├── main.py
├── models.py
├── parser.py
├── requirements.txt
├── README.md
└── LICENSE
```
## Technologies Used

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn
- Biopython
- ReportLab
- NumPy
- Matplotlib (for future visualization)

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/BioSequence-Analyzer-API.git
```

Move into the project directory:

```bash
cd BioSequence-Analyzer-API
```

Install dependencies:

```bash
pip install -r requirements.txt
```
## Running the API

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will start at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API welcome message |
| POST | `/analyze` | Analyze a DNA sequence |
| POST | `/upload-fasta` | Upload and analyze FASTA file |
| POST | `/generate-report` | Generate analysis report |

## Example Request

```json
{
  "sequence": "ATGCGTGAATTCGCGTAA",
  "reference": "ATGCGTGAATTCGCGTAA"
}
```
## Example Response

```json
{
  "sequence_analysis": {
    "sequence": "ATGCGTGAATTCGCGTAA",
    "length": 18,
    "reverse_complement": "TTACGCGAATTCACGCAT"
  },
  "composition": {
    "GC_content": 50.0,
    "AT_content": 50.0
  },
  "translation": {
    "protein": "MREFA"
  }
}
```
## Screenshots

### Swagger UI

Add a screenshot of the interactive Swagger documentation.

![Swagger UI](images/swagger.png)

---

### Example Analysis

Add a screenshot showing a successful DNA sequence analysis.

![Analysis](images/analysis.png)

---

### FASTA Upload

Add a screenshot of batch sequence analysis.

![FASTA Upload](images/fasta_upload.png)

## Future Roadmap

- 📊 DNA sequence visualization
- 📈 GC content and nucleotide composition charts
- 🗄️ Database integration (SQLite / PostgreSQL / MongoDB)
- 👤 User authentication
- 📜 Analysis history
- 🤖 Machine Learning-based mutation prediction
- 🧬 Disease classification models
- 🐳 Docker support
- ☁️ Cloud deployment
- 🌐 Public API endpoint

## Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**Muhammad Moeen Asim**

Bioinformatics Student | Python Developer | FastAPI Developer

- GitHub: https://github.com/MoeenAsim
- LinkedIn: https://www.linkedin.com/in/muhammad-moeen-asim-679209332/