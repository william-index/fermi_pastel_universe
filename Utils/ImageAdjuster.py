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
                    imageData[x, y] = self.adjustHSV(oColor, [0, adjust, 0])

        return image

    def adjustHSV(self, rgbaColor, adjusts):
        hsv = colorsys.rgb_to_hsv(rgbaColor[0]/255.0, rgbaColor[1]/255.0, rgbaColor[2]/255.0)
        hsv = (
            hsv[0] + (adjusts[0]),
            hsv[1] + (adjusts[1]),
            hsv[2] + (adjusts[2]))
        rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
        modifiedRGBA = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255), rgbaColor[3])
        return modifiedRGBA

    def invertMask(self, mask):
        maskData = mask.load()
        for y in xrange(mask.size[1]):
            for x in xrange(mask.size[0]):
                if maskData[x, y] == (0,0,0,0):
                    maskData[x, y] = (255,255,255,255)
                else:
                    maskData[x, y] = (0,0,0,0)

        return mask
