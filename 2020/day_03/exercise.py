import re
import itertools
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True)

def get_tree_collisions(lines, start_x, start_y, delta_x, delta_y):
    current_x = start_x
    collisions = 0
    for current_y in range(start_y, len(lines), delta_y):
        if lines[current_y][current_x] == '#':
            collisions += 1
        current_x = (current_x + delta_x) % len(lines[current_y])
    return collisions

def get_tree_collision_product(lines, start_x, start_y, slopes):
    product = 1
    for slope in slopes:
        product *= get_tree_collisions(lines, start_x, start_y, slope[0], slope[1])
    return product

if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.f) as input_file:
        lines = input_file.read().splitlines()
        print(f'tree collisions: {get_tree_collisions(lines, 0, 0, 3, 1)}')
        slopes = [[1,1], [3,1], [5,1], [7, 1], [1, 2]]
        print(f'collision product: {get_tree_collision_product(lines, 0, 0, slopes)}')
