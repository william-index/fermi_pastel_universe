#!/usr/bin/python
from PIL import Image, ImageDraw, ImageOps
from UniverseBuilder.CoordinateParser import CoordinateParser
from UniverseBuilder.Planet import Planet
from SpaceArtist.CelestialBodies import CelestialBodies
from Utils.ImageAdjuster import ImageAdjuster

bodyArtist = CelestialBodies()
imageAdjuster = ImageAdjuster()

canvas = (100, 100)
testPlanetAddresses = [
    "1974cf-d321-ff224a",
    "523b56-789f-abcdef",
    "5b5b5b-1212-abcdef",
    "5b5b5b-1212-aaaaaa",
    "812391-4365-675434",
    "abf654-1111-000000"
]

planetSeed = CoordinateParser(testPlanetAddresses[0])
planet = Planet(planetSeed, canvas)


# @TODO background gradient meshes
# @TODO shiny planets
# @TODO drips
# @TODO Bandaids on planets
# @TODO background stars

# @TODO atmospheres
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

# Draw background color and planet
draw = ImageDraw.Draw(scene)
draw.rectangle(((0, 0), canvas), fill=imageAdjuster.adjustHSV(planet.baseColor, [.1, 0, 0]))

# draw planet
scene = bodyArtist.draw(scene, planet, canvas)

# add moons
for k, moon in enumerate(planet.moons):
    draw.ellipse(moon, fill=planet.moonColors[k], outline=(255,255,255,255))

scene = scene.resize((canvas[0]*5, canvas[1]*5), Image.NEAREST)
scene.show()
