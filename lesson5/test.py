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
    def test_01_one(self):
        result = get_roman_numeral(1)
        self.assertEqual('I', result)

    def test_02_ten(self):
        result = get_roman_numeral(10)
        self.assertEqual('X', result)

    def test_03_five(self):
        result = get_roman_numeral(5)
        self.assertEqual('V', result)

    def test_04_seven(self):
        result = get_roman_numeral(7)
        self.assertEqual('VII', result)

    def test_05_sixteen(self):
        result = get_roman_numeral(16)
        self.assertEqual('XVI', result)

    def test_06_twenty_eight(self):
        result = get_roman_numeral(28)
        self.assertEqual('XXVIII', result)

    def test_07_four(self):
        result = get_roman_numeral(4)
        self.assertEqual('IV', result)

    def test_08_nine(self):
        result = get_roman_numeral(9)
        self.assertEqual('IX', result)

    def test_09_thirty_nine(self):
        result = get_roman_numeral(39)
        self.assertEqual('XXXIX', result)

    def test_10_thirty_four(self):
        result = get_roman_numeral(34)
        self.assertEqual('XXXIV', result)

    def test_11_fifty(self):
        result = get_roman_numeral(50)
        self.assertEqual('L', result)

    def test_12_fifty_nine(self):
        result = get_roman_numeral(59)
        self.assertEqual('LIX', result)

    def test_13_one_hundred(self):
        result = get_roman_numeral(100)
        self.assertEqual('C', result)

    def test_14_five_hundred(self):
        result = get_roman_numeral(500)
        self.assertEqual('D', result)

    def test_15_one_thousand(self):
        result = get_roman_numeral(1000)
        self.assertEqual('M', result)

    def test_16_eighty_eight(self):
        result = get_roman_numeral(88)
        self.assertEqual('LXXXVIII', result)

    def test_17_eighty_nine(self):
        result = get_roman_numeral(89)
        self.assertEqual('LXXXIX', result)

    def test_18_negative_number(self):
        with self.assertRaises(TypeError):
            result = get_roman_numeral(-1)

    def test_19_none(self):
        with self.assertRaises(TypeError):
            result = get_roman_numeral(None)

    def test_20_empty_string(self):
        with self.assertRaises(TypeError):
            result = get_roman_numeral('')

    def test_21_zero(self):
        with self.assertRaises(TypeError):
            result = get_roman_numeral(0)

    def test_22_alphacharacter(self):
        with self.assertRaises(TypeError) as e:
            result = get_roman_numeral('test')
        self.assertEqual('The value you entered is invalid: {num} is not a positive integer.'.format(num='test'),
                         str(e.exception))

    def test_23_nineteen(self):
        result = get_roman_numeral(19)
        self.assertEqual('XIX', result)

    def test_24_ninety(self):
        result = get_roman_numeral(90)
        self.assertEqual('XC', result)

    def test_25_fourty(self):
        result = get_roman_numeral(40)
        self.assertEqual('XL', result)

    def test_26_four_hundred_and_fourty_eight(self):
        result = get_roman_numeral(448)
        self.assertEqual('CDXLVIII', result)

    def test_27_nineteen_eighty_nine(self):
        result = get_roman_numeral(1989)
        self.assertEqual('MCMLXXXIX', result)

    def test_28_nine_hundred_and_ninety(self):
        result = get_roman_numeral(990)
        self.assertEqual('CMXC', result)

    def test_29_nineteen_ninety(self):
        result = get_roman_numeral(1990)
        self.assertEqual('MCMXC', result)

    def test_30_nineteen_ninety_nine(self):
        result = get_roman_numeral(1999)
        self.assertEqual('MCMXCIX', result)

    def test_31_two_thousand_and_eight(self):
        result = get_roman_numeral(2008)
        self.assertEqual('MMVIII', result)

    def test_32_two_thousand_nine_hundred_and_ninety(self):
        result = get_roman_numeral(2990)
        self.assertEqual('MMCMXC', result)

    def test_33_two_thousand_nine_hundred_and_ninety_nine(self):
        result = get_roman_numeral(2999)
        self.assertEqual('MMCMXCIX', result)

    def test_34_two_thousand_four_hundred_and_fourty_four(self):
        result = get_roman_numeral(2444)
        self.assertEqual('MMCDXLIV', result)

    def test_35_three_thousand(self):
        result = get_roman_numeral(3000)
        self.assertEqual('MMM', result)

    def test_36_five_thousand_four_hundred_and_ninety_four(self):
        result = get_roman_numeral(5494)
        self.assertEqual('MMMMMCDXCIV', result)

if __name__ == '__main__':
    unittest.main()