#!/usr/bin/python
import colorsys

"""
Generates Planet Data and details from seed
"""
class ImageAdjuster:
    def adjustArea(self, image, area, adjust):
        imageData = image.load()
        areaData = area.load()

        for y in xrange(image.size[1]):
            for x in xrange(image.size[0]):
                if areaData[x, y] == (255, 255, 255, 255):
                    oColor = imageData[x, y]
                    hsv = colorsys.rgb_to_hsv(oColor[0]/255.0, oColor[1]/255.0, oColor[2]/255.0)
                    hsv = (hsv[0], hsv[1] + adjust, hsv[2])

                    rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
                    imageData[x, y] = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255), 255)

        return image
