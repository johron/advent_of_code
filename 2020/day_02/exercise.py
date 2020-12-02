import re
from operator import xor
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True)

def normal_password(min, max, character, password):
    return password.count(character) in range(min, max+1)

def toboggan_password(first, second, character, password):
    first_match = password[first-1] == character
    second_match = password[second-1] == character
    return (first_match or second_match) and xor(first_match, second_match)

def validate_from_string(input, validator):
    pattern = re.compile(r'(\d+)-(\d+) (\D): (\D+)')
    matches = pattern.findall(input)[0]
    return validator(int(matches[0]), int(matches[1]), matches[2], matches[3])
    
if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.f) as input_file:
        normal_passwords = 0
        toboggan_passwords = 0
        for line in input_file.read().splitlines():
            if validate_from_string(line, normal_password):
                normal_passwords += 1
            if validate_from_string(line, toboggan_password):
                toboggan_passwords += 1

        print(f'normal passwords: {normal_passwords}')
        print(f'toboggan passwords: {toboggan_passwords}')