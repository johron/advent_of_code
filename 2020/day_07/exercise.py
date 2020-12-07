import re
import itertools
import argparse
import string
parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True)

class BagRule:
    def __init__(self, name, content):
        self._name = name
        self._content = content

    def __repr__(self):
        return f'{self._name}, {self._content}'

    def can_contain(self, desired):
        return desired in self._content.keys()
    
    def get_number_of_bags(self, rules):
        current = 1
        for name, count in self._content.items():
            current += (rules[name].get_number_of_bags(rules) * count)
        return current


def make_bag_rules(input):
    rules = {}
    for line in input.splitlines():
        match_1 = re.match(r'^(\D+ \D+) bags* contain (.+)', line)
        name = match_1.group(1)
        rest = match_1.group(2)
        content = {}
        for entry in rest.split(','):
            match_2 = re.match(r'^(\d+) (\D+ \D+) bags*', entry.strip())
            if match_2:
                content[match_2.group(2)] = int(match_2.group(1))

        rules[name] = BagRule(name, content)
        #print(rules[name])
    return rules

def get_bag_layers(input, desired):
    rules = make_bag_rules(input)
    remaining_bags = [desired]
    found_bags = set()
    while remaining_bags:
        current_bag = remaining_bags.pop(0)
        for name, rule, in rules.items():
            if name not in found_bags and rule.can_contain(current_bag):
                remaining_bags.append(name)
        found_bags.add(current_bag)

    return len(found_bags) -1

def get_bag_count(input, desired):
    rules = make_bag_rules(input)
    return rules[desired].get_number_of_bags(rules) -1



if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.f) as input_file:
        text = input_file.read()
        search_color = 'shiny gold'
        print(f'layers ({search_color}): {get_bag_layers(text, search_color)}')
        print(f'count ({search_color}): {get_bag_count(text, search_color)}')
        


