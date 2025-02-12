def add(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b

def reverse_string(s: str) -> str:
    """Returns the reverse of the given string."""
    new_s=s[::-1]
    return new_s

def is_even(n: int) -> bool:
    """Returns True if the number is even, otherwise False."""
    if n%2==0:
        return True
    else:
        False
        
