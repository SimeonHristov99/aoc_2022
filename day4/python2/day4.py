def part1(file: str):
    with open(file, 'r') as f:
        lines = f.read().splitlines()

    lines = list(map(lambda x: list(map(lambda y: list(map(int, y.split('-'))), x.split(','))), lines))
    overlapping = 0

    for [(s1, e1), (s2, e2)] in lines:
        if s1 >= s2 and e1 <= e2 or s2 >= s1 and e2 <= e1:
            overlapping += 1

    return overlapping


def part2(file: str):
    with open(file, 'r') as f:
        lines = f.read().splitlines()

    lines = list(map(lambda x: list(map(lambda y: list(map(int, y.split('-'))), x.split(','))), lines))
    overlapping = 0

    for [(s1, e1), (s2, e2)] in lines:
        r1 = set(range(s1, e1 + 1))
        r2 = set(range(s2, e2 + 1))
        
        if len(r1.intersection(r2)) > 0:
            overlapping += 1

    return overlapping


def main():
    print(f"Part 1 (sample): {part1('sample.txt')}")
    print(f"Part 1 (input): {part1('input.txt')}")
    print()
    print(f"Part 2 (sample): {part2('sample.txt')}")
    print(f"Part 2 (input): {part2('input.txt')}")


if __name__ == '__main__':
    main()
