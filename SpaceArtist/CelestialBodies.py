#!/usr/bin/python
from PIL import Image, ImageDraw, ImageOps
from UniverseBuilder.TerrainBuilder import TerrainBuilder
from Utils.ImageAdjuster import ImageAdjuster

# image adjustment utility
imageAdjuster = ImageAdjuster()

"""
Parser for coordinate strings
"""
class CelestialBodies:

    def draw(self, scene, body, canvas):
        # drips
        draw = ImageDraw.Draw(scene)
        for drip in body.drips:
            draw.line(
                (drip[0], drip[1]) + (drip[0], drip[1] + drip[2]),
                (255, 255, 255, 255),
                drip[3])

        # planet body
        draw = ImageDraw.Draw(scene)
        draw.ellipse(body.box, fill=body.baseColor)
        pMask = Image.new("RGBA", canvas, (0, 0, 0, 0))

        # planet terrain
        terrainBuilder = TerrainBuilder(body, canvas, pMask)

        # create body mask
        draw = ImageDraw.Draw(pMask)
        draw.ellipse(body.box, fill=(255,255,255,255))

        # ring mask setup
        ringMask = Image.new("RGBA", canvas, (0, 0, 0, 0))
        pMaskRings = pMask.copy()
        pMaskRings = pMaskRings.crop((0, 0, canvas[0], canvas[1]/2))
        ringMask.paste(pMaskRings, (0,0))

        # Add Land Masses
        if body.landCount:
            land = terrainBuilder.buildLandMasses()
            scene.paste(land, (0,0), land)

        # Handle Shading Planet
        for shadow in body.shadows:
            shadowCan = Image.new("RGBA", canvas, (0, 0, 0, 0))
            draw = ImageDraw.Draw(shadowCan)
            draw.ellipse(shadow, fill=(255,255,255,255))

            scene = imageAdjuster.adjustArea(scene, shadowCan, body.shadowIntensity)

        # outline
        draw = ImageDraw.Draw(scene)
        draw.ellipse(body.box, outline=(255,255,255,255))

        # draw rings
        ringsScene = Image.new("RGBA", canvas, (0, 0, 0, 0))
        ringArt = Image.new("RGBA", canvas, (0, 0, 0, 0))
        draw = ImageDraw.Draw(ringArt)
        for ring in body.rings:
            draw.ellipse(ring, outline=body.ringColor)

        # angle rings
        ringArt = ringArt.rotate(body.ringAngle)
        ringMask = ringMask.rotate(body.ringAngle)

        # compose scene
        ringsScene.paste(ringArt, (0,0), imageAdjuster.invertMask(ringMask))
        scene.paste(ringsScene, (0,0), ringsScene)
        return scene
