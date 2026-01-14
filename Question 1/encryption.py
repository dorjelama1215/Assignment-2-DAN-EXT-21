from pathlib import Path

HALF_SIZE = 13

#Shifting a character code within its half-alphabet range
def _wrap_shift(code: int, base: int, shift: int) -> str:
#converting absolute positon codes
    relative_pos = code - base
    new_pos = (relative_pos + shift) % HALF_SIZE
    return chr(base + new_pos)

#converting back to caracter
def encrypt_character(char: str, shift1: int, shift2: int) -> str:
#lowercaseshifting forward 
    if "a" <= char <= "m":
        return _wrap_shift(ord(char), ord("a"), shift1 * shift2)
#lowercase: shifting back
    if "n" <= char <= "z":
        return _wrap_shift(ord(char), ord("n"), -(shift1 + shift2))
#uppercase: shiftig back 
    if "A" <= char <= "M":
        return _wrap_shift(ord(char), ord("A"), -shift1)
#uppercase: shifting forward 
    if "N" <= char <= "Z":
        return _wrap_shift(ord(char), ord("N"), shift2 ** 2)

    return char


def encrypted_file(
    source: str | Path = "Question 1/raw_text.txt",
    destination: str | Path = "encrypted_text.txt",
    *,
    shift1: int,
    shift2: int,
    encoding: str = "utf-8",
) -> str:
#reading the source file
    text = Path(source).read_text(encoding=encoding)
#encryptig them individually 
    encrypted = []
    for ch in text:
        encrypted.append(encrypt_character(ch, shift1, shift2))
#single string are joined with encrypted characters
    encrypted_text = "".join(encrypted)
#writing for destination file
    Path(destination).write_text(encrypted_text, encoding=encoding)

    return encrypted_text