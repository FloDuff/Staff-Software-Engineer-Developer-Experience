import unittest
from main import sort, ResultStack

class TestSortLogic(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(10, 10, 10, 10), ResultStack.STANDARD)

    def test_heavy_only(self):
        self.assertEqual(sort(10, 10, 10, 25), ResultStack.SPECIAL)

    def test_bulky_only(self):
        self.assertEqual(sort(200, 10, 10, 10), ResultStack.SPECIAL)

    def test_both_rejected(self):
        self.assertEqual(sort(200, 200, 200, 50), ResultStack.REJECTED)
