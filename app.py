#!/usr/bin/python
from PIL import Image, ImageDraw, ImageOps
from UniverseBuilder.CoordinateParser import CoordinateParser
from UniverseBuilder.Planet import Planet
from UniverseBuilder.TerrainBuilder import TerrainBuilder
from SpaceArtist.CelestialBody import CelestialBody
from Utils.ImageAdjuster import ImageAdjuster

# image adjustment utility
imageAdjuster = ImageAdjuster()

canvas = (100, 80)
# "1974cf-d321-ff224a"
# "523b56-789f-abcdef"
# "5b5b5b-1212-abcdef"
# "5b5b5b-1212-aaaaaa"
planetSeed = CoordinateParser("1974cf-d321-ff224a")
planet = Planet(planetSeed, canvas)


# @TODO method/class for draw celestial body
# @TODO seeds
# @TODO colors
# @TODO gradients
# @TODO gas planets
# @TODO craters
# @TODO atmospheres
# @TODO rings
# @TODO background gradient meshes
# @TODO background stars
# @TODO planet states
#       - life
#       - life types
# @TODO planet destruction
# @TODO advances civilization (visible and space crafts)
# @TODO artificial planets?

# Create Scene for Universe Photo
scene = Image.new("RGBA", canvas, (0, 0, 0, 0))
pMask = scene.copy()

terrainBuilder = TerrainBuilder(planet, canvas, pMask)

# Draw background color and planet
draw = ImageDraw.Draw(scene)
draw.rectangle(((0, 0), canvas), fill=(235,205,212,255))
draw.ellipse(planet.box, fill=(135,205,212,255))

# create planet mask
draw = ImageDraw.Draw(pMask)
draw.ellipse(planet.box, fill=(255,255,255,255))

# Add Land Masses
if planet.landCount:
    land = terrainBuilder.buildLandMasses()
    scene.paste(land, (0,0), land)

# Handle Shading Planet
for shadow in planet.shadows:
    shadowCan = Image.new("RGBA", canvas, (0, 0, 0, 0))
    draw = ImageDraw.Draw(shadowCan)
    draw.ellipse(shadow, fill=(255,255,255,255))

    scene = imageAdjuster.adjustArea(scene, shadowCan, planet.shadowIntensity)

scene = scene.resize((500, 400), Image.NEAREST)
scene.show()
