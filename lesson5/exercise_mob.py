def chop(element, array):
    if element in array:
        return array.index(element)
    return -1

no_repeat = {
    50: "L",
    9: "IX",
    5: "V",
    4: "IV"
}

repeat = {
    100: "C",
    10: "L",
    1: "I",
}

array = [
    {
        100: "C"
    },
    {
        50: "L"
    },
    {
        10: "X"
    },
    {
        9: "IX"
    },
    {
        5: "V"
    },
    {
        4: "IV"
    },
    {
        1: "I"
    }
]

def get_roman_numeral(number):
    result = ""

    for item in array:
        if number == item.keys()[0]:
            result += item.values()[0]
        else:
            for i in range(number // item.keys()[0]): 
               result += item.values()[0]

        number = number % item.keys()[0]

    # if number // 50 > 0:
    #     result += "L"

    # number = number % 50

    # if number // 10 > 0:
    #     for i in range(number // 10): 
    #         result += "X"
    
    # number = number % 10

    # if number == 9:
    #     result += "IX"
    
    # number = number % 9

    # if number // 5 > 0:
    #     result += "V"
        
    # number = number % 5

    # if number == 4:
    #     result += "IV"

    # number = number % 4

    # if number // 1 > 0:
    #     for i in range(number):
    #         result += "I"
    
    return result
    