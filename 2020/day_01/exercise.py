
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True)

def fibbonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibbonacci(n-1) + fibbonacci(n-2)

def recursive_solve(numbers, current_sum, remaining_layers, expected_sum):
    return 0

def get_expense_report_number_2(numbers, expected_nr):
    for first in range(0, len(numbers)):
        for second in range(first+1, len(numbers)):
            if numbers[first] + numbers[second] == expected_nr:
                return numbers[first] * numbers[second]

def get_expense_report_number_3(numbers, expected_nr):
    for first in range(0, len(numbers)):
        for second in range(first+1, len(numbers)):
            for third in range(second+1, len(numbers)):
                if numbers[first] + numbers[second] + numbers[third] == expected_nr:
                    return numbers[first] * numbers[second] * numbers[third]

if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.f) as input_file:
        content = input_file.read()

    numbers = [int(n) for n in content.splitlines()]
    print(f'expense report number: {get_expense_report_number_3(numbers, 2020)}')

    