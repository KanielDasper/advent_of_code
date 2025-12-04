test_data = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]


def part1(data, limit=3):
    matrix = [list(row) for row in data]
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result = 0

    def is_valid(row, col):
        return 0 <= row < num_rows and 0 <= col < num_cols

    def count_adjacent_ats(row, col):
        adjacent_count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                neighbor_row = row + dr
                neighbor_col = col + dc
                if is_valid(neighbor_row, neighbor_col):
                    if matrix[neighbor_row][neighbor_col] == "@":
                        adjacent_count += 1

        return adjacent_count

    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == "@":
                if count_adjacent_ats(row, col) <= limit:
                    result += 1

    return result


def part2(data, limit=3):
    matrix = [list(row) for row in data]
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    total_removed = 0

    def is_valid(row, col):
        return 0 <= row < num_rows and 0 <= col < num_cols

    def count_adjacent_ats(row, col):
        adjacent_count = 0 

        # 3x3 grid, skip cell itself
        for delta_row in (-1, 0, 1): 
            for delta_col in (-1, 0, 1):
                if delta_row == 0 and delta_col == 0:
                    continue
                neighbor_row = row + delta_row
                neighbor_col = col + delta_col
                if is_valid(neighbor_row, neighbor_col):
                    if matrix[neighbor_row][neighbor_col] == "@":
                        adjacent_count += 1
        return adjacent_count

    any_removal = True
    while any_removal:
        any_removal = False
        cells_to_remove = []

        for row in range(num_rows):
            for col in range(num_cols):
                if matrix[row][col] == "@":
                    if count_adjacent_ats(row, col) <= limit:
                        cells_to_remove.append((row, col))
                        any_removal = True

        for row, col in cells_to_remove:
            matrix[row][col] = "."
            total_removed += 1

    return total_removed
