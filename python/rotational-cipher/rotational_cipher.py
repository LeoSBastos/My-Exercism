def rotate(text: str, key: int) -> str:
    return ''.join(
        [
            chr((ord(c) - ord('a') + key) % 26 + ord('a'))
            if c.islower()
            else chr((ord(c) - ord('A') + key) % 26 + ord('A'))
            if c.isupper()
            else c
            for c in list(text)
        ]
    )
