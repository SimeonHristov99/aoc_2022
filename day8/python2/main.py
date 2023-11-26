FILENAME_SAMPLE = "sample.txt"
FILENAME_INPUT = "input.txt"


def part1(filename: str) -> int:
    with open(filename, "r") as f:
        grid = f.read().splitlines()

    num_rows = len(grid)
    num_cols = len(grid[0])

    num_visible = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if i in {0, num_rows - 1} or j in {0, num_cols - 1}:
                num_visible += 1
                continue

            # right
            visible = True
            j_clone = j + 1
            while j_clone < num_cols and visible:
                if grid[i][j_clone] >= grid[i][j]:
                    visible = False
                j_clone += 1
            if visible:
                num_visible += 1
                continue

            # left
            visible = True
            j_clone = j - 1
            while j_clone >= 0 and visible:
                if grid[i][j_clone] >= grid[i][j]:
                    visible = False
                j_clone -= 1
            if visible:
                num_visible += 1
                continue

            # down
            visible = True
            i_clone = i + 1
            while i_clone < num_rows and visible:
                if grid[i_clone][j] >= grid[i][j]:
                    visible = False
                i_clone += 1
            if visible:
                num_visible += 1
                continue

            # up
            visible = True
            i_clone = i - 1
            while i_clone >= 0 and visible:
                if grid[i_clone][j] >= grid[i][j]:
                    visible = False
                i_clone -= 1
            if visible:
                num_visible += 1

    return num_visible


def part2(filename: str):
    with open(filename, "r") as f:
        grid = f.read().splitlines()

    num_rows = len(grid)
    num_cols = len(grid[0])

    max_score = 0

    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            num_right = 0
            j_clone = j + 1
            while j_clone < num_cols:
                num_right += 1
                if grid[i][j_clone] >= grid[i][j]:
                    break
                j_clone += 1

            num_left = 0
            j_clone = j - 1
            while j_clone >= 0:
                num_left += 1
                if grid[i][j_clone] >= grid[i][j]:
                    break
                j_clone -= 1

            num_down = 0
            i_clone = i + 1
            while i_clone < num_rows:
                num_down += 1
                if grid[i_clone][j] >= grid[i][j]:
                    break
                i_clone += 1

            num_up = 0
            i_clone = i - 1
            while i_clone >= 0:
                num_up += 1
                if grid[i_clone][j] >= grid[i][j]:
                    break
                i_clone -= 1

            score = num_left * num_right * num_up * num_down

            max_score = max(max_score, score)

    return max_score


def main() -> None:
    print(f"Part 1 (sample): {part1(FILENAME_SAMPLE)}")
    print(f"Part 1 (input): {part1(FILENAME_INPUT)}")

    print(f"Part 2 (sample): {part2(FILENAME_SAMPLE)}")
    print(f"Part 2 (input): {part2(FILENAME_INPUT)}")


if __name__ == "__main__":
    main()
