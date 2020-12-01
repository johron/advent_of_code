
import argparse
import itertools
import math
parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True)

def get_expense_report_nr(numbers, count, expected_sum):
    for current in itertools.permutations(numbers, count):
        if sum(current) == expected_sum:
            return math.prod(current)
    return None

if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.f) as input_file:
        numbers = [int(n) for n in input_file.read().splitlines()]

        print(f'number[2]: {get_expense_report_nr(numbers, 2, 2020)}')
        print(f'number[3]: {get_expense_report_nr(numbers, 3, 2020)}')

    