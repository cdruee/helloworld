#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


class Test_dummy(unittest.TestCase):
    """
    always passes
    """
    def test_1(self):
        a = 1
        self.assertEqual(a, 1)


if __name__ == '__main__':
    unittest.main()
