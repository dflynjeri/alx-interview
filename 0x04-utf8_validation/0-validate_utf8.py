#!/usr/bin/python3
"""A module to validate UTF-8 encoding."""


def validUTF8(data):
    # Variable to keep track of how many bytes are expected in a UTF-8
    # character
    bytes_to_process = 0

    for byte in data:
        # Mask to get the 8 least significant bits (1 byte)
        byte = byte & 0xFF

        if bytes_to_process == 0:
            # Determine number of bytes in the current character
            if (byte >> 5) == 0b110:  # 2-byte character
                bytes_to_process = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                bytes_to_process = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                bytes_to_process = 3
            elif (byte >> 7):  # 1-byte character, leading bit should be 0
                return False
        else:
            # Check if byte follows the pattern 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            bytes_to_process -= 1

    return bytes_to_process == 0
