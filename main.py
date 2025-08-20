"""Quick-run script for sigma-bond validation.

This script uses src/sigma/core.py for the calculation and runs a small
validation harness, writing results to CSV.
"""
from src.sigma.core import calculate_sigma_bonds
import csv
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "sigma_bond_validation_results.csv"

# Small, human-curated example set. T = total atoms (convention used here: heavy atoms only),
# R = ring count, topology = 'polyhedral' or 'non-polyhedral' as a hint for phi inference.
EXAMPLES = [
    {"name": "Benzene (C6)", "T": 6, "R": 1, "topology": "non-polyhedral", "actual": 6 + 1 - 1},
    {"name": "Cyclohexane (C6)", "T": 6, "R": 1, "topology": "non-polyhedral", "actual": 6 + 1 - 1},
    {"name": "Fullerene-C60 (C60)", "T": 60, "R": 31, "topology": "polyhedral", "actual": 60 + 31 - 2},
    {"name": "Cube-like cluster", "T": 8, "R": 6, "topology": "polyhedral", "actual": 8 + 6 - 2},
    {"name": "Linear chain (5 atoms)", "T": 5, "R": 0, "topology": "non-polyhedral", "actual": 5 + 0 - 1},
]

def run_validation():
    rows = []
    for ex in EXAMPLES:
        predicted = calculate_sigma_bonds(ex["T"], ex["R"], topology=ex["topology"])
        result = "OK" if predicted == ex.get("actual") else "MISMATCH"
        rows.append({"Molecule": ex["name"], "T": ex["T"], "R": ex["R"], "Topology": ex["topology"], "Actual": ex.get("actual"), "Predicted": predicted, "Result": result})

    # write CSV
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    # simple summary
    ok = sum(1 for r in rows if r["Result"] == "OK")
    print(f"Validation complete — {ok}/{len(rows)} matched. Output: {OUT}")


if __name__ == "__main__":
    run_validation()
