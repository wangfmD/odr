# coding: utf-8
import unittest


class TT(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(1, True)

    def test_2(self):
        self.assertEqual(1,True)

if __name__ == '__main__':
    unittest.main()
