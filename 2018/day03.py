import numpy as np


def part1_and_2(command_list):
    def to_int(string_list):
        return list(map(int, string_list))

    commands = []
    for command in command_list:
        cid = int(command.split("@")[0][1:])
        cmd = command.split("@")[1].split(":")
        start = to_int(cmd[0].lstrip().split(","))
        size = to_int(cmd[1].lstrip().split("x"))

        commands.append((cid, start, size))

    maxx, maxy = 0, 0
    for _, start, size in commands:
        maxx = max(start[0] + size[0], maxx)
        maxy = max(start[1] + size[1], maxx)

    grid = np.zeros((maxx + 1, maxy + 1))
    for _, start, size in commands:
        grid[start[0]:start[0] + size[0], start[1]:start[1] + size[1]] += 1

    grid = grid > 1

    winner = None
    for cid, start, size in commands:
        if not np.any(grid[start[0]:start[0] + size[0], start[1]:start[1] + size[1]]):
            winner = cid
            break

    assert winner is not None

    return np.count_nonzero(grid), winner


test_command_list = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
assert part1_and_2(test_command_list) == (4, 3)

input_file = open('day03.in')
sequence = [line.rstrip() for line in input_file]

answer = part1_and_2(sequence)
print("part1:", answer[0])
print("part2:", answer[1])
