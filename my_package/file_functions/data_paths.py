from __future__ import annotations
import pathlib
import sys
from typing import TYPE_CHECKING, Final


__all__ = ["ROOT_DIR", "DATA_DIR"]


ROOT_DIR: Final = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR: Final = ROOT_DIR / "data"
