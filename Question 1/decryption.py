from __future__ import annotations 
from pathlib import Path

# function to shift a character within its half of the alphabet
def _shift_in_half(ch: str, delta: int, start: str) -> str:
   
    base = ord(start)
    offset = ord(ch) - base
    return chr(base + (offset + delta) % 13)

# function to decrypt a single character based on the specified rules
def decrypt_char(ch: str, shift1: int, shift2: int, *args, **kwargs) -> str:
    
    if ch.islower():
        # First half lowercase (a-m): backward shift
        if "a" <= ch <= "m":
            return _shift_in_half(ch, -(shift1 * shift2), "a")
        # Second half lowercase (n-z): forward shift
        return _shift_in_half(ch, shift1 + shift2, "n")

    if ch.isupper():
        # First half uppercase (A-M): forward shift
        if "A" <= ch <= "M":
            return _shift_in_half(ch, shift1, "A")
        # Second half uppercase (N-Z): backward squared shift
        return _shift_in_half(ch, -(shift2 ** 2), "N")

    return ch

# function to decrypt an entire file
def decrypted_file(
    input_path: str | Path = "encrypted_text.txt",
    output_path: str | Path = "decrypted_text.txt",
    *,
    shift1: int,
    shift2: int,
    **kwargs
) -> str:
    
    encoding = kwargs.get("encoding", "utf-8")

    text = Path(input_path).read_text(encoding=encoding)
    decrypted_text = "".join(decrypt_char(c, shift1, shift2) for c in text)
    Path(output_path).write_text(decrypted_text, encoding=encoding)

    return decrypted_text