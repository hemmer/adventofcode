import numpy as np

def parts_1_and_2(points, part2_limit=10000):
    # make indexing simpler
    points[:, 0] -= points[:, 0].min()
    points[:, 1] -= points[:, 1].min()

    min_x, max_x = points[:, 0].min(), points[:, 0].max() + 1
    min_y, max_y = points[:, 1].min(), points[:, 1].max() + 1

    grid_full = np.zeros((max_x, max_y, len(points)), dtype=int)

    for x in range(0, max_x):
        for y in range(0, max_y):
            for i, (px, py) in enumerate(points):
                grid_full[x, y, i] = abs(px - x) + abs(py - y)

    grid_closest = np.zeros((max_x, max_y), dtype=int)

    for x in range(0, max_x):
        for y in range(0, max_y):

            distances = grid_full[x, y, :]
            closest = np.where(distances == distances.min())[0]

            if len(closest) == 1:
                grid_closest[x, y] = closest[0]
            else:
                grid_closest[x, y] = -1

    # edge elements are infinite
    edges = set(np.concatenate((grid_closest[0, :], grid_closest[-1, :], grid_closest[:, 0], grid_closest[:, -1])))
    # so remove
    for edge_val in edges:
        grid_closest[grid_closest == edge_val] = 0
    grid_closest[grid_closest == -1] = 0

    # count the largest remaining region
    remaining = np.unique(grid_closest[grid_closest > 0], return_counts=True)[1]
    part1 = remaining.max()

    grid_reduced = np.sum(grid_full, axis=2)
    part2 = len(grid_reduced[grid_reduced < part2_limit])

    return part1, part2


points = np.array([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
assert parts_1_and_2(points, part2_limit=32) == (17, 16)

input_file = open('day06.in')
sequence = np.array([tuple(map(int, line.rstrip().split(", "))) for line in input_file])
ans1, ans2 = parts_1_and_2(sequence)

print("part1:", ans1)
print("part2:", ans2)
