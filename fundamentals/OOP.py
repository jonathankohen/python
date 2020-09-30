class House:
    def __init__(self, numGarages, dogName):
        # attributes
        self.numLivingRooms = 1
        self.numBaths = 3
        self.numBedrooms = 4
        self.numBackyard = 1
        self.garageCount = numGarages
        self.nameOfOwner = dogName
        self.solarPanels = 0

    def addSolarPower(self, amount):
        self.solarPanels += amount
        return self

    def changeDogName(self, dogName):
        self.nameOfOwner = dogName
        return self

# self = "this", refers to the object itself
# when house object is called, self is the name of the object "house1, house 2, etc."
# need to add return self into new methods if you want to chain them. never in init method. only if nothing else to return


# instances of the House class/AKA House objects
house1 = House(2, "Junior")
house2 = House(0, "Jeff")
house3 = House(1, "Rover")
house4 = House(2, "Beamer")

# house1.garageCount = 4
# print(house1.garageCount)

house1.addSolarPower(3).addSolarPower(4).changeDogName('Lily').addSolarPower(5)
print(house1.solarPanels)
print(house1.nameOfOwner)
