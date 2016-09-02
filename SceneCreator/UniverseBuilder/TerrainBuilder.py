#!/usr/bin/python
from PIL import Image, ImageDraw, ImageOps

"""
Build Terrain Items for a planet
"""
class TerrainBuilder:
    def __init__(self, planet, canvas, pMask):
        self.planet = planet
        self.canvas = canvas
        self.pMask = pMask

    """Generates land masses for a planet for a Planet object instance

    Args:
        planet (Planet): a planet object
        canvas (tuple): width and height of canvas
        pMask (Image): mask to use for cropping to planet

    Returns:
        Image: image of landmasses cropped to planet mask
    """
    def buildLandMasses(self):
        planet = self.planet
        land = Image.new("RGBA", self.canvas)
        draw = ImageDraw.Draw(land)
        for landData in planet.lands:
            lx = landData[0]
            ly = landData[1]
            lr = landData[2]

            shiftData = landData[3:]
            for shift in shiftData:
                lx += shift
                ly += (shift*shift) % 8 - 3
                draw.ellipse((lx-lr, ly-lr, lx+lr, ly+lr), fill=planet.secondaryColor)
                lr = (lr+1) % 6

        blank = Image.new("RGBA", self.canvas)
        blank.paste(land, (0, 0), land)
        pplan = Image.new("RGBA", self.canvas)
        pplan.paste(blank, (0, 0), self.pMask)
        return pplan
