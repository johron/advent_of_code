import re
import itertools
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True)

def get_row(text):
    return int('0b' + text.replace('B', '1').replace('F', '0'), 2)

def get_col(text):
    return int('0b' + text.replace('R', '1').replace('L', '0'), 2)

def get_seat(text):
    row_input = text[0:7]
    col_input = text[7:10]
    return get_row(row_input)*8 + get_col(col_input)

def get_max_seat_nr(lines):
    max_nr = 0
    for line in lines:
        max_nr = max(max_nr, get_seat(line))
    return max_nr

def get_free_seat_nr(lines):
    seats = sorted([get_seat(line) for line in lines])
    for index in range(0, len(seats)-1):
        if seats[index+1] != seats[index]+1:
            return seats[index]+1
    return None
    

if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.f) as input_file:
        text = input_file.read().splitlines()
        print(f'max seat nr: {get_max_seat_nr(text)}')
        print(f'free seat nr: {get_free_seat_nr(text)}')


