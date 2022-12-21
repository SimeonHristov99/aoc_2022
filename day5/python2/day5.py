def solve(file: str, part1=True):
    with open(file, 'r') as f:
        lines = f.read().splitlines()

    stacks = [''] * len([lines[0][j:j+3] for j in range(0, len(lines[0]), 4)])

    i = 0
    while lines[i + 1] != '':
        for idx, j in enumerate(range(0, len(lines[i]), 4)):
            to_add = lines[i][j:j+3]
            if to_add.strip() != '':
                stacks[idx] += to_add[1]

        i += 1

    for line in lines[i + 2:]:
        _, how_much, _, stack_from, _, stack_to = line.split()

        how_much = int(how_much)
        stack_from = int(stack_from) - 1
        stack_to = int(stack_to) - 1

        taken = stacks[stack_from][:how_much]
        stacks[stack_from] = stacks[stack_from][how_much:]

        if part1:
            stacks[stack_to] = taken[::-1] + stacks[stack_to]
        else:
            stacks[stack_to] = taken + stacks[stack_to]

    return ''.join(map(lambda xs: xs[0], stacks))


def main():
    print(f'Part 1 (sample.txt): {solve("sample.txt")}')
    print(f'Part 1 (input.txt): {solve("input.txt")}')
    print()
    print(f'Part 2 (sample.txt): {solve("sample.txt", False)}')
    print(f'Part 2 (input.txt): {solve("input.txt", False)}')


if __name__ == '__main__':
    main()
