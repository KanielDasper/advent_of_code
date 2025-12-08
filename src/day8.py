import math


def parse_lines(file):
    with open(file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        return [tuple(map(int, item.split(","))) for item in lines]


data = parse_lines("data/day8.txt")


def part1(junction_pairs):
    junctions = len(data)

    edges = []

    for current in range(junctions):
        for target in range(current + 1, junctions):
            distance = math.dist(data[current], data[target])
            edges.append((distance, current, target))

    edges.sort()
    parent = list(range(junctions))
    circuit_size = [1] * junctions

    def find_parent_junction(junction):
        if parent[junction] != junction:
            parent[junction] = find_parent_junction(parent[junction])
        return parent[junction]

    def merge_circuits(first_junction, second_junction):
        base_circuit = find_parent_junction(first_junction)
        comp_circuit = find_parent_junction(second_junction)
        if base_circuit == comp_circuit:
            return

        if circuit_size[base_circuit] < circuit_size[comp_circuit]:
            parent[base_circuit] = comp_circuit
            circuit_size[comp_circuit] += circuit_size[base_circuit]
        else:
            parent[comp_circuit] = base_circuit
            circuit_size[base_circuit] += circuit_size[comp_circuit]

    for current in range(junction_pairs):
        distance, first_junction, second_junction = edges[current]
        merge_circuits(first_junction, second_junction)

    curcuits = [find_parent_junction(i) for i in range(junctions)]
    curcuit_mapping = {}
    for curcuit in curcuits:
        if curcuit in curcuit_mapping:
            curcuit_mapping[curcuit] += 1
        else:
            curcuit_mapping[curcuit] = 1
    sorted_sizes = sorted(curcuit_mapping.values(), reverse=True)
    return math.prod(sorted_sizes[:3])


def part2():
    pass
    # Nej tak, part1 tog mig 5 timer.


if __name__ == "__main__":
    print(part1(1000))
