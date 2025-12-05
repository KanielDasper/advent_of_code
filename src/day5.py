def part1(data):
    data.remove("")

    ids = []
    ranges = []

    for i in data:
        if "-" in i:
            l, r = i.split("-")
            ranges.append((l, r))
        if "-" not in i:
            ids.append(int(i))

    fresh = []
    for start, end in ranges:
        for i in ids:
            if i >= int(start) and i <= int(end):
                fresh.append(i)

    return len(set(fresh))


def part2(data):
    ranges = []

    for line in data:
        if "-" in line:
            l, r = line.split("-")
            ranges.append((int(l), int(r)))
    ranges = sorted(ranges, key=lambda x: x[0])

    def merge(intervals):
        merged = []
        for start, end in intervals:
            if not merged or start > merged[-1][1] + 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged

    merged = merge(ranges)
    return sum((end - start + 1) for start, end in merged)


if __name__ == "__main__":
    print(part1(), part2())
