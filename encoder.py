"""Encode/Decode signed 14-bit integer values"""

LOBYTE_MASK = int("7F", 16) # 7 digits
RANGE_SIZE = 8192

def encode(num: int) -> str:
    """Encode signed 14-bit integer in standardized hex format

    >>> encode(6111)
    '6f5f'
    >>> encode(340)
    '4254'
    >>> encode(-2628)
    '2b3c'
    >>> encode(-255)
    '3e01'
    >>> encode(7550)
    '7a7e'

    """

    if num not in range(-RANGE_SIZE, RANGE_SIZE):
        raise ValueError(f"Integer argument must be in [-{RANGE_SIZE}, {RANGE_SIZE})")

    translated = num + RANGE_SIZE
    lobyte = translated & LOBYTE_MASK
    hibyte = translated ^ lobyte
    encoded = lobyte + (hibyte << 1)
    return str(format(encoded, "04x")).upper()

def decode(encoded_num: str) -> int:
    """Decode standardized hex format into signed 14-bit integer

    >>> decode("0A0A")
    -6902
    >>> decode("0029")
    -8151
    >>> decode("3F0F")
    -113
    >>> decode("4400")
    512
    >>> decode("5E7F")
    3967

    """
    num = int(encoded_num, 16)
    lobyte = num & LOBYTE_MASK
    hibyte = num ^ lobyte
    translated = lobyte + (hibyte >> 1)
    return translated - RANGE_SIZE


if __name__ == "__main__":
    import doctest
    doctest.testmod()
