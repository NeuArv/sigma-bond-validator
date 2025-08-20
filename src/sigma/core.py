"""Core library for sigma-bond prediction.

Counting conventions (important):

- T: total number of atoms used by the model. In the quick examples we use
  *heavy atoms only* (e.g., carbon count for hydrocarbons). If you use explicit
  hydrogens, results must be compared against consistent ground truth.
- R: topological ring count (integer).
- topology: optional hint to infer phi. If phi is provided explicitly it will be used.
"""

from typing import Optional, Union

def infer_phi_from_topology(topology: str) -> int:
    """Infer phi from a short topology hint string."""
    if not topology:
        return 1
    t = topology.lower().strip()
    if t in ("polyhedral", "closed", "sphere", "fullerene", "polyhedron", "3d-closed"):
        return 2
    return 1

def calculate_sigma_bonds(T: Union[int, float], R: int, topology: Optional[str] = None, phi: Optional[int] = None) -> int:
    """Calculate predicted sigma bonds using sigma = T + R - phi.

    Parameters
    ----------
    T : int or float
        Total atom count (see module docstring for counting convention).
    R : int
        Number of rings (non-negative integer).
    topology : str, optional
        Short hint for topology to infer phi (values like 'polyhedral' or 'non-polyhedral').
    phi : int, optional
        If provided, phi overrides topology inference.

    Returns
    -------
    int
        Predicted sigma bonds (rounded to int).
    """
    # Basic validation
    if T is None or R is None:
        raise ValueError("T and R must be provided")
    try:
        T_val = int(T)
    except Exception as e:
        raise ValueError("T must be coercible to int") from e
    if T_val < 0 or int(R) < 0:
        raise ValueError("T and R must be non-negative")
    if phi is None:
        phi_val = infer_phi_from_topology(topology or "")
    else:
        phi_val = int(phi)
    sigma = T_val + int(R) - phi_val
    return int(sigma)
