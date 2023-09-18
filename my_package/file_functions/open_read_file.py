from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:  # pragma: no cover
    from _typeshed import StrPath


for _ in range(3):
    pass


__all__ = ["simple_read"]


def simple_read(filename: StrPath) -> str:
    with open(filename) as f:
        return f.read().strip()
