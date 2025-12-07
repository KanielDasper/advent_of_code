from math import prod
from main import parse_lines


def part1():
    data = parse_lines("data/day6.txt")
    nums, ops = data[:-1], data[-1:]

    nums = [num.split() for num in nums]
    ops = " ".join(ops).split()

    answers = []
    for idx, op in enumerate(ops):
        expr = ""
        for num in nums:
            expr += num[idx]
            expr += op

        expr = expr[:-1]  # rm last op
        answers.append(eval(expr))

    return sum(answers)


def part2():
    with open("data/test_day6.txt") as f:
        lines = [
            list(x.replace("\n", "").replace(" ", ".")) for x in f
        ]  # Get whitespaces as dots

    items = list(map(list, zip(*lines)))

    res = 0
    coll = []
    print(items)

    while len(items) > 0:
        item = items.pop()
        if len("".join(item).strip(".")) > 0:
            coll.append(item)
            op = item[-1]
            if op in ("+", "*"):
                numbers = ["".join(c[:-1]).strip(".") for c in coll]
                numbers = [int(n) for n in numbers if len(n) > 0]

                if op == "+":
                    res += sum(numbers)
                else:
                    res += prod(numbers)
                coll = []
    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
