#!python

import math
import string


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 94, 'base is out of range: {}'.format(base)

    symbols = getSymbols(base)

    flippydoos = []
    for digit in digits:
        flippydoos.append(symbols.find(digit))

    flippydoos = flippydoos[::-1]

    result = 0
    for power, flippy in enumerate(flippydoos):
        if power == 0:
            result += flippy
        else:
            result += flippy * (base ** power)

    return result


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 94, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    symbols = getSymbols(base)

    num = number
    power = 0
    while num / base >= 1:
        num /= base
        power += 1

    num = number
    max_power = power + 1
    encoded = []
    while len(encoded) < max_power:
        if num >= base ** power:
            index = math.floor(num / (base ** power))
            encoded.append(symbols[index])
            num -= index * (base ** power)
        else:
            encoded.append('0')
        power -= 1

    return ''.join(encoded)


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 94, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 94, 'base2 is out of range: {}'.format(base2)

    decoded = decode(digits, base1)
    converted = encode(decoded, base2)
    return converted

def getSymbols(base):
    """Gets the necessary symbols for encoding/decoding"""
    if base == 64:
        set = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
    else:
        set = string.printable

    return set[:base]


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])

        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
