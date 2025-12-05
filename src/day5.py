from main import parse_lines


def part1():
    data = parse_lines("data/day5.txt")
    data.remove("")

    ids = []
    ranges = []

    for i in data:
        if "-" in i:
            left, right = i.split("-")
            ranges.append((left, right))
        if "-" not in i:
            ids.append(int(i))

    fresh = []
    for start, end in ranges:
        for i in ids:
            if i >= int(start) and i <= int(end):
                fresh.append(i)

    return len(set(fresh))

def part2():
    pass
