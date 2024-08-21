#!/usr/bin/python3
"""This module defines the validUTF8 function."""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
        Check if a list of integers represents a valid UTF-8 encoded sequence
    """
    num_bytes = 0
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Ensure byte is an integer between 0 and 255
        if not isinstance(byte, int) or byte < 0 or byte > 255:
            return False

    # If num_bytes is 0, we're looking for first byte in a new UTF-8 character
        if num_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:  # 1-byte character (ASCII)
                continue

            if num_bytes == 1 or num_bytes > 4:  # Invalid UTF-8 sequence
                return False

            else:
                # All subsequent bytes must start with 10xxxxxx
                if not (byte & mask1 and not (byte & mask2)):
                    return False
    num_bytes -= 1

    # If num_bytes isnt zero then we hav incomplete UTF-8 char
    return num_bytes == 0


# Test cases
data = [65, 90.03]  # Invalid input (contains a float)
print(validUTF8(data))  # Expected: False

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Expected: True

data = [229, 65, 127, 256]  # Invalid input (contains a num of 0-255 range)
print(validUTF8(data))  # Expected: False
