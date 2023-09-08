import pathlib
from typing import Final


__all__ = ["ROOT_DIR", "DATA_DIR"]


ROOT_DIR: Final = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR: Final = ROOT_DIR / "data"
