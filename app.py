#!/usr/bin/python
from PIL import Image, ImageDraw, ImageOps
from UniverseBuilder.CoordinateParser import CoordinateParser, CoordinateGenerator
from UniverseBuilder.Planet import Planet
from SpaceArtist.CelestialBodies import CelestialBodies
from Utils.ImageAdjuster import ImageAdjuster

from random import randint

bodyArtist = CelestialBodies()
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
    coordGenerator.getRandomAddress()
]

planetSeed = CoordinateParser(testPlanetAddresses[10])
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

# Draw background color
draw = ImageDraw.Draw(scene)
bgColor = imageAdjuster.adjustHSV(planet.baseColor, [.1, 0, 0])
draw.rectangle(((0, 0), canvas), fill=bgColor)

# create background gradient
sceneData = scene.load()
spaceRangeRate = ((((planet.seed.total%4)+1)/10.0)+.1)
for x in range(0, canvas[0]):
    for y in range(0, canvas[1]):
        sceneData[x,y] = imageAdjuster.adjustHSV(sceneData[x,y],
            [
                ((y+(x*planet.signMod))/200.0)*spaceRangeRate,
                0,
                0])

# Adds stars
starField = Image.new("RGBA", canvas, (0, 0, 0, 0))
draw = ImageDraw.Draw(starField)
heart = Image.open("art/heart_7_7.png").convert('RGBA')
burst = Image.open("art/star_burst_7_7.png").convert('RGBA')
# heart = heart.resize((5, 5), Image.NEAREST)
# heartData = heart.load()
for i in range(0,((planet.seed.total+1)*333)%60):
    xSeed = planet.seed.values[i%16]
    ySeed = planet.seed.values[15-(i%16)]

    x = ((xSeed**xSeed) * (ySeed+1)) % canvas[0]
    y = ((ySeed**ySeed) * (xSeed+1)) % canvas[1]

    heartMod = planet.seed.values[planet.seed.values[11]] + 7
    burstMod = planet.seed.values[planet.seed.values[3]] + 11
    if x%heartMod == y%heartMod:
        starField.paste(heart, (x,y), heart)
    elif x%burstMod == y%burstMod:
        starField.paste(burst, (x,y), burst)
    else:
        size = (((x+y)%2)+1)*2
        draw.rectangle((x,y,x,y+size), fill=(255,255,255,255/(8-size)))
        draw.rectangle((x-(size/2),y+(size/2),x+(size/2),y+(size/2)), fill=(255,255,255,255/(8-size)))

scene.paste(starField, (0,0), starField)

# draw planet
scene = bodyArtist.draw(scene, planet, canvas)

# add moons
for k, moon in enumerate(planet.moons):
    draw.ellipse(moon, fill=planet.moonColors[k], outline=(255,255,255,255))

scene = scene.resize((canvas[0]*5, canvas[1]*5), Image.NEAREST)
scene.show()
