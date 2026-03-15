import unittest
from main import sort, ResultStack

class TestPackageSorter(unittest.TestCase):

    def test_standard_package(self):
        """Standard packages are neither bulky nor heavy."""
        self.assertEqual(sort(10, 10, 10, 5), ResultStack.STANDARD)

    def test_bulky_by_volume(self):
        """Volume exactly 1,000,000 should be bulky (SPECIAL)."""
        self.assertEqual(sort(100, 100, 100, 10), ResultStack.SPECIAL)

    def test_bulky_by_dimension(self):
        """One dimension >= 150 should be bulky (SPECIAL)."""
        self.assertEqual(sort(150, 10, 10, 5), ResultStack.SPECIAL)

    def test_heavy_package(self):
        """Mass >= 20 should be heavy (SPECIAL)."""
        self.assertEqual(sort(10, 10, 10, 20), ResultStack.SPECIAL)

    def test_rejected_package(self):
        """Both heavy and bulky should be REJECTED."""
        self.assertEqual(sort(150, 150, 150, 50), ResultStack.REJECTED)

    def test_edge_cases(self):
        """Test exactly on the boundary lines."""
        # Exactly 20kg, not bulky -> SPECIAL
        self.assertEqual(sort(10, 10, 10, 20), ResultStack.SPECIAL)
        # Exactly 150cm dimension, not heavy -> SPECIAL
        self.assertEqual(sort(150, 10, 10, 5), ResultStack.SPECIAL)

if __name__ == '__main__':
    unittest.main()
