with open("data/day2.txt", "r") as f:  # "11-22" -> "[(11, 22)]"
    data = [tuple(line.split("-")) for line in f.read().split(",")]


def invalid_id_part1(data):
    invalid_id_sum = 0
    for first, second in data:
        for i in range(int(first), int(second) + 1):
            current_id = str(i)

            if len(current_id) % 2 == 0:
                left_slice, right_slice = (
                    current_id[: int((len(current_id)) / 2)],
                    current_id[int((len(current_id)) / 2) :],
                )

                if left_slice == right_slice:
                    invalid_id_sum += i

    return invalid_id_sum


ans1 = invalid_id_part1(data)
print("Sum of invalid ID's:", ans1)

# Part 2 incomplete

def invalid_id_part2(data):
    invalid_id_sum = 0
    for first, second in data:
        for i in range(int(first), int(second) + 1):
            current_id = str(i)

            sequence_len = len(current_id) // 2

            if sequence_len == 0 and current_id[:i] * sequence_len == i:
                left_slice, right_slice = (
                    current_id[: int((len(current_id)) / sequence_len)],
                    current_id[int((len(current_id)) / sequence_len) :],
                )

                if left_slice == right_slice:
                    invalid_id_sum += i
    return invalid_id_sum


print(invalid_id_part2(data))
