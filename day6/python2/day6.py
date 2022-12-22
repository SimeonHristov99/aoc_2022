def get_idx(xs: str, size: int):
    for i in range(len(xs)):
        if len(set(xs[i:i + size])) == size:
            return i + size

    return -1


def solve(file: str, size: int):
    with open(file, 'r') as f:
        lines = f.read().splitlines()

    return [get_idx(x, size) for x in lines]


def main():
    print(f'Part 1 (sample.txt): {solve("sample.txt", 4)}')
    print(f'Part 1 (input.txt): {solve("input.txt", 4)}')
    print()
    print(f'Part 2 (sample.txt): {solve("sample.txt", 14)}')
    print(f'Part 2 (input.txt): {solve("input.txt", 14)}')


if __name__ == '__main__':
    main()
