"""
Checks if the decrypted text is exactly the same as the original text.
"""

from __future__ import annotations
from pathlib import Path


def verification_files(
    original_path: str | Path = "Question 1/raw_text.txt",
    decrypted_path: str | Path = "decrypted_text.txt",
    *,
    encoding: str = "utf-8",
) -> bool:
    """Open both files, read their text, and check if they match."""
    original = Path(original_path).read_text(encoding=encoding)  # Get the original text from the file.
    decrypted = Path(decrypted_path).read_text(encoding=encoding)  # Get the decrypted text from the file.
    return original == decrypted  # Say True only if both texts are the same.
