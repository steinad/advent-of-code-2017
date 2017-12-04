#!/usr/bin/env python3
import sys
import argparse


def captcha(digits):
    '''Finds the sum of all digits that match the next digit in the list. The list is circular, so the
        digit after the last digit is the first digit in the list.

        digits - the input string of digits
    '''
    total = 0
    for idx in range(len(digits) - 1):
        if digits[idx] == digits[idx + 1]:
            total += int(digits[idx])

    if digits[0] == digits[-1]:
        total += int(digits[0])

    return total


def captcha_halfway(digits):
    '''Finds the sum of all digits that match the digit halfway around a circular list.

        digits - the input string of digits. Assumes an even length list.
    '''
    num_digits = len(digits)
    halfway = int(num_digits / 2)
    total = 0
    for idx in range(len(digits)):
        if digits[idx] == digits[(idx + halfway) % num_digits]:
            total += int(digits[idx])

    return total


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process captcha two ways.')
    parser.add_argument('-d', '--digit-string', nargs='?')
    parser.add_argument('-i', '--input-file', nargs='?')
    args = parser.parse_args()

    digits = None
    if args.digit_string is not None:
        digits = args.digit_string.strip()
    elif args.input_file is not None:
        with open(args.input_file) as f:
            digits = next(f).strip()

    if digits is not None:
        print(
            "{}\n\tsequential ==> {}\n\thalfway ==> {}".format(
                digits,
                captcha(digits),
                captcha_halfway(digits)
            )
        )
