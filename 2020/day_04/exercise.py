import re
import itertools
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True)

def naive_validators():
    validators = {}
    validators['byr'] = lambda text: True
    validators['iyr'] = lambda text: True
    validators['eyr'] = lambda text: True
    validators['hgt'] = lambda text: True
    validators['hcl'] = lambda text: True
    validators['ecl'] = lambda text: True
    validators['pid'] = lambda text: True
    return validators
    
def validate_height_2(string):
    if string.endswith('in'):
        return len(string) == 4 and int(string[0:2]) in range(59, 77)
    elif string.endswith('cm'):
        return len(string) == 5 and int(string[0:3]) in range(150, 194)
    else:
        return False

def strict_validators():
    validators = {}
    validators['byr'] = lambda text: int(text) in range(1920, 2003)
    validators['iyr'] = lambda text: int(text) in range(2010, 2021)
    validators['eyr'] = lambda text: int(text) in range(2020, 2031)
    validators['hgt'] = lambda text: validate_height_2(text)
    validators['hcl'] = lambda text: re.match(r'^#[0-9, a-f]{6}$', text) is not None
    validators['ecl'] = lambda text: text in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    validators['pid'] = lambda text: re.match(r'^\d{9}$', text) is not None
    return validators

class PassportValidator:
    def __init__(self, data, validators):
        self._data = re.split(r'[ \n]', data.strip())
        self._validators = validators

    def is_valid(self):
        for key in self._validators.keys():
            if not self.has_entry(key):
                return False

        for entry in self._data:
            elements = entry.split(':')
            key = elements[0]
            value = elements[1]

            if key in self._validators.keys():
                if not self.entry_is_valid(key, value):
                    return False
        return True

    def has_entry(self, key):
        for entry in self._data:
            if entry.find(key) == 0:
                return True
        return False

    def entry_is_valid(self, key, value):
        return self._validators[key](value)        

def valid_password_count(text, validators):
    count = 0
    sections = text.split('\n\n')
    for section in sections:
        p = PassportValidator(section, validators)
        if p.is_valid():
            count += 1
    return count


if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.f) as input_file:
        text = input_file.read()
        print(f'naive passports: {valid_password_count(text, naive_validators())}')
        print(f'strict passports: {valid_password_count(text, strict_validators())}')


