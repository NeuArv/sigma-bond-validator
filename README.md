# Sigma-Bond Validator

**Topologically-Adaptive Sigma Bond Counter**

A compact research implementation and validation harness for a topological sigma-bond counting rule:

> σ = T + R − φ

Where:
- σ: predicted number of sigma bonds
- T: total number of atoms (counting semantics documented in code)
- R: number of rings
- φ: topology parameter (φ = 2 for closed/polyhedral structures; φ = 1 otherwise)

## Contents
- `main.py` — quick-run script and validation harness (produces `sigma_bond_validation_results.csv`).
- `requirements.txt` — minimal runtime dependencies.
- `LICENSE` — license for the project (MIT recommended).

## Quick start
1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Activate the venv:
# macOS / Linux: source .venv/bin/activate
# Windows: run the Activate script located in .venv/Scripts from PowerShell or cmd
pip install -r requirements.txt
```

2. Run the validation:

```bash
python main.py
```

Outputs:
- `sigma_bond_validation_results.csv` — per-molecule predictions and results.

## Notes
- Counting semantics (explicit vs implicit hydrogens) are implementation-sensitive; see docstrings in `src/sigma/core.py`.
- For reproducible experiments move datasets to `data/` and load from CSVs.

## License & Citation
- Recommended license: MIT.
- Include a CITATION or BibTeX entry if this code is used in publications.
