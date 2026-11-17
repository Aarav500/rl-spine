import numpy as np
import pytest
from values import exact_value, neumann_value

P = np.array([[0.5, 0.5], [0.2, 0.8]])
r = np.array([1.0, 0.0])
gamma = 0.9


def test_k3_matches_hand_sum():
    assert neumann_value(P, r, gamma, 3) == pytest.approx([1.7335, 0.3906])


def test_k200_matches_solve():
    assert neumann_value(P, r, gamma, 200) == pytest.approx(exact_value(P, r, gamma))