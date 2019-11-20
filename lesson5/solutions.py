def chop(element, array):
    if element in array:
        return array.index(element)
    return -1

def get_roman_numeral(number):
    result = ''

    roman = [
        {
            'limit': 1000,
            'method': 'repeat',
            'letter': "M"
        },
        {
            'limit': 900,
            'method': 'unique',
            'letter': "CM"
        },
        {
            'limit': 500,
            'method': 'unique',
            'letter': "D"
        },
        {
            'limit': 400,
            'method': 'unique',
            'letter': "CD"
        },
        {
            'limit': 100,
            'method': 'repeat',
            'letter': "C"
        },
        {
            'limit': 90,
            'method': 'unique',
            'letter': "XC"
        },
        {
            'limit': 50,
            'method': 'unique',
            'letter': "L"
        },
        {
            'limit': 40,
            'method': 'unique',
            'letter': "XL"
        },
        {
            'limit': 10,
            'method': 'repeat',
            'letter': "X"
        },
        {
            'limit': 9,
            'method': 'unique',
            'letter': "IX"
        },
        {
            'limit': 5,
            'method': 'unique',
            'letter': "V"
        },
        {
            'limit': 4,
            'method': 'unique',
            'letter': "IV"
        },
        {
            'limit': 1,
            'method': 'repeat',
            'letter': "I"
        }
    ]

    if isinstance(number, str) or number < 1:
        raise TypeError(f"The value you entered is invalid: {number} is not a positive integer.")

    else:
        for i in range(len(roman)):
            if number // roman[i]['limit'] > 0:
                if roman[i]['method'] == 'unique':
                    result += roman[i]['letter']
                else:
                    for j in range(number // roman[i]['limit']):
                        result += roman[i]['letter']

                number = number % roman[i]['limit']

    return result