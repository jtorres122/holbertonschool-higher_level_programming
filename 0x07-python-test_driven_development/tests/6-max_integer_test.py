#!/usr/bin/python3
'''
Module contains unit test for function max_integer
'''

import unittest
max_integer = __import__('6-max_integer').max_integer

class max_integer_test(unittest.TestCase):
    ''' Class tests max integer function '''

    def test_max(self):
        '''comment'''
        l = [1, 2, 3, 4]
        self.assertEqual(max_integer(l), 4)

        l = [0, 23, 45, 55]
        self.assertEqual(max_integer(l), 55)

        l = [None]
        self.assertEqual(max_integer(l), None)

        l = []
        self.assertEqual(max_integer(l), None)

        l = [7, 1, 2, 3]
        self.assertEqual(max_integer(l), 7)

        l = [-1, -2, -3, -5]
        self.assertEqual(max_integer(l), -1)

        l = [100]
        self.assertEqual(max_integer(l), 100)

        l = [10, 20, 30, 40, 50, 102, 60, 75, 85, 95, 101]
        self.assertEqual(max_integer(l), 102)

if __name__ == "__main__":
    unittest.main()

