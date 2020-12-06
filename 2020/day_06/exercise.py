import re
import itertools
import argparse
import string
parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True)

def get_sum_of_answers(sections):
    total_sum = 0
    for section in sections:
        answers = set()
        for line in section.splitlines():
            for char in line.strip():
                answers.add(char)
        total_sum += len(answers)
    return total_sum

def get_sum_of_consensus(sections):
    total_sum = 0
    for section in sections:
        answers = set()
        discard = set()
        for line in section.splitlines():
            for char in line.strip():
                answers.add(char)
        
        for char in answers:
            for line in section.splitlines():
                if char not in line.strip():
                    discard.add(char)
        total_sum += len(answers) - len(discard)
    return total_sum


if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.f) as input_file:
        sections = input_file.read().split('\n\n')
        print(f'answer sum: {get_sum_of_answers(sections)}')
        print(f'consensus sum: {get_sum_of_consensus(sections)}')


