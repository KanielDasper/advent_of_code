def part1():
    with open("data/day9.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        lines = [tuple(map(int, l.split(","))) for l in lines]

    max_area = 0
    for i in range(len(lines)):
        x1, y1 = lines[i][0], lines[i][1]
        for j in range(i + 1, len(lines)):
            x2, y2 = lines[j]
            area = abs((x2 - x1) - 1) * abs((y2 - y1) - 1)  #
            max_area = max(max_area, area)

    return max_area


if __name__ == "__main__":
    print(part1())
