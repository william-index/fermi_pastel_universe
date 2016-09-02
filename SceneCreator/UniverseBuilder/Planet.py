#!/usr/bin/python
import attr
from ..DataLists.Colors import colors
from ..Utils.ImageAdjuster import ImageAdjuster


from random import randint

"""
Generates Planet Data and details from seed
"""
@attr.s
class Planet(object):
    seed = attr.ib()
    canvas = attr.ib()

    @property
    def imageAdjuster(self):
        return ImageAdjuster()

    @property
    def baseColor(self):
        return self.getColor(0)

    @property
    def secondaryColor(self):
        return self.getColor(1)

    @property
    def bgColor(self):
        return self.imageAdjuster.adjustHSV(self.baseColor, [.1, 0, 0])

    @property
    def signMod(self):
        values = self.seed.values
        if self.seed.total % 2:
            return 1
        else:
            return -1

    @property
    def streaks(self):
        return self.seed.values[9] % 5

    @property
    def box(self):
        boxX1 = self.canvas[0]/2-self.r
        boxY1 = self.canvas[1]/2-self.r
        boxX2 = self.canvas[0]/2+self.r
        boxY2 = self.canvas[1]/2+self.r
        return (boxX1, boxY1, boxX2, boxY2)

    @property
    def shadowIntensity(self):
        return (self.seed.values[8]/16.0 % 0.3) + 0.1

    @property
    def isShiny(self):
        return self.seed.values[self.seed.values[7]] % 2

    @property
    def ringColor(self):
        return self.imageAdjuster.adjustHSV(
            self.secondaryColor,
            [0.4, 0, 0]
        )

    @property
    def ringAngle(self):
        return (self.seed.values[11]*self.seed.values[10]) %90

    @property
    def moonColors(self):
        return [
            self.getColor(3),
            self.getColor(4),
            self.getColor(5),
            self.getColor(6),
            self.getColor(3),
            self.getColor(4),
            self.getColor(5),
            self.getColor(6),
            self.getColor(3),
            self.getColor(4),
            self.getColor(5),
            self.getColor(6)
        ]

    @property
    def life(self):
        lifeTypes = []
        values = self.seed.values

        if self.seed.total % 25 < 2 and sum(values[0:6]) >= 30:
            if sum(values[0:6]) == sum(values[6:10]) == sum(values[10:16]):
                lifeTypes = ["intelligent"]
            elif sum(values[0:6]) == sum(values[10:16]):
                lifeTypes = ["flora", "fauna"]
            else:
                lifeTypes = ["primordial"]

        return lifeTypes

    @property
    def drips(self):
        if self.seed.total % 2:
            return []

        totalDrips = self.seed.values[14]
        if totalDrips == 0:
            totalDrips = 1

        drips = []
        for drip in range(0, totalDrips):
            dripX = ((self.seed.values[drip]*self.seed.total*drip) % (self.r*2)) + (self.box[0] + 1)
            dripY = self.box[1] + self.r
            dripH = (((self.seed.values[drip]*self.seed.total*(drip+1)) % 36) % (self.r)) + (self.r/3)
            dripW = (self.seed.values[drip]%3) + 1
            drips.append([dripX, dripY, dripH, dripW])
        return drips

    @property
    def rings(self):
        values = self.seed.values
        box = self.box
        rings = []

        if self.seed.total % 2:
            numRings = self.seed.total % 8
            ringSizes = [((values[16-ring-1] + (values[16-ring-1] % 2))*11)%24 for ring in range(0, numRings)]

            for ringSize in ringSizes:
                if ringSize > 2:
                    ringWidth = self.r + ringSize/2
                    ringHeight = self.r/2

                    ringX = box[0] - ringSize/2
                    ringY = box[1] + self.r - ringSize/2
                    ringW = box[2] + ringSize/2
                    ringH = ringY + ringSize
                    ring = (ringX, ringY, ringW, ringH)
                    rings.append(ring)

        return rings

    @property
    def moons(self):
        values = self.seed.values
        moons = []
        if values[13] % 2:
            for m in range(0, values[values[11]] % 7):
                valueIndex = values[(values[(0+m)%16])%16]

                moonSize = int((valueIndex % self.r/3.0) + 2)
                moonSize = moonSize + (moonSize % 2) #keep it even :)

                moonX = int(values[valueIndex]/16.0 * self.canvas[0]*.7)
                moonY = int(values[values[valueIndex]]/16.0 * self.canvas[1]*.7)
                moon = ((moonX, moonY), (moonSize+moonX, moonSize+moonY))

                moons.append(moon)
        return moons

    @property
    def r(self):
        return (self.seed.total % 20) + 4

    @property
    def landCount(self):
        landCountSeedIndex = self.seed.values[self.seed.total % 16]
        landCount = 0
        if landCountSeedIndex % 3:
            landCount = (self.seed.total % landCountSeedIndex)
        return landCount

    @property
    def lands(self):
        landCount = self.landCount
        lands = []

        for i in range(0, landCount):
            index1 = self.seed.values[i%16]
            index2 = self.seed.values[(index1*index1) % 16]
            landSteps = ((self.seed.total % 16) % (index2+1)) + 2
            land = [(((self.seed.values[self.seed.total % 16]) % (step + 1)) % 8) - 3 for step in range(0, landSteps)]

            xPercent = float(((index2 + 1.0) / ((index1*index2 % 16) + 1.0))) % 1.0
            yPercent = float(((index1 + 1.0) / ((index1*index2 % 16) + 1.0))) % 1.0

            landx = self.box[0] + int(self.r*2 * xPercent)
            landy = self.box[1] + int(self.r*2 * yPercent)
            landr = ((self.box[0] * int(100 * xPercent) * int(100 * yPercent)) % (index1+1)) + 1
            lands.append([landx, landy, landr] + land)

        return lands

    @property
    def shadows(self):
        shadow1 = (self.box[0]+self.box[0]/8, self.box[1]+self.box[1]/8, self.box[2]-self.box[0]/4, self.box[3]-self.box[0]/4)
        shadow2 = (self.box[0]+self.box[0]/4, self.box[1]+self.box[1]/4, self.box[2]-self.box[0]/2.5, self.box[3]-self.box[0]/2)
        return [shadow1, shadow2]

    def getColor(self, key, mod=0):
        values = self.seed.values
        totalNumberSeed = 0
        for k, v in enumerate(range(key % 16, (key + 3) % 16)):
            key = values[values[v]]
            totalNumberSeed += key

        colorKey = ((totalNumberSeed % len(colors)) + mod) % len(colors)
        return colors[colorKey]
