#!/usr/bin/python
# FermiPasteladox


from PIL import Image, ImageDraw, ImageOps, ImageFont
from UniverseBuilder import CoordinateParser, CoordinateGenerator, Planet
from SpaceArtist import CelestialBodies, OpenSpace, InterfaceOverlay
from Utils.ImageAdjuster import ImageAdjuster
from TwitterWrapper.TweepyWrapper import TwitterApi

from random import randint

bodyArtist = CelestialBodies()
starArtist = OpenSpace()
interfaceArtist = InterfaceOverlay()
imageAdjuster = ImageAdjuster()
coordGenerator = CoordinateGenerator()
twitter = TwitterApi()

# Twitter Testing
# twitter.PostUpdate('test')
twitter.recentMentions()

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
    "803530-4cff-3ae251"
]

planetSeed = CoordinateParser(testPlanetAddresses[11])
planet = Planet(planetSeed, canvas)


# @TODO Bandaids on planets

# @TODO Show planet name/ID
# @TODO planet stats
#       - temperature
#       - life
#       - life types

# @TODO planet destruction
# @TODO advances civilization (visible and space crafts)
# @TODO artificial planets?
# @TODO post planets to twitter
# @TODO reply with planets to explorers: http://stackoverflow.com/questions/16377315/tweepy-user-id-from-mention
#       http://tweepy.readthedocs.io/en/v3.5.0/cursor_tutorial.html

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


# Scale and resize
canvas = (canvas[0]*5, canvas[1]*5)
scene = scene.resize(canvas, Image.NEAREST)


# Interface
scene = interfaceArtist.draw(scene, planet, canvas)

scene.show()
