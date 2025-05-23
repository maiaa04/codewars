# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5

import unittest


def parse_int(string: str):
    units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'] # value corresponds to index
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']  # value corresponds to 10*index
    scales = ['', '', 'hundred', 'thousand', '', '', 'million']  # value corresponds to 10**index
    temp = 0
    result = 0
    string = string.replace(' and ', ' ').replace('-', ' ')
    s = string.split(' ')
    for x in s:
        if x in units:
            temp += units.index(x)
        elif x in tens:
            temp += tens.index(x)*10
        else:
            if x == 'hundred':
                temp += temp*(10**scales.index(x))-temp
            else:
                result += temp*(10**scales.index(x))
                temp = 0
        if x is s[-1]:
            result += temp
    return result


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_int('one'), 1)
        self.assertEqual(parse_int('twenty'), 20)
        self.assertEqual(parse_int('two hundred forty-six'), 246)
        self.assertEqual(
            parse_int('six hundred sixty-six thousand six hundred sixty-six'), 666666)


if __name__ == '__main__':
    unittest.main()
