import unittest
from lesson7.exercise import sum_of_intervals

class SumIntevalCase(unittest.TestCase):
    def test_sumInterval(self):
        self.assertEqual(sum_of_intervals([(1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 5), (6, 10)]), 8)
        self.assertEqual(sum_of_intervals([(1, 5), (1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)

if __name__ == '__main__':
    unittest.main()