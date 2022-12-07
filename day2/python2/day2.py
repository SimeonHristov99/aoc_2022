mapping = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

# assuming POV from right player
win_conditions = {
    ('A', 'B'),
    ('C', 'A'),
    ('B', 'C'),
}

weights = {
    'A': 1,
    'B': 2,
    'C': 3,
}

points = {
    'win': 6,
    'draw': 3,
    'lose': 0,
}

# A = Rock
# B = Paper
# C = Scissors

hands = {
    ('win', 'A'): 'B',
    ('win', 'B'): 'C',
    ('win', 'C'): 'A',
    ('lose', 'A'): 'C',
    ('lose', 'B'): 'A',
    ('lose', 'C'): 'B',
}


def convert_to_beginning(ch: str):
    return chr(ord('A') + ord(ch) - ord('X'))


def part1(file: str):
    with open(file, 'r') as f:
        contents = f.readlines()

    contents = [tuple(line.strip().split(' ')) for line in contents]
    contents = [(other, convert_to_beginning(me)) for other, me in contents]

    scores = []

    for other, me in contents:
        if (other, me) in win_conditions:
            scores.append(points.get('win') + weights.get(me))
        elif other == me:
            scores.append(points.get('draw') + weights.get(me))
        else:
            scores.append(points.get('lose') + weights.get(me))

    return sum(scores)


def part2(file: str):
    with open(file, 'r') as f:
        contents = f.readlines()

    contents = [tuple(line.strip().split(' ')) for line in contents]
    contents = [(other, result) for other, result in contents]

    print(contents)

    scores = []

    for other, result in contents:
        if mapping.get(result) == 'win':
            scores.append(points.get('win') +
                          weights.get(hands.get('win', other)))
        elif mapping.get(result) == 'draw':
            scores.append(points.get('draw') + weights.get(other))
        else:
            scores.append(points.get('lose') +
                          weights.get(hands.get('lose', other)))
    
    print(scores)

    return sum(scores)


def main():
    # print(f"Part 1 (sample): {part1('sample.txt')}")
    # print(f"Part 1 (input): {part1('input.txt')}")
    # print()
    print(f"Part 2 (sample): {part2('sample.txt')}")
    # print(f"Part 2 (input): {part2('input.txt')}")


if __name__ == '__main__':
    main()
