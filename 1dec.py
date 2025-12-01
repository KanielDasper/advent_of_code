import csv
import re

with open("data/dial_input.csv") as f:
    reader = csv.reader(f)
    dial_inputs = [row[0] for row in reader]


def convert_to_number(item) -> int:
    _, number = re.match(r"([A-Za-z]+)(\d+)", item).groups()
    return int(number)


def input_parser(input_list) -> int:
    dial_start_number = 50
    no_of_times_passed_0 = 0

    for item in input_list:
        if item.startswith("L"):
            number = convert_to_number(item)
            dial_start_number -= number

        if item.startswith("R"):
            number = convert_to_number(item)
            dial_start_number += number

        if dial_start_number > 99 or dial_start_number < 0:
            dial_start_number = dial_start_number % 100

        if dial_start_number == 0:
            no_of_times_passed_0 += 1

    return no_of_times_passed_0


print(input_parser(dial_inputs))
