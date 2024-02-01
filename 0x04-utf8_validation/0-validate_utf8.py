#!/usr/bin/python3
"""
method that determines if a given data
set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    param data: A list of integers representing the data set.
    return: True if data is a valid UTF-8 encoding, else return False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Count the number of bytes in this UTF-8 character
            if byte & 0b10000000 == 0:
                continue
            elif byte & 0b11100000 == 0b11000000:
                num_bytes = 1
            elif byte & 0b11110000 == 0b11100000:
                num_bytes = 2
            elif byte & 0b11111000 == 0b11110000:
                num_bytes = 3
            else:
                return False
        # If this is not the start of a new UTF-8 character
        else:
            # Check if the current byte is a continuation byte
            if byte & 0b11000000 == 0b10000000:
                num_bytes -= 1
            else:
                return False

    # If we have reached the end of the data set and all characters are valid
    return num_bytes == 0
