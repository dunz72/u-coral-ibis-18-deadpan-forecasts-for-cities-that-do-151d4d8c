"""Deadpan Forecasts for Cities That Do Not Exist entry.

The single original forecast line lives in entry.txt next to this
file. This script reads it, checks it fits the sealed gate (1-160
characters, valid UTF-8, exactly one line, not only whitespace),
then writes an exact byte copy to $MAKEFUN_OUTPUT_DIR/entry.txt,
falling back to ./output/entry.txt when that variable is not set.
After writing, the copy is read back and compared by SHA-256 so a
partial write can never pass silently. Stdlib only.
"""

import hashlib
import os


def source_path():
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, "entry.txt")


def read_source(path):
    with open(path, "rb") as handle:
        return handle.read()


def decode_forecast(raw):
    return raw.decode("utf-8")


def check_forecast(text):
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be empty or only whitespace")
    if len(cleaned) > 160:
        raise ValueError(
            f"entry must be at most 160 characters, got {len(cleaned)}"
        )
    if text != cleaned:
        raise ValueError("entry.txt must hold exactly one line")
    if not any(ch.isdigit() for ch in cleaned):
        raise ValueError("entry must include a concrete number or figure")
    return cleaned


def output_folder():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")


def store_copy(raw, directory):
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(raw)
    with open(target, "rb") as handle:
        stored = handle.read()
    if hashlib.sha256(stored).hexdigest() != hashlib.sha256(raw).hexdigest():
        raise ValueError("output is not byte-identical to entry.txt")
    return target


def main():
    raw = read_source(source_path())
    text = check_forecast(decode_forecast(raw))
    target = store_copy(raw, output_folder())
    digest = hashlib.sha256(raw).hexdigest()
    print(f"wrote {len(raw)} bytes ({len(text)} chars) to {target}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
