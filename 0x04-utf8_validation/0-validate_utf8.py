#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """Determines if given data set represents valid utf-8 encoding"""
    nbytes = 0

    for b in data:
        if not isinstance(b, int):
            return False

        b = b & 0xFF

        if nbytes == 0:
            if b >> 5 == 0b110:
                nbytes = 1
            elif b >> 4 == 0b1110:
                nbytes = 2
            elif b >> 3 == 0b11110:
                nbytes = 3
            elif b >> 7:
                return False
        else:
            if b >> 6 != 0b10:
                return False
            nbytes -= 1
    return nbytes == 0
