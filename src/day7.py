from main import parse_lines


def part1():
    data = parse_lines("data/day7.txt")
    data = [list(line) for line in data]

    total_beams = 0

    # enumerate my beloved
    for y_pos, row in enumerate(data):
        for x_pos, col in enumerate(row):
            if col == "S":
                data[y_pos + 1][x_pos] = "|"
            elif col == ".":
                if y_pos - 1 > 0 and data[y_pos - 1][x_pos] == "|":
                    data[y_pos][x_pos] = "|"
            elif col == "^":
                if y_pos - 1 > 0 and data[y_pos - 1][x_pos] == "|":
                    data[y_pos][x_pos - 1] = "|"
                    data[y_pos][x_pos + 1] = "|"
                    total_beams += 1
    return total_beams

def walk(tree):
    if tree is not None:
        print(tree)
        walk(tree.left)
        walk(tree.right)

def part2():
    data = parse_lines("data/test_day7.txt")
    return data


if __name__ == "__main__":
    print(part1())
    print(part2())
