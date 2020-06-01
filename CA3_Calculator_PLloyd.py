# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:31:50 2020

@author: CA3 - Calculator
"""
#10 Functional Calculator with Map Reduce Filter & Generator

#For assignment 3 create a Calculator class and CalculatorTest 
#class that will implement functionality from a calculator using 
#lists. Each function should use the lessons learned in the map, 
#reduce, filter, and generator lecture.


#***************


from functools import reduce
import math
math.pi

class Calculator(object): # object is assumed, but written for clarity

    
## USING REDUCE FUNCTION - reduces a list to a single value, a single result
## takes 2 args, can use lambda
## syntax: r = reduce(func, seq)
    
    def sum_all(self, values): # self is assumed, but written for clarity
        return reduce(lambda x, y: x+y, values)
    ## print(reduce(lambda x, y: x+y, [47, 11, 42, 13])) - sumall can be used for add and subtract
    ## what its doing: takes 47 + 11 = 48 - redfines x, then adds to y = 42 = 100, those become
    ## x then add to y = 13 RETURNS 113
    
    def multiply(self, values):
        return reduce(lambda x, y: x*y, values)   

    def divide(self, values):
        return reduce(lambda x, y: x/y, values)

    def max_val(self, values):
        return reduce(lambda x,y: x if (x>y) else y, values) 
## f = lambda x,y: x if (x>y) else y
## print (reduce(f, [47, 11, 42, 13]))
##what it's doing, returning the max figure:
##it'll take 47 and 11, because 47 is greater than b, will
##return 47, then the next figure, 47 greater than 42, so 47, etc.

    def min_val(self, values):
        return reduce(lambda x,y: x if (x<y) else y, values) 
## f = lambda x,y: x if (x<y) else y
## print (reduce(f, [47, 11, 42, 13]))
## what it's doing, returning the min figure:
## it'll take 47 and 11, because 47 is greater than b, will
## return b = 11, then the next figure, 11 less than 42, so 11, etc.
## test above with 1 line of code:
## return reduce(lambda a, b: a if (a<b) else b, [47, 11, 42, 13])
## print(reduce(lambda a, b: a if (a<b) else b, [47, 11, 42, 13]))

##  USING LIST AND MAP
    def square(self, values):
        return list(map(lambda x:x*x, values))
      
    def cube(self, values):
        # Get new sequence which is the cube of values in a sequence.
        return list(map(lambda x: x ** 3, values))                 
##  USING FILTER Function
## Can use lambda - filter applies true/false comp. to each item in list - 
## filter out some things from the new result list
## Return only the odd no: Use x % 2 - divisable by 2 with remainder zero
##(note ==1 is optional notation, will assume TRUE)
    def even(self, values):
        return list(filter(lambda x: x % 2 ==0, values)) 
    
    def odd(self, values):
        return list(filter(lambda x: x % 2 ==1, values)) 

## USING LIST COMPREHENSION - find area of a circle
    def circle_area(self, values): 
        return [math.pi*x**2 for x in values if x > 0] 

     
   
def operator_menu():
    print('1 or + or - for the sum of all values')
    print('2 or * for multiplication')
    print('3 or / for division')
    print('4 or max for max')   
    print('5 or min for min')
    print('6 or sq to square the number')   
    print('7 or cub to cube the number')   
    print('8 or even to filter all the even numbers')
    print('9 or odd to filter all the odd numbers')
    print('10 or a for the area of a circle')


def process_operation():     
    operator_menu()
    func = input('Enter operator from list above: (use lower case for characters)   ')        
    if func not in ['1', '+', '-', '2','*','3', \
                     '/', '4', 'max', '5','min','6', 'sq', '7', \
                     'cub', '8', 'even', '9', 'odd', '10', 'c']:
        print('That selection is not a valid operation!') 
    else:
        values = list(map(eval,input('Please input a range of numbers separated by comma   ' ).split(",")))        
    
    calc = Calculator() # create an instance and then call that instance (below), alternatively, Calculator().defname
    
    if func in ['1', '+', '-']:
        print  ('Sum result   ', calc.sum_all(values))
        
    elif func in ['2', '*']:
        print  ('Multiplication result   ', calc.multiply(values))
  
    elif func in ['3', '/']:
        print  ('Divide result   ', calc.divide(values))  
      
    elif func in ['4', 'max']:
        print  ('Max result   ', calc.max_val(values))
         
    elif func in ['5', 'min']:
        print  ('Min result   ', calc.min_val(values))
        
    elif func in ['6', 'sq']:
        print  ('Square result   ', calc.square(values))
        
    elif func in ['7', 'cub']:
        print  ('Cubed result   ', calc.cube(values))
        
    elif func in ['8', 'even']:
        print  ('Result of all the even numbers in the list...', calc.even(values))

    elif func in ['9', 'odd']:
        print  ('Result of all the odd numbers in the list   ', calc.odd(values))   
        
    elif func in ['10', 'c']:
        print  ('Area of the circle, given radius   ', calc.circle_area(values))  
      

def main():
    repeat_calc = ''
    while repeat_calc != 'n':
        process_operation()
        repeat_calc = input('Would you like to continue? (Press any key to \
                                                       continue or n to exit) ')

if __name__ == '__main__': # to run from command line, where,  if name input == main, then run main function
    main()   

