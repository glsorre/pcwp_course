import unittest
from math import factorial
from timeit import timeit
from functools import lru_cache
from lesson2.exercise import arithtmetic, memoize
from lesson2.exercise import factorial as factorial_mine

class TestArithmetic(unittest.TestCase):
  def test_1_1(self):
    result = arithtmetic(1,1)
    self.assertDictEqual(result, {
      "sum": 2,
      "product": 1,
      "division": 1,
      "remainder": 0
    })

  def test_2_2(self):
    result = arithtmetic(2,2)
    self.assertDictEqual(result, {
      "sum": 4,
      "product": 4,
      "division": 1,
      "remainder": 0
    })

  def test_1000_1(self):
    result = arithtmetic(1000,1)
    self.assertDictEqual(result, {
      "sum": 1001,
      "product": 1000,
      "division": 1000,
      "remainder": 0
    })

  def test_2_3(self):
    result = arithtmetic(2,3)
    self.assertDictEqual(result, {
      "sum": 5,
      "product": 6,
      "division": 0.6666666666666666,
      "remainder": 2
    })

class TestFactorial(unittest.TestCase):
  def test_factorial(self):
    factorial1 = factorial(1)
    factorial5 = factorial(5)
    factorial10 = factorial(10)
    factorial1_mine = factorial_mine(1)
    factorial5_mine = factorial_mine(5)
    factorial10_mine = factorial_mine(10)
    self.assertEqual(factorial1, factorial1_mine)
    self.assertEqual(factorial5, factorial5_mine)
    self.assertEqual(factorial10, factorial10_mine)

class TestMemoization(unittest.TestCase):
  def test_memoization(self):
    factorial_with_cache = memoize(factorial)

    @lru_cache
    def factorial_with_rlu(n):
      factorial(n)

    def code_without():
      factorial(1000)

    def code():
      factorial_with_cache(1000)

    def code_with_lru():
      factorial_with_rlu(1000)

    result_without = timeit(code_without, number=10000)
    result_with = timeit(code, number=10000)
    result_with_lru = timeit(code_with_lru, number=10000)

    print(f"Tempo senza cache {result_without}. Tempo con cache {result_with}. Tempo con python decorator {result_with_lru}")
    self.assertGreater(result_without, result_with)

if __name__ == '__main__':
  unittest.main()