import numpy as np


__all__ = ["sum_array"]


def sum_array(a: np.ndarray) -> float:
    """Sum an array.

    Parameters
    ----------
    a : array-like
        The array to sum.

    Returns
    -------
    float
        The sum of the array.
    """
    return np.sum(a)
