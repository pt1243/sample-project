from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:  # pragma: no cover
    from _typeshed import StrPath


__all__ = ["simple_read"]


def simple_read(filename: StrPath) -> str:
    """Opens a file and returns the contents.

    Parameters
    ----------
    filename : file-like
        The file-like object to open.

    Returns
    -------
    str
        The contents of the file.
    """
    with open(filename, "r") as f:
        return f.read().strip()
