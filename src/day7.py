import functools
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


def part2():
    data = parse_lines("data/day7.txt")
    data = [list(line) for line in data]

    height = len(data)
    width = len(data[0])
    timelines = 1

    @functools.lru_cache()
    def run_timeline(x_pos, y_pos):
        if not (0 <= x_pos < width and 0 <= y_pos < height):
            return 0
        tile = data[y_pos][x_pos]

        timelines = 0
        if tile == "S":
            if y_pos + 1 < height:
                data[y_pos + 1][x_pos] = "|"
                timelines += run_timeline(x_pos, y_pos + 1)
            return timelines

        if tile == "|":
            return run_timeline(x_pos, y_pos + 1)

        if tile == ".":
            if data[y_pos - 1][x_pos] == "|":
                data[y_pos][x_pos] = "|"
                timelines += run_timeline(x_pos, y_pos + 1)
            return timelines

        if tile == "^":
            if data[y_pos - 1][x_pos] == "|":
                if x_pos - 1 >= 0:
                    data[y_pos][x_pos - 1] = "|"
                    timelines += run_timeline(x_pos - 1, y_pos)

                if x_pos + 1 < width:
                    data[y_pos][x_pos + 1] = "|"
                    timelines += run_timeline(x_pos + 1, y_pos)
                return timelines + 1

    for y_pos, row in enumerate(data):
        for x_pos, col in enumerate(row):
            if col == "S":
                timelines += run_timeline(x_pos, y_pos)

    return timelines


if __name__ == "__main__":
    print(part1())
    print(part2())
