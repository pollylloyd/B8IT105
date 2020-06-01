# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:44:09 2020

@author: P Lloyd 10525563 - CA3 - Calculator
"""

import unittest

from CA3_Calculator_PLloyd import Calculator

values = [2,5,10,8,-5,-3,1.1]

class testCalculator(unittest.TestCase):
    def setUp(self): # built in function
        self.calc = Calculator() # created a instance of Calculator into test class
        
    def test_sum_all(self): 
        self.assertEqual(18.1, self.calc.sum_all(values)) 

    def test_multiply(self):
        self.assertEqual(13200.000000000002, self.calc.multiply(values)) 
        
    def test_divide(self):
        self.assertEqual(0.000303030303030303, self.calc.divide(values)) 
        
    def test_max(self):
        self.assertEqual(10, self.calc.max_val(values)) 
        
    def test_min(self):
        self.assertEqual(-5, self.calc.min_val(values)) 
        
    def test_square(self):
        self.assertEqual([4, 25, 100, 64, 25, 9, 1.2100000000000002], self.calc.square(values)) 
        
    def test_cube(self):
        self.assertEqual([8, 125, 1000, 512, -125, -27, 1.3310000000000004], self.calc.cube(values)) 
        
    def test_odd(self):
        self.assertEqual([5, -5, -3], self.calc.odd(values)) 
        
    def test_even(self):
        self.assertEqual([2, 10, 8], self.calc.even(values)) 
        
    def test_circle_area(self):
        self.assertEqual([12.566370614359172, 78.53981633974483, 314.1592653589793, 201.06192982974676, 3.8013271108436504], self.calc.circle_area(values)) 
        
if __name__ == '__main__':
    unittest.main()
       