# Sigma-Bond Validator

[![Tests](https://github.com/NeuArv/sigma-bond-validator/actions/workflows/python-app.yml/badge.svg)](https://github.com/NeuArv/sigma-bond-validator/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.21203%2Frs-7340867%2Fv1-blue.svg)](https://doi.org/10.21203/rs-7340867/v1)

**Topologically-Adaptive Sigma Bond Counter**

**Author:** Arvind Gyandatt Mishra  
**Contact / LinkedIn:** https://www.linkedin.com/in/arvind-gyandatt-mishra-a6760a16b/  
**Preprint / DOI:** Mishra, A. G. (2024). *Sigma Bond Calculation via Euler's Formula for Planar and Polyhedral Molecular Graphs*. DOI: `10.21203/rs.3.rs-7340867/v1`

A compact research implementation and reproducible validation harness for a topological sigma-bond counting rule:

> σ = T + R − φ

Where:
- **σ** — predicted number of sigma bonds  
- **T** — total number of atoms (counting semantics — **follow the conventions described in the preprint and in the code**; see docstrings in `src/sigma/core.py`)  
- **R** — number of rings (topological faces)  
- **φ** — topology parameter (φ = 2 for closed/polyhedral / genus-0 structures; φ = 1 otherwise)

---

## Contents
- `main.py` — quick-run script and validation harness (produces `sigma_bond_validation_results.csv`).  
- `src/sigma/core.py` — core implementation and counting-convention documentation.  
- `scripts/reproduce_paper.py` — reproduce calculations from `data/validation_set.csv`.  
- `data/validation_set.csv` — validation scaffold (place your full 50-molecule table here).  
- `requirements.txt` — minimal runtime dependencies.  
- `LICENSE` — MIT.  
- `CITATION.bib`, `CITATION.cff` — citation metadata.  
- `.github/workflows/python-app.yml` — CI skeleton (runs tests + reproduction).

---

## Quick start

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate
pip install -r requirements.txt
```

2. Run the quick validation:

```bash
python main.py
```

Outputs:
- `sigma_bond_validation_results.csv` — per-molecule predictions and simple pass/fail.

3. Reproduce the paper table (scaffold):

```bash
python scripts/reproduce_paper.py
# to fail CI on mismatches:
python scripts/reproduce_paper.py --fail-on-mismatch
```

This reads `data/validation_set.csv` and writes `sigma_bond_reproduction_results.csv`.

---

## Notes & reproducibility

- **Counting conventions:** Follow the counting semantics described in the preprint (Mishra) and in the code. Do **not** substitute different counting rules without documenting them and re-evaluating results. See `src/sigma/core.py` docstrings for code-level guidance and `data/README.md` (create if needed) for dataset-specific notes.  
- **Validation data:** The repository currently contains a scaffold `data/validation_set.csv`. Please add the canonical 50-molecule validation table (with provenance and ring-counting method) into `data/` for reproducible runs.  
- **CI note:** If you use GitHub Actions, ensure matrix python versions are quoted (e.g. `'3.10'`) to avoid YAML float-parsing issues. The provided workflow skeleton includes a `PYTHONPATH` export so `src/` is importable during test runs.

---

## License & citation

- Repository license: **MIT** (see `LICENSE`).
- Primary theoretical source:  
  Mishra, A. G. (2024). *Sigma Bond Calculation via Euler's Formula for Planar and Polyhedral Molecular Graphs*. DOI: `10.21203/rs.3.rs-7340867/v1`.

Machine-readable citations are available in `CITATION.bib` and `CITATION.cff`.

---

## Maintainer
**Arvind Gyandatt Mishra**

---

_Last updated: 2025-08-20_
