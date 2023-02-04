# -*- coding: utf-8 -*-
"""
Updated Feb 4, 2023
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Arun Rao Nayineni
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(7, 7, 7), 'Equilateral', '7,7,7 should be equilateral')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene', '10,11,12 should be Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(100, 110, 112), 'Scalene', '100,110,112 should be Scalene triangle')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isosceles', '5,5,3 should be a Isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(4, 6, 6), 'Isosceles', '4,6,6 should be a Isosceles')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(8, 6, 8), 'Isosceles', '8,6,8 should be a Isosceles')

    def testIsoscelesTriangleD(self):
        self.assertEqual(classifyTriangle(6, 6, 4), 'Isosceles', '6,6,4 should be a Isosceles')

    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(-1, -1, -1), 'InvalidInput', '-1,-1,-1 is InvalidInput')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(201, 201, 201), 'InvalidInput', '201,201,201 is InvalidInput')

    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle("200", "200", "200"), 'InvalidInput', '200,200,200 is InvalidInput')

    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(1, 3, 5), 'NotATriangle', '1,3,5 NotATriangle')

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(1, 4, 5), 'NotATriangle', '1,4,5 NotATriangle')

    def testNotATriangle3(self):
        self.assertEqual(classifyTriangle(1, 17, 5), 'NotATriangle', '1,17,5 NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
