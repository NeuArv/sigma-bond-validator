import pytest
from src.sigma.core import calculate_sigma_bonds

def test_basic_non_polyhedral():
    assert calculate_sigma_bonds(6, 1, topology='non-polyhedral') == 6

def test_basic_polyhedral():
    assert calculate_sigma_bonds(60, 31, topology='polyhedral') == 89

def test_phi_override():
    assert calculate_sigma_bonds(10, 2, phi=2) == 10

def test_invalid_inputs():
    with pytest.raises(ValueError):
        calculate_sigma_bonds(None, 1)
    with pytest.raises(ValueError):
        calculate_sigma_bonds(-1, 0)
