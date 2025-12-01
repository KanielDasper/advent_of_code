import csv
import re

with open("dial_input.csv") as f:
    reader = csv.reader(f)
    dial_inputs = [row[0] for row in reader]


def item_to_num(item) -> int:
    _, number = re.match(r"([A-Za-z]+)(\d+)", item).groups()
    return int(number)


def single_click_parser(input_list) -> int:
    dial_num = 50
    password = 0

    for item in input_list:
        num = item_to_num(item)

        if item.startswith("L"):
            dial_num -= num
        elif item.startswith("R"):
            dial_num += num

        while dial_num > 99 or dial_num < 0:
            dial_num = dial_num % 100

        if dial_num == 0:
            password += 1

    return password


first_password = single_click_parser(dial_inputs)
print("First password:", first_password)


def multiple_click_parser(input_list) -> int:
    dial_num = 50
    password = 0
    dial_loc = 0

    for item in input_list:
        num = item_to_num(item)

        if item.startswith("L"):
            dial_loc = -num
        elif item.startswith("R"):
            dial_loc = num

        prev_loc = dial_num
        dial_num += dial_loc

        crossings = abs(dial_num // 100)
        dial_num = dial_num % 100

        if dial_num == 0 and dial_loc > 0:
            crossings -= 1
        if prev_loc == 0 and dial_loc < 0:
            crossings -= 1
        if dial_num == 0:
            crossings += 1

        password += crossings

    return password


second_password = multiple_click_parser(dial_inputs)
print("Second password:", second_password)
