#!/usr/bin/python
from random import randint

"""
Parser for coordinate strings
"""
class CoordinateParser:
    def __init__(self, coords):
        self.raw = coords
        self.values = self.processCoordinates(coords)
        self.total = sum(self.values)

    """Process a coordinates string to an int array
    Removes uneeded characters, and converts to ints, reorganizes list
    based on pattern at %16 from list sum from list of order lists

    Args:
        coords (String) : string in format 000000-0000-000000
            where each non-hyphen character can be any
            single character hex value

    Returns:
        int list: processed coordinate list (used for seeding planet)
    """
    def processCoordinates(self, coords):
        randomizeTemplates = [
            [5, 7, 15, 6, 12, 4, 14, 1, 9, 0, 11, 13, 2, 3, 8, 10],
            [5, 7, 11, 8, 9, 13, 4, 1, 10, 0, 2, 14, 3, 15, 12, 6],
            [0, 5, 10, 15, 4, 12, 13, 3, 2, 14, 11, 1, 7, 8, 6, 9],
            [3, 5, 2, 7, 15, 13, 11, 6, 9, 12, 10, 14, 4, 8, 0, 1],
            [2, 15, 8, 4, 11, 1, 12, 10, 5, 9, 13, 6, 14, 7, 0, 3],
            [8, 14, 0, 12, 4, 15, 7, 13, 1, 9, 11, 3, 5, 6, 10, 2],
            [11, 8, 1, 0, 7, 15, 4, 13, 2, 12, 5, 9, 14, 6, 10, 3],
            [0, 10, 9, 7, 13, 6, 1, 3, 4, 5, 14, 15, 12, 8, 11, 2],
            [11, 7, 5, 1, 10, 8, 4, 14, 6, 12, 2, 3, 0, 13, 9, 15],
            [6, 4, 8, 3, 13, 14, 7, 2, 1, 10, 0, 15, 5, 12, 9, 11],
            [2, 11, 12, 8, 6, 4, 14, 10, 15, 1, 0, 13, 7, 9, 3, 5],
            [15, 3, 1, 12, 11, 4, 14, 13, 9, 10, 8, 5, 0, 7, 2, 6],
            [2, 5, 14, 8, 4, 1, 7, 15, 0, 11, 12, 9, 6, 13, 3, 10],
            [0, 9, 3, 2, 11, 13, 7, 10, 8, 15, 1, 12, 14, 5, 4, 6],
            [13, 3, 0, 12, 14, 9, 1, 10, 6, 15, 2, 5, 7, 8, 4, 11],
            [8, 7, 2, 9, 12, 0, 10, 6, 3, 5, 1, 14, 13, 4, 11, 15]
        ]
        coords = map(self.hexCharToInt ,list(coords.replace("-","")))
        randoms = randomizeTemplates[sum(coords) % 16]
        sortedCoords = [coords[randoms[i]] for i in randoms]
        return sortedCoords

    def hexCharToInt(self, i):
        return int('0x' + i, 0)

class CoordinateGenerator:
    def getRandomAddress(self):
        values = []
        for i in range(0,16):
            ri = randint(0,15)
            rHex = hex(ri)[2:]
            values.append(rHex)
        values.insert(6,'-')
        values.insert(11,'-')
        return ''.join(values)
