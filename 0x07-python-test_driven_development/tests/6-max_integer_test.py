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
        arr = [1, 2, 3, 4]
        self.assertEqual(max_integer(arr), 4)

        arr = [0, 23, 45, 55]
        self.assertEqual(max_integer(arr), 55)

        arr = [None]
        self.assertEqual(max_integer(arr), None)

        arr = []
        self.assertEqual(max_integer(arr), None)

        arr = [7, 1, 2, 3]
        self.assertEqual(max_integer(arr), 7)

        arr = [-1, -2, -3, -5]
        self.assertEqual(max_integer(arr), -1)

        arr = [100]
        self.assertEqual(max_integer(arr), 100)

        arr = [10, 20, 30, 40, 50, 102, 60, 75, 85, 95, 101]
        self.assertEqual(max_integer(arr), 102)


if __name__ == "__main__":
    unittest.main()
