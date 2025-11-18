def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (ignore non-alphanumeric and case)."""
    filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]

# generate helper to normalize and strip non-alphanumeric characters from a string
def normalize_string(s: str) -> str:
    """Return a normalized version of the string with only lowercase alphanumeric characters."""
    return ''.join(ch.lower() for ch in s if ch.isalnum())


# suggest a helper to cache normalized strings for repeated calls
from functools import lru_cache
@lru_cache(maxsize=128)
def cached_normalize_string(s: str) -> str:
    """Return a cached normalized version of the string."""
    return normalize_string(s)