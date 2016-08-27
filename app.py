#!/usr/bin/python
from PIL import Image, ImageDraw, ImageOps
from UniverseBuilder.CoordinateParser import CoordinateParser
from UniverseBuilder.Planet import Planet
from SpaceArtist.CelestialBodies import CelestialBodies

bodyArtist = CelestialBodies()

canvas = (100, 80)
# "1974cf-d321-ff224a"
# "523b56-789f-abcdef"
# "5b5b5b-1212-abcdef"
# "5b5b5b-1212-aaaaaa"
# "812391-4365-675434"
planetSeed = CoordinateParser("1974cf-d321-ff224a")
planet = Planet(planetSeed, canvas)


# @TODO method/class for draw celestial body
# @TODO colors
# @TODO gradients
# @TODO gas planets
# @TODO craters
# @TODO atmospheres
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

# Draw background color and planet
draw = ImageDraw.Draw(scene)
draw.rectangle(((0, 0), canvas), fill=(235,205,212,255))

# draw planet
scene = bodyArtist.draw(scene, planet, canvas)

# add moons
for moon in planet.moons:
    draw.ellipse(moon, fill=(235,0,0,255))

scene = scene.resize((500, 400), Image.NEAREST)
scene.show()
