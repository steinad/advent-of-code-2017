#!/usr/bin/env python3
import argparse


def checksum(spreadsheet):
    total = 0
    for line in spreadsheet:
        minval = line[0]
        maxval = minval
        for value in line:
            if value < minval:
                minval = value
            if value > maxval:
                maxval = value
        total += (maxval - minval)
    return total


def divisible(spreadsheet):
    total = 0
    for line in spreadsheet:
        done = False
        for idx, val1 in enumerate(line):
            for val2 in line[idx + 1:]:
                if val1 % val2 == 0:
                    total += val1 / val2
                    done = True
                    break
                elif val2 % val1 == 0:
                    total += val2 / val1
                    done = True
                    break
            if done:
                break
    return int(total)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process captcha two ways.')
    # parser.add_argument('-i', '--input-file', nargs='?')
    parser.add_argument('input_file')
    args = parser.parse_args()

    spreadsheet = []
    with open(args.input_file) as f:
        for line in f:
            spreadsheet.append(list(map(int, line.strip().split('\t'))))

    print('checksum:', checksum(spreadsheet))
    print('divisibles:', divisible(spreadsheet))
