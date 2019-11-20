import unittest
from lesson5.exercise import chop, get_roman_numeral

class ChopCase(unittest.TestCase):
    def test_chop(self):
        self.assertEqual(-1, chop(3, []))
        self.assertEqual(-1, chop(3, [1]))
        self.assertEqual(0,  chop(1, [1]))
        self.assertEqual(0,  chop(1, [1, 3, 5]))
        self.assertEqual(1,  chop(3, [1, 3, 5]))
        self.assertEqual(2,  chop(5, [1, 3, 5]))
        self.assertEqual(-1, chop(0, [1, 3, 5]))
        self.assertEqual(-1, chop(2, [1, 3, 5]))
        self.assertEqual(-1, chop(4, [1, 3, 5]))
        self.assertEqual(-1, chop(6, [1, 3, 5]))
        self.assertEqual(0,  chop(1, [1, 3, 5, 7]))
        self.assertEqual(1,  chop(3, [1, 3, 5, 7]))
        self.assertEqual(2,  chop(5, [1, 3, 5, 7]))
        self.assertEqual(3,  chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(8, [1, 3, 5, 7]))

class RomanNumeralsConvertToRomanTests(unittest.TestCase):
    def test_one(self):
        result = get_roman_numeral(1)
        self.assertEqual('I', result)

    def test_ten(self):
        result = get_roman_numeral(10)
        self.assertEqual('X', result)

    def test_five(self):
        result = get_roman_numeral(5)
        self.assertEqual('V', result)

    def test_seven(self):
        result = get_roman_numeral(7)
        self.assertEqual('VII', result)

    def test_sixteen(self):
        result = get_roman_numeral(16)
        self.assertEqual('XVI', result)

    def test_twenty_eight(self):
        result = get_roman_numeral(28)
        self.assertEqual('XXVIII', result)

    def test_four(self):
        result = get_roman_numeral(4)
        self.assertEqual('IV', result)

    def test_four(self):
        result = get_roman_numeral(9)
        self.assertEqual('IX', result)

    def test_thirty_nine(self):
        result = get_roman_numeral(39)
        self.assertEqual('XXXIX', result)

    def test_thirty_four(self):
        result = get_roman_numeral(34)
        self.assertEqual('XXXIV', result)

    def test_fifty(self):
        result = get_roman_numeral(50)
        self.assertEqual('L', result)

    def test_fifty_nine(self):
        result = get_roman_numeral(59)
        self.assertEqual('LIX', result)

    def test_one_hundred(self):
        result = get_roman_numeral(100)
        self.assertEqual('C', result)

    def test_five_hundred(self):
        result = get_roman_numeral(500)
        self.assertEqual('D', result)

    def test_one_thousand(self):
        result = get_roman_numeral(1000)
        self.assertEqual('M', result)

    def test_eighty_eight(self):
        result = get_roman_numeral(88)
        self.assertEqual('LXXXVIII', result)

    def test_eighty_nine(self):
        result = get_roman_numeral(89)
        self.assertEqual('LXXXIX', result)

    def test_negative_number(self):
        with self.assertRaises(TypeError):
            result = get_roman_numeral(-1)

    def test_none(self):
        with self.assertRaises(TypeError):
            result = get_roman_numeral(None)


    def test_empty_string(self):
        with self.assertRaises(TypeError):
            result = get_roman_numeral('')

    def test_zero(self):
        with self.assertRaises(TypeError):
            result = get_roman_numeral(0)

    def test_alphacharacter(self):
        with self.assertRaises(TypeError) as e:
            result = get_roman_numeral('test')
        self.assertEqual('The value you entered is invalid: {num} is not a positive integer.'.format(num='test'),
                         str(e.exception))

    def test_nineteen(self):
        result = get_roman_numeral(19)
        self.assertEqual('XIX', result)

    def test_ninety(self):
        result = get_roman_numeral(90)
        self.assertEqual('XC', result)

    def test_fourty(self):
        result = get_roman_numeral(40)
        self.assertEqual('XL', result)

    def test_four_hundred_and_fourty_eight(self):
        result = get_roman_numeral(448)
        self.assertEqual('CDXLVIII', result)

    def test_nineteen_eighty_nine(self):
        result = get_roman_numeral(1989)
        self.assertEqual('MCMLXXXIX', result)

    def test_nine_hundred_and_ninety(self):
        result = get_roman_numeral(990)
        self.assertEqual('CMXC', result)

    def test_nineteen_ninety(self):
        result = get_roman_numeral(1990)
        self.assertEqual('MCMXC', result)

    def test_nineteen_ninety_nine(self):
        result = get_roman_numeral(1999)
        self.assertEqual('MCMXCIX', result)

    def test_two_thousand_and_eight(self):
        result = get_roman_numeral(2008)
        self.assertEqual('MMVIII', result)

    def test_two_thousand_nine_hundred_and_ninety(self):
        result = get_roman_numeral(2990)
        self.assertEqual('MMCMXC', result)

    def test_two_thousand_nine_hundred_and_ninety_nine(self):
        result = get_roman_numeral(2999)
        self.assertEqual('MMCMXCIX', result)

    def test_two_thousand_four_hundred_and_fourty_four(self):
        result = get_roman_numeral(2444)
        self.assertEqual('MMCDXLIV', result)

    def test_three_thousand(self):
        result = get_roman_numeral(3000)
        self.assertEqual('MMM', result)

    def test_five_thousand_four_hundred_and_ninety_four(self):
        result = get_roman_numeral(5494)
        self.assertEqual('MMMMMCDXCIV', result)

if __name__ == '__main__':
    unittest.main()