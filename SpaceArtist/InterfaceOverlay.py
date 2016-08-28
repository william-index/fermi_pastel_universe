#!/usr/bin/python
from PIL import Image, ImageDraw, ImageOps, ImageFont


"""
Handles Drawing Interface elements
"""
class InterfaceOverlay:
    def __init__(self):
        self.topArea = 0
        self.bottomArea = 60
        self.font = ImageFont.truetype('fonts/PressStart2P.ttf', 12)
        self.canvas = (0,0)

    def draw(self, scene, planet, canvas):
        self.canvas = (canvas[0], canvas[1]+self.topArea+self.bottomArea)
        interfacedScene = Image.new('RGBA', self.canvas, (255,255,255,255))
        interfacedScene.paste(scene, (0,self.topArea))

        # Planet Name
        text = 'PLANET: ' + planet.seed.raw.upper()
        self.drawCenteredText(text, self.canvas[1]-25-18, planet.bgColor, interfacedScene)

        # Life Detected
        text = 'Void of Life'
        if planet.life:
            text= 'Life! Type: (' + ', '.join(planet.life) + ')'
        self.drawCenteredText(text.upper(), self.canvas[1]-25, planet.bgColor, interfacedScene)

        return interfacedScene

    def drawCenteredText(self, text, y, color, scene):
        draw = ImageDraw.Draw(scene)

        size = self.font.getsize(text)
        leftOffset = (self.canvas[0] - size[0])/2
        draw.text((leftOffset, y), text, color, font=self.font)
