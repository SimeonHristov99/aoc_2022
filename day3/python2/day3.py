def get_score(item: str) -> int:
    if item.islower():
        first_letter = 'a'
        initial_score = 1
    else:
        first_letter = 'A'
        initial_score = 27

    return ord(item) - ord(first_letter) + initial_score


def part1(file: str):
    with open(file, 'r') as f:
        lines = f.read().splitlines()

    scores = []

    for line in lines:
        half = len(line) // 2

        compartment_first = set(line[:half])
        compartment_second = set(line[half:])
        appear_in_both = compartment_first.intersection(compartment_second)

        scores += list(map(get_score, appear_in_both))

    return sum(scores)


def main():
    print(f"Part 1 (sample): {part1('sample.txt')}")
    print(f"Part 1 (input): {part1('input.txt')}")


if __name__ == '__main__':
    main()
