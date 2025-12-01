import csv
import re

with open("dial_input.csv") as f:
    reader = csv.reader(f)
    dial_inputs = [row[0] for row in reader]


def convert_item_to_number(item) -> int:
    _, number = re.match(r"([A-Za-z]+)(\d+)", item).groups()
    return int(number)


def single_click_parser(input_list) -> int:
    dial_number = 50
    password = 0

    for item in input_list:
        number = convert_item_to_number(item)

        if item.startswith("L"):
            dial_number -= number
        elif item.startswith("R"):
            dial_number += number

        while dial_number > 99 or dial_number < 0:
            dial_number = dial_number % 100

        if dial_number == 0:
            password += 1

    return password


first_password = single_click_parser(dial_inputs)
print("First password:", first_password)


def multiple_click_parser(input_list) -> int:
    dial_number = 50
    password = 0
    dial_loc = 0

    for item in input_list:
        number = convert_item_to_number(item)

        if item.startswith("L"):
            dial_loc = -number
        elif item.startswith("R"):
            dial_loc = number

        prev_pointer = dial_number
        dial_number += dial_loc

        crossings = abs(dial_number // 100)
        dial_number = dial_number % 100

        if dial_number == 0 and dial_loc > 0:
            crossings -= 1
        if prev_pointer == 0 and dial_loc < 0:
            crossings -= 1
        if dial_number == 0:
            crossings += 1

        password += crossings

    return password


second_password = multiple_click_parser(dial_inputs)
print("Second password:", second_password)
