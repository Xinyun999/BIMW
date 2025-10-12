
import torch
import numpy as np
import torch.nn.functional as F
from sklearn.linear_model import Ridge
from scipy.stats import chisquare
from typing import Tuple

# Ownership verification via chi-square
# ----------------------------
def ownership_chi2_test(extracted_bits: np.ndarray, owner_bits: np.ndarray, alpha: float = 0.01) -> Tuple[bool, float, float]:
    """
    Compare extracted bits to owner's watermark bits.
    Performs chi-square goodness-of-fit on [matches, mismatches] vs expected [L/2, L/2].
    Returns (is_owner, pvalue, chi2_stat).
    Decision rule: reject null (random bits) if pvalue < alpha -> ownership accepted.
    """
    assert extracted_bits.shape == owner_bits.shape
    L = extracted_bits.shape[0]
    matches = int(np.sum(extracted_bits == owner_bits))
    mismatches = L - matches
    observed = np.array([matches, mismatches], dtype=np.float64)
    expected = np.array([L / 2.0, L / 2.0], dtype=np.float64)
    chi2_stat, p_value = chisquare(f_obs=observed, f_exp=expected)
    is_owner = p_value < alpha
    return is_owner, float(p_value), float(chi2_stat)
















