#!/usr/bin/python

"""
Generates Planet Data and details from seed
"""
class Planet:
    def __init__(self, seed, canvas):
        self.seed = seed
        self.r = self.getPlanetRadius()
        self.box = (canvas[0]/2-self.r, canvas[1]/2-self.r, canvas[0]/2+self.r, canvas[1]/2+self.r)
        self.landCount = self.getLandMassCount()
        self.lands = self.createLandMassPatterns()

        self.shadows = self.createShadows()
        self.shadowIntensity = self.seed.values[8]/16.0 % 0.4

    def getPlanetRadius(self):
        return (self.seed.total % 20) + 4

    def getLandMassCount(self):
        landCountSeedIndex = self.seed.values[self.seed.total % 16]
        landCount = 0
        if landCountSeedIndex % 2:
            landCount = (self.seed.total % landCountSeedIndex)
        return landCount

    def createLandMassPatterns(self):
        lands = []

        for i in range(0, self.landCount):
            index1 = self.seed.values[i]
            index2 = self.seed.values[(index1*index1) % 16]
            landSteps = ((self.seed.total % 16) % index2) + 2
            land = [(((self.seed.values[self.seed.total % 16]) % (step + 1)) % 8) - 3 for step in range(0, landSteps)]

            xPercent = float(((index2 + 1.0) / ((index1*index2 % 16) + 1.0))) % 1.0
            yPercent = float(((index1 + 1.0) / ((index1*index2 % 16) + 1.0))) % 1.0

            landx = self.box[0] + int(self.r*2 * xPercent)
            landy = self.box[1] + int(self.r*2 * yPercent)
            landr = ((self.box[0] * int(100 * xPercent) * int(100 * yPercent)) % index1) + 1
            lands.append([landx, landy, landr] + land)

        return lands

    def createShadows(self):
        shadow1 = (self.box[0]+self.box[0]/8, self.box[1]+self.box[1]/8, self.box[2]-self.box[0]/4, self.box[3]-self.box[0]/4)
        shadow2 = (self.box[0]+self.box[0]/4, self.box[1]+self.box[1]/4, self.box[2]-self.box[0]/2.5, self.box[3]-self.box[0]/2)
        return [shadow1, shadow2]
