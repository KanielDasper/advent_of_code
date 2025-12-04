from day4 import part1, part2


def parse_lines(file):
    with open(file, "r") as f:
        return [line.strip() for line in f.readlines()]


def main():
    lines = parse_lines("data/day4.txt")
    return (part1(lines), part2(lines))

if __name__ == "__main__":
    print(main())
