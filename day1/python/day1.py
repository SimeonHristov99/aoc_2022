import numpy as np


def part1(file: str):
    with open(file, 'r') as f:
        elements = [line.strip() for line in f.readlines()]

    res = []
    current = []

    for el in elements:
        if el.isnumeric():
            current.append(int(el))
        else:
            res.append(current)
            current = []

    res.append(current)

    return max(map(sum, res))


def part2(file: str):
    with open(file, 'r') as f:
        elements = [line.strip() for line in f.readlines()]

    res = []
    current = []

    for el in elements:
        if el.isnumeric():
            current.append(int(el))
        else:
            res.append(current)
            current = []

    res.append(current)

    return sum(sorted(map(sum, res))[-3:])


def main():
    print(f"Part 1 (sample): {part1('sample.txt')}")
    print(f"Part 1 (input): {part1('input.txt')}")
    print()
    print(f"Part 2 (sample): {part2('sample.txt')}")
    print(f"Part 2 (input): {part2('input.txt')}")


if __name__ == '__main__':
    main()
