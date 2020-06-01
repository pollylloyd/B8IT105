# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:19:21 2020
CA2 - Car App
@author: P Lloyd
"""


from CA2_Cars_PLloyd import Car, ElectricCar, PetrolCar,  HybridCar, DieselCar

class Fleet(object):
    def __init__(self): # create lists for each of the following car types
        self.__electric_cars = []
        self.__petrol_cars = []
        self.__diesel_cars = []
        self.__hybrid_cars = []


    def create_inventory(self):  # set the number of each of the car types
        for i in range(1, 7):
           self.__electric_cars.append(ElectricCar())
        for i in range(1, 21):
           self.__petrol_cars.append(PetrolCar())
        for i in range(1, 11):
            self.__diesel_cars.append(DieselCar())
        for i in range(1, 5):
            self.__hybrid_cars.append(HybridCar())
       
    def getElectricCar(self):
        return self.__electric_cars
     
    def getPetrolCar(self):
        return self.__petrol_cars
         
    def getDieselCar(self):
        return self.__diesel_cars
       
    def getHybridCar(self):
        return self.__hybrid_cars
    

    def check_stock_level(self): # return the stock level of each car type (- Hires, + Returns)
        print('Electric cars stock level: ' + str(len(self.getElectricCar())))  
        print('Petrol cars stock level ' + str(len(self.getPetrolCar())))  
        print('Diesel cars stock level: ' + str(len(self.getDieselCar())))  
        print('Hybrid cars stock level: ' + str(len(self.getHybridCar()))) 
 

    def save_data(self): # save to a csv file 
        csv_file = open('DBSCarRental.csv', 'w')
        csv_file.write('Electric,' + str(len(self.__electric_cars)) + '\n')
        csv_file.write('Petrol,' + str(len(self.__petrol_cars)) + '\n')
        csv_file.write('Hybrid,' + str(len(self.__hybrid_cars)) + '\n')
        csv_file.write('Diesel,' + str(len(self.__diesel_cars)) + '\n')
        csv_file.close()
        print('Your changes have been saved')
        
    def hireCar(self, cartype):
        if cartype == 'E' or cartype == 'e':            
            return self.__electric_cars.pop() # pop removes the last value from this list
        elif cartype == 'P' or cartype == 'p':            
            return self.__petrol_cars.pop()
        elif cartype == 'D' or cartype == 'd':            
            return self.__diesel_cars.pop()
        elif cartype == 'H' or cartype == 'h':            
            return self.__hybrid_cars.pop()
        

    def returnCar(self, cartype, car):
        if cartype == 'E' or cartype == 'e':
            self.__electric_cars.append(car) # adds the vehicle back to the list
        elif cartype == 'P' or cartype == 'p':
            self.__petrol_cars.append(car)
        elif cartype == 'D' or cartype == 'd':
            self._diesel_cars.append(car)
        elif cartype == 'H' or cartype == 'h':
            self.__hybrid_cars.append(car)

 
    def mainMenu(self):
        print('Welcome to DBS Car Rental')
        self.check_stock_level()
        rentedCar = None
        msg = 'Please select H to Hire a car or R to return a car, or any key to return to main menu: '
        answer = input(msg)
        while answer == 'H' or answer == 'R' or answer == 'h' or answer == 'r':
            if answer == 'H' or answer == 'h':
                cartype = input('Please select your choice of car - P for petrol, D for diesel, E for electric, H for hybrid:  ').upper()
                rentedCar = self.hireCar(cartype)
                print('Hire')
            elif answer == 'R' or answer == 'r':
                cartype = input('Please select your choice of car - P for petrol, D for diesel, E for electric, H for hybrid:  ').upper()
                self.returnCar(cartype, rentedCar)   
                print('return')
            self.check_stock_level()
            answer = input(msg)


if __name__ == '__main__':
    DBSCarRental = Fleet()
    DBSCarRental.create_inventory()
    proceed = 'y'
    while proceed.lower() == 'y':
        DBSCarRental.mainMenu()
        proceed = input('Would you like to continue? Please select y to continue or n to exit:   ')
    DBSCarRental.save_data()