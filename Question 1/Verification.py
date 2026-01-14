"""
verification.py
---------------
Verifies whether the decrypted text matches the original raw text.
"""

from __future__ import annotations
from pathlib import Path


def verification_files(
    original_path: str | Path = "Question 1/raw_text.txt",
    decrypted_path: str | Path = "decrypted_text.txt",
    *,
    encoding: str = "utf-8",
) -> bool:
   
    original = Path(original_path).read_text(encoding=encoding)
    decrypted = Path(decrypted_path).read_text(encoding=encoding)

    return original == decrypted
