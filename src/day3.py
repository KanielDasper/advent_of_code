def solve(batteries: int):
    with open("data/day3.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    result = 0

    for value in data:
        battery_string = ""
        current_pos = 0

        for idx in range(batteries, 0, -1):
            current_range = value[current_pos : len(value) - idx + 1]
            current_highest = max(current_range)
            battery_string += str(current_highest)
            current_pos += current_range.index(current_highest) + 1

        result += int(battery_string)
    return result


if __name__ == "__main__":
    ans1 = solve(2)
    ans2 = solve(12)
    print(ans1)
    print(ans2)
