#!/usr/bin/python

from DataLists.Colors import colors
from Utils.ImageAdjuster import ImageAdjuster

from random import randint

"""
Generates Planet Data and details from seed
"""
class Planet:
    def __init__(self, seed, canvas):
        self.imageAdjuster = ImageAdjuster()

        self.seed = seed
        self.canvas = canvas

        self.r = self.getPlanetRadius()
        self.box = (canvas[0]/2-self.r, canvas[1]/2-self.r, canvas[0]/2+self.r, canvas[1]/2+self.r)
        self.landCount = self.getLandMassCount()
        self.lands = self.createLandMassPatterns(self.landCount)

        self.atmosphere = self.createAtmosphere()

        self.shadows = self.createShadows()
        self.shadowIntensity = (self.seed.values[8]/16.0 % 0.3) + 0.1

        self.moons = self.generateMoons()
        self.rings = self.generateRings()

        self.signMod = self.getSignMod()

        self.isShiny = self.seed.values[self.seed.values[7]] % 2

        # colorsys
        self.baseColor = self.getColor(0)
        self.secondaryColor = self.getColor(1)

        self.ringColor = self.imageAdjuster.adjustHSV(self.secondaryColor, [0.4, 0, 0])
        self.moonColors = [self.getColor(3), self.getColor(4), self.getColor(5), self.getColor(6)]

        self.ringAngle = (self.seed.values[11]*self.seed.values[10]) %90

        self.drips = self.generateDrips()

    def generateDrips(self):
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

    def getSignMod(self):
        values = self.seed.values
        if self.seed.total % 2:
            return 1
        else:
            return -1

    def getColor(self, key, mod=0):
        values = self.seed.values
        totalNumberSeed = 0
        for k, v in enumerate(range(key % 16, (key + 3) % 16)):
            key = values[values[v]]
            totalNumberSeed += key

        colorKey = ((totalNumberSeed % len(colors)) + mod) % len(colors)
        return colors[colorKey]

    def generateRings(self):
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

    def generateMoons(self):
        values = self.seed.values
        moons = []
        for m in range(0, values[11] % 4):
            valueIndex = values[(values[(0+m)%16])%16]

            moonSize = int((valueIndex % self.r/3) + 2)
            moonSize = moonSize + (moonSize % 2) #keep it even :)

            moonX = int(values[valueIndex]/16.0 * self.canvas[0]*.7)
            moonY = int(values[values[valueIndex]]/16.0 * self.canvas[1]*.7)
            moon = ((moonX, moonY), (moonSize+moonX, moonSize+moonY))

            moons.append(moon)
        return moons

    def getPlanetRadius(self):
        return (self.seed.total % 20) + 4

    def getLandMassCount(self):
        landCountSeedIndex = self.seed.values[self.seed.total % 16]
        landCount = 0
        if landCountSeedIndex % 2:
            landCount = (self.seed.total % landCountSeedIndex)
        return landCount

    def createLandMassPatterns(self, landCount):
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

    def createAtmosphere(self):
        print "atmospheres not enabled"
        return

    def createShadows(self):
        shadow1 = (self.box[0]+self.box[0]/8, self.box[1]+self.box[1]/8, self.box[2]-self.box[0]/4, self.box[3]-self.box[0]/4)
        shadow2 = (self.box[0]+self.box[0]/4, self.box[1]+self.box[1]/4, self.box[2]-self.box[0]/2.5, self.box[3]-self.box[0]/2)
        return [shadow1, shadow2]
