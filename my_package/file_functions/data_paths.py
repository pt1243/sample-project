from __future__ import annotations
import pathlib
import sys
from typing import TYPE_CHECKING


if TYPE_CHECKING:  # pragma: no cover
    if sys.version_info >= (3, 8):
        from typing import Final
    else:
        from typing_extensions import Final


__all__ = ["ROOT_DIR", "DATA_DIR"]


ROOT_DIR: Final = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR: Final = ROOT_DIR / "data"
