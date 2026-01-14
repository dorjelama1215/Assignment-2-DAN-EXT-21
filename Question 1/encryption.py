

HALF_SIZE = 13


def _wrap_shift(code: int, base: int, shift: int) -> str:

    relative_pos = code - base
    new_pos = (relative_pos + shift) % HALF_SIZE
    return chr(base + new_pos)


def encrypt_character(char: str, shift1: int, shift2: int) -> str:

    if "a" <= char <= "m":
        return _wrap_shift(ord(char), ord("a"), shift1 * shift2)

    if "n" <= char <= "z":
        return _wrap_shift(ord(char), ord("n"), -(shift1 + shift2))

    if "A" <= char <= "M":
        return _wrap_shift(ord(char), ord("A"), -shift1)

    if "N" <= char <= "Z":
        return _wrap_shift(ord(char), ord("N"), shift2 ** 2)

    return char


def encrypted_file(
    source: str | Path = "raw_text.txt",
    destination: str | Path = "encrypted_text.txt",
    *,
    shift1: int,
    shift2: int,
    encoding: str = "utf-8",
) -> str:
 
    text = Path(source).read_text(encoding=encoding)

    encrypted = []
    for ch in text:
        encrypted.append(encrypt_character(ch, shift1, shift2))

    encrypted_text = "".join(encrypted)
    Path(destination).write_text(encrypted_text, encoding=encoding)

    return encrypted_text