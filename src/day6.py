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
    data = parse_lines("data/test_day6.txt")
    nums, ops = data[:-1], data[-1:]

    nums = reversed([num.split() for num in nums])
    ops = " ".join(ops).split()

    for idx, op in enumerate(ops):
        expr = ""
        for num in nums:
            expr += num[idx]
            expr += op

        print(expr)




if __name__ == "__main__":
    print(part1())
    part2()
