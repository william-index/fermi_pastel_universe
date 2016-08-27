#!/usr/bin/python

"""
Generates Planet Data and details from seed
"""
class Planet:
    def __init__(self, seed, canvas):
        self.seed = seed
        self.canvas = canvas

        self.r = self.getPlanetRadius()
        self.box = (canvas[0]/2-self.r, canvas[1]/2-self.r, canvas[0]/2+self.r, canvas[1]/2+self.r)
        self.landCount = self.getLandMassCount()
        self.lands = self.createLandMassPatterns()

        self.shadows = self.createShadows()
        self.shadowIntensity = self.seed.values[8]/16.0 % 0.4

        self.moons = self.generateMoons()
        self.rings = self.generateRings()

        # colorsys
        self.ringColor = (0,0,255,200)

    def generateRings(self):
        values = self.seed.values
        box = self.box
        rings = []

        if self.seed.total % 2:
            numRings = self.seed.total % 8
            ringSizes = [((values[16-ring-1] + (values[16-ring-1] % 2))*11)%24 for ring in range(0, numRings)]
            print ringSizes

            for ringSize in ringSizes:
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
