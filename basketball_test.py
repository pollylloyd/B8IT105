# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:46:32 2020

@author: Owner
"""


import unittest

import Basketball

class testBasketball(unittest.TestCase):
    
    def setUp(self):
        self.contents = Basketball.get_page_contents()
    
    def test_get_page_contents(self):
        self.assertTrue(len(self.contents) >0)
    
    def test_convert_to_soup(self):
        self.assertTrue(Basketball.convert_to_soup(self.contents) is not None)


if __name__ == '__main__':
    unittest.main()