import numpy as np


def power(x, y, serial):
    id = x + 10
    power = id * y
    power += serial
    power *= id
    hundreds = int(str(power)[-3])

    return hundreds - 5


assert power(3, 5, 8) == 4
assert power(122, 79, 57) == -5
assert power(217, 196, 39) == 0
assert power(101, 153, 71) == 4


def solution(serial, sizes=(3,)):
    grid = np.zeros((300, 300), dtype=int)

    for y in range(300):
        for x in range(300):
            grid[x, y] = power(x + 1, y + 1, serial)

    # Summed-area table
    summed_grid = grid.cumsum(axis=0).cumsum(axis=1)

    max_value, best_pos, best_size = 0, None, None
    for size in sizes:
        for y in range(300 - size):
            for x in range(300 - size):
                a, b, c, d = (x, y), (x, y + size), (x + size, y), (x + size, y + size)
                value = summed_grid[a] + summed_grid[d] - summed_grid[b] - summed_grid[c]
                if value > max_value:
                    max_value = value
                    best_pos = (x + 2, y + 2)
                    best_size = size

    return best_pos, best_size, max_value


assert solution(42) == ((21, 61), 3, 30)
assert solution(18) == ((33, 45), 3, 29)
print("part1:", solution(8199))

assert solution(42, sizes=range(300)) == ((232, 251), 12, 119)
assert solution(18, sizes=range(300)) == ((90, 269), 16, 113)
print("part2:", solution(8199, sizes=range(300)))
