# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:19:21 2020
CA2 - Car App
@author: P Lloyd
"""

# Define a class for my car - OBJECT ORIENTED PROGRAMMING
#classes, def and membervars

class Car(object):  # BASE CLASS - this is the blue print
    # GOOD PRACTISE to call this 'object' in parenthesis, but if blank - python knows it's an object
    # implement the car object.
    # Classes names start UC
    # Modules start LC
    # def names start LC
    
    def __init__(self): # TAKES ONE PARAMETER - CALLING THIS 'SELF' AS IS 
        #CONVENTION - THEN BELOW EACH INSTANCES HAS A NAME ATTRIBUTE, COLOUR, MAKE ETC.
        #store the variables
        #setting member variables
        self.__registration = ''
        self.__colour = '' ##__DENOTES IT'S PRIVATE/HIDDEN 
        self.__make = ''   ## __PRIVATE - OUTPUT IT, PRINT - IT'LL SAY IT HAS NO ATTRIBUTE
        self.__model = '' ## __PRIVATE
        self.__km = 0 ## __PRIVATE - KM SET TO 0 AS DEFAULT
        self.__forHire = 'Y'
        
    def setRegistration(self, registration): # HAS TWO PARAMS
        self.__registration = registration
    
    def getRegistration(self):
        return self.__registration
    
    def setColour(self, colour): # HAS TWO PARAMS
        self.__colour = colour
        
    def getColour(self): # HAS ONE PARAM
        return self.__colour
        # CLASS CREATED WITH 4 VARS - 3 PRIVATE - FOR PRIVATE - 
        #HAS TO PUT IN GETTERS AND SETTERS
        #CREATE THE INSTANCE - GET DEFAULT VALS, UPDATE VALUES, 
        #THEN PROVE THEY'VE UPDATED CORRECTED    
    
    def setMake(self, make):
        self.__make = make         

    def getMake(self):
        return self.__make
    
    def setModel(self, model):
        self.__model = model
        
    def getModel(self):
        return self.__model
    
    def setKm(self, km):
        self.__km = km  
    
    def getKm(self):
        return self.__km
    
    def setForHire(self, forHire):
        self.__forHire = forHire

    def getForHire(self):
        return self.__forHire

#add some behaviours/actions
    def move(self, distance):
        print('Km travelled this hire:' + str(distance) + 'Kms')
        self.__km += distance

    def paint(self, colour):
        print('Car has been painted' + colour)
        self.__colour = colour
        return colour

    def status(self, forHire):
        print('Is this car available for hire? ' +str(forHire))
        self.__forHire = forHire
        return forHire

# create an instance of the class to test
#car1 = Car()
#
#print(car1.getRegistration())
#print(car1.getColour())
#print(car1.getMake())
#print(car1.getModel())
#print(car1.getKm())
#print(car1.getForHire())

#set some new values to the parameters to test

#car1.setRegistration('18-D-4938')
#car1.setColour('Platinum grey metallic')
#car1.setMake('Volkswagon')
#car1.setModel('Passat')
#car1.setKm(100)
#car1.setForHire('N')

#test - print out new values to prove they've updated
#print(car1.getRegistration())
#print(car1.getColour())
#print(car1.getMake())
#print(car1.getModel())
#print(car1.getKm())
#print(car1.getForHire())
#
##update the km, paint colour and status - after adding the behaviours (above)
#car1.move(5)
#car1.paint('Deep black pearl')
#car1.status('Y')
##test - print out the new values to prove they're updated
#
#print(car1.getRegistration())
#print(car1.getColour())
#print(car1.getMake())
#print(car1.getModel())
#print(car1.getKm())
#print(car1.getForHire())


## Create subclasses

class ElectricCar(Car): # electric car calls/extends the Car class
    #Car is the class we are inheriting 
    #then list the things that are DIFFERENT into the subclass -
    #all things to common to all cars will be in main class
    def __init(self):
        super().__init__() # code allows to call from multiple objects inclc Car class, instead of 
                            #Car.__init__(self)
        self.__numberFuelCells = '' #default value blank
    
    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value
    
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    

class PetrolCar(Car):
    def __init(self):
        super().__init__() 
        self.__transmission = 'M' # set as M for Manual as default as most are manual
        self.__engineSize = ''

    def setTransmission(self, transmission):
        self.__transmission = transmission
    
    def getTransmission(self):
        return self.__transmission

    def setEngineSize(self, size):
        self.__engineSize = size      

    def getEngineSize(self):
        return self.__engineSize
    

class HybridCar(Car):
    def __init__(self):
        super().__init__()
        self.__fuelTankCapacity = ''
        
    def setFuelTankCapacity(self, fuelTankCapacity):
        self.__fuelTankCapacity = fuelTankCapacity
        
    def getFuelTankCapacity(self):
        return self.__fuelTankCapacity 

      
class DieselCar(Car): 
    def __init(self):
        super().__init__() 
        self.__transmission = 'M' # set as M for Manual as default as most are manual
        self.__engineSize = ''

    def setTransmission(self, transmission):
        self.__transmission = transmission
    
    def getTransmission(self):
        return self.__transmission

    def setEngineSize(self, enginesize):
        self.__engineSize = enginesize      

    def getEngineSize(self):
        return self.__engineSize


# check that the subclasses are functioning - with specific subclass 
#vars and also those from default in  Superclass
#ecar1 = ElectricCar()
#hcar1 = HybridCar()
#dcar1 = DieselCar()
#pcar1 = PetrolCar()
#
#ecar1.setNumberFuelCells(2)
#ecar1.setForHire('N')
#hcar1.setFuelTankCapacity(57)
#dcar1.setTransmission('A')
#dcar1.setEngineSize(1.6)
#pcar1.setTransmission('A')
#pcar1.setEngineSize(2)
#
#print(ecar1.getNumberFuelCells())
#print(ecar1.getForHire())
#print(hcar1.getFuelTankCapacity())
#print(dcar1.getTransmission())
#print(dcar1.getEngineSize())
#print(pcar1.getTransmission())
#print(pcar1.getEngineSize())


