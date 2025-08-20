#!/usr/bin/env python3
"""Reproduce paper calculations from data/validation_set.csv

Usage:
    python scripts/reproduce_paper.py [--fail-on-mismatch]
"""
import csv
import argparse
from pathlib import Path
from src.sigma.core import calculate_sigma_bonds

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'validation_set.csv'
OUT = ROOT / 'sigma_bond_reproduction_results.csv'

parser = argparse.ArgumentParser()
parser.add_argument('--fail-on-mismatch', action='store_true', help='Return non-zero exit code if any mismatch is found')
args = parser.parse_args()

rows = []
with DATA.open() as f:
    reader = csv.DictReader(f)
    for r in reader:
        T = int(r['T'])
        R = int(r['R'])
        topology = r.get('topology', '')
        predicted = calculate_sigma_bonds(T, R, topology=topology)
        actual = int(r['actual_sigma'])
        ok = predicted == actual
        rows.append({
            'name': r['name'], 'T': T, 'R': R, 'topology': topology, 'actual': actual, 'predicted': predicted, 'ok': ok
        })

# write results
with OUT.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name','T','R','topology','actual','predicted','ok'])
    writer.writeheader()
    writer.writerows(rows)

total = len(rows)
matched = sum(1 for r in rows if r['ok'])
print(f'Reproduction complete: {matched}/{total} matched. Results: {OUT}')

if args.fail_on_mismatch and matched != total:
    print('Mismatch found and --fail-on-mismatch specified; exiting with code 2')
    raise SystemExit(2)
