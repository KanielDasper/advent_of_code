with open("data/day2.txt", "r") as f:  # "11-22" -> "[(11, 22)]"
    data = [tuple(line.split("-")) for line in f.read().split(",")]


def invalid_id_part1(data):
    invalid_id_sum = 0

    for first, second in data:
        start = int(first)
        end = int(second)

        for i in range(start, end + 1):
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
print(ans1)


def invalid_id_part2(data):
    invalid_id_sum = 0

    for first, second in data:
        start = int(first)
        end = int(second)

        for i in range(start, end + 1):
            current_id = str(i)
            total_len = len(current_id)

            for chunk_size in range(1, total_len):
                if total_len % chunk_size != 0:
                    continue

                chunks = [
                    current_id[pos : pos + chunk_size]
                    for pos in range(0, total_len, chunk_size)
                ]

                if len(chunks) < 2:
                    continue

                if all(chunk == chunks[0] for chunk in chunks):
                    invalid_id_sum += i
                    break

    return invalid_id_sum


ans2 = invalid_id_part2(data)
print(ans2)
