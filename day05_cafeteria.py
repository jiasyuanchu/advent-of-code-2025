# day05_cafeteria.py

def parse_input(filename):
    with open(filename) as f:
        sections = f.read().strip().split("\n\n")
    # parsing fresh ranges
    ranges = [tuple(map(int, line.split("-"))) for line in sections[0].splitlines()]
    # parsing IDs
    ids = [int(x) for x in sections[1].splitlines()]
    return ranges, ids

def is_fresh(id, ranges):
    return any(start <= id <= end for start, end in ranges)

def count_fresh(ranges, ids):
    return sum(1 for id in ids if is_fresh(id, ranges))

if __name__ == "__main__":
    # Check the example input first
    ranges, ids = parse_input("day05_example.txt")
    example_result = count_fresh(ranges, ids)
    print("Example result:", example_result)

    # my puzzle input
    ranges, ids = parse_input("day05_input.txt")
    puzzle_result = count_fresh(ranges, ids)
    print("Puzzle input result:", puzzle_result)
