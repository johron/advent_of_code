import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True)

def fuel_equation(mass):
    return (mass // 3) - 2

def compound_fuel_equation(mass):
    total_cost = 0
    fuel_cost = fuel_equation(mass)
    while fuel_cost > 0:
        total_cost += fuel_cost
        fuel_cost = fuel_equation(fuel_cost)
    return total_cost
    

def get_original_fuel(numbers):
    return sum(fuel_equation(mass) for mass in numbers)

def get_compound_fuel(numbers):
    return sum(compound_fuel_equation(mass) for mass in numbers)

if __name__ == '__main__':
    args = parser.parse_args()
    with open(args.f) as input_file:
        numbers = [int(n) for n in input_file.read().splitlines()]

        print(f'fuel requirements [original]: {get_original_fuel(numbers)}')
        print(f'fuel requirements [compound]: {get_compound_fuel(numbers)}')