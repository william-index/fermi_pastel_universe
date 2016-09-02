#!/usr/bin/python
import attr
from PIL import Image, ImageDraw, ImageOps, ImageFont
from UniverseBuilder import CoordinateParser, CoordinateGenerator, Planet
from SpaceArtist import CelestialBodies, OpenSpace, InterfaceOverlay
from Utils.ImageAdjuster import ImageAdjuster

from random import randint

"""
Generates Planet Data and details from seed
"""
@attr.s
class SceneCreator(object):
    _imageAdjuster = attr.ib(default=ImageAdjuster())
    _bodyArtist = attr.ib(default=CelestialBodies())
    _starArtist = attr.ib(default=OpenSpace())
    _interfaceArtist = attr.ib(default=InterfaceOverlay())
    _imageAdjuster = attr.ib(default=ImageAdjuster())
    _coordGenerator = attr.ib(default=CoordinateGenerator())

    _address = attr.ib(default=False)
    _planet = attr.ib(default=False)

    @property
    def address(self):
        if self._address:
            print self._address
            return self._address

        self._address = self._coordGenerator.getRandomAddress()
        print self._address
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def planet(self):
        return self._planet

    @planet.setter
    def planet(self, planet):
        self._planet = planet

    @property
    def sceneTxt(self):
        lifeText = 'Void of Life'
        if self.planet.life:
            lifeText= 'Life! Type: (' + ', '.join(self.planet.life) + ')'

        text = 'Planet: {0}\n{1}'.format(self.address, lifeText)
        return text

    def createScene(self, canvas, coordinates=False):
        if coordinates:
            self.address = coordinates

        planetSeed = CoordinateParser(self.address)

        self.planet = Planet(planetSeed, canvas)
        planet = self.planet

        # Create Scene for Universe Photo
        scene = Image.new("RGBA", canvas, (0, 0, 0, 0))
        pMask = scene.copy()

        # Draw background colors
        self._starArtist.drawBackground(scene, planet, canvas)

        # Draw light lines
        self._starArtist.drawStreaks(scene, planet, canvas)

        # Adds stars
        self._starArtist.drawStars(scene, planet, canvas)

        # draw planet
        self._bodyArtist.draw(scene, planet, canvas)

        # add moons
        draw = ImageDraw.Draw(scene)
        for k, moon in enumerate(planet.moons):
            draw.ellipse(moon, fill=planet.moonColors[k], outline=(255,255,255,255))

        # Scale and resize
        canvas = (canvas[0]*5, canvas[1]*5)
        scene = scene.resize(canvas, Image.NEAREST)

        # Interface
        scene = self._interfaceArtist.draw(scene, planet, canvas)

        return scene, self.sceneTxt
