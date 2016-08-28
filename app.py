#!/usr/bin/python
from PIL import Image, ImageDraw, ImageOps
from UniverseBuilder.CoordinateParser import CoordinateParser, CoordinateGenerator
from UniverseBuilder.Planet import Planet
from SpaceArtist.CelestialBodies import CelestialBodies
from SpaceArtist.OpenSpace import OpenSpace
from Utils.ImageAdjuster import ImageAdjuster

from random import randint

bodyArtist = CelestialBodies()
starArtist = OpenSpace()
imageAdjuster = ImageAdjuster()
coordGenerator = CoordinateGenerator()

canvas = (100, 100)
testPlanetAddresses = [
    "1974cf-d321-ff224a",
    "523b56-789f-abcdef",
    "5b5b5b-1212-abcdef",
    "5b5b5b-1212-aaaaaa",
    "812391-4365-675434",
    "abf654-1111-000000",
    "239f90-2bca-dd4231",
    "111111-0000-111111",
    "abad1d-3aaba-d1d3a",
    "a61221-17a21-11111",
    "cb1143-0019-6a43c9",
    coordGenerator.getRandomAddress(),
    "c516da-576a-81cc50"
]

planetSeed = CoordinateParser(testPlanetAddresses[11])
planet = Planet(planetSeed, canvas)


# @TODO background streaks
# @TODO atmospheres
# @TODO Bandaids on planets

# @TODO craters

# @TODO planet states
#       - life
#       - life types

# @TODO planet destruction
# @TODO advances civilization (visible and space crafts)
# @TODO artificial planets?

# Create Scene for Universe Photo
scene = Image.new("RGBA", canvas, (0, 0, 0, 0))
pMask = scene.copy()

# Draw background colors
starArtist.drawBackground(scene, planet, canvas)

# Draw light lines
starArtist.drawStreaks(scene, planet, canvas)

# Adds stars
starArtist.drawStars(scene, planet, canvas)

# draw planet
bodyArtist.draw(scene, planet, canvas)

# add moons
draw = ImageDraw.Draw(scene)
for k, moon in enumerate(planet.moons):
    draw.ellipse(moon, fill=planet.moonColors[k], outline=(255,255,255,255))

scene = scene.resize((canvas[0]*5, canvas[1]*5), Image.NEAREST)
scene.show()
