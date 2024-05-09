#!/usr/bin/python3
"""
method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """

    def check_prefix(byte):
        """
        Checks if a given byte starts with the correct UTF-8 prefix.

        Args:
            byte (int): The byte to check.

        Returns:
            bool: True if the byte starts with '10', else False.
        """
        return bin(byte).startswith('0b10')

    i = 0
    while i < len(data):
        if data[i] < 128:  # 1-byte character
            i += 1
        elif data[i] < 224:  # 2-byte character
            if i + 1 >= len(data) or not check_prefix(data[i + 1]):
                return False
            i += 2
        elif data[i] < 240:  # 3-byte character
            if i + 2 >= len(data) or \
                not check_prefix(data[i + 1]) or \
                    not check_prefix(data[i + 2]):
                return False
            i += 3
        elif data[i] < 248:  # 4-byte character
            if i + 3 >= len(data) or \
                not check_prefix(data[i + 1]) or \
                    not check_prefix(data[i + 2]) or \
                    not check_prefix(data[i + 3]):
                return False
            i += 4
        else:  # Invalid byte
            return False

    return True
