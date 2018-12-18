import sys

import numpy as np


class Coord(object):
    def __init__(self, i, j, value=None):
        self.i, self.j = i, j  # i row, j column
        self.value = value

    def __lt__(self, other):
        if self.value is not None and self.value != other.value:
            return self.value < other.value

        if self.i == other.i:
            return self.j < other.j
        else:
            return self.i < other.i

    def __repr__(self):
        if self.value is not None:
            return f"<coord: i: {self.i}, j: {self.j}, value: {self.value}>"
        else:
            return f"<coord: i: {self.i}, j: {self.j}>"


class Unit(Coord):
    def __init__(self, i, j, unit_type):
        super(Unit, self).__init__(i, j)

        self.unit_type = unit_type  # 1 elf, 2, goblin

    def __repr__(self):
        if self.unit_type == 1:
            return f"<elf: i: {self.i}, j: {self.j}>"
        elif self.unit_type == 2:
            return f"<goblin: i: {self.i}, j: {self.j}>"


def backtrace(distance, start_i, start_j):
    def get_next(i, j, value):
        if value == 2:
            return Coord(i, j)
        for di, dj in [[-1, 0], [0, -1], [0, +1], [+1, 0]]:
            if distance[i + di, j + dj] == value - 1:
                return get_next(i + di, j + dj, value - 1)
        assert False

    path_length = distance[start_i, start_j]
    return get_next(start_i, start_j, path_length), path_length


def best_move(grid, i, j, targets):
    path_distance = np.zeros(grid.shape)
    path_distance[grid != 0] = -1
    path_distance[i, j] = 0

    for target in targets:
        path_distance[target.i, target.j] = 0

    def recurse_best_path(path, ri, rj, dist):
        for target in targets:
            if ri == target.i and rj == target.j:
                # better than recorded or unset
                if path[ri, rj] > dist or path[ri, rj] == 0:
                    path[ri, rj] = dist
                    return False
                else:
                    return True
        if path[ri, rj] != 0:
            if path[ri, rj] > dist:
                path[ri, rj] = dist
            else:
                return True

        path[ri, rj] = dist

        dead_end_up = recurse_best_path(path, ri - 1, rj, dist + 1)
        dead_end_left = recurse_best_path(path, ri, rj - 1, dist + 1)
        dead_end_right = recurse_best_path(path, ri, rj + 1, dist + 1)
        dead_end_down = recurse_best_path(path, ri + 1, rj, dist + 1)

        all_dead_ends = dead_end_right and dead_end_left and dead_end_up and dead_end_down

        if all_dead_ends:
            return True
        else:
            return False

    all_dead_ends = recurse_best_path(path_distance, i, j, 1)
    if all_dead_ends:
        return None
    else:
        return path_distance


def update(i, j, grid, grid_hp):
    if grid[i, j] == 1:
        enemy_type = 2
    elif grid[i, j] == 2:
        enemy_type = 1
    else:
        # this unit must have died
        return False

    if np.count_nonzero(grid == enemy_type) == 0:
        return True

    at_target, possible_targets = False, []
    for ei in range(1, len(grid) - 1):
        if at_target:
            break
        for ej in range(1, len(grid[0]) - 1):
            if (grid[ei + 1, ej] == enemy_type or grid[ei - 1, ej] == enemy_type or
                    grid[ei, ej + 1] == enemy_type or grid[ei, ej - 1] == enemy_type):
                if ei == i and ej == j:
                    possible_targets.clear()
                    at_target = True
                    break
                if grid[ei, ej] == 0:
                    possible_targets.append(Coord(ei, ej))

    if len(possible_targets) > 0:
        distance_field = best_move(grid, i, j, possible_targets)

        # if we've got this far (possible_targets > 0) then we aren't already at a
        # target - if the distance field is None, then we can't reach any targets
        if distance_field is None:
            return False

        for target in possible_targets:
            if distance_field[target.i, target.j] <= 0:
                dist = grid.shape[0] * grid.shape[1]
            else:
                dist = distance_field[target.i, target.j] - 1
            target.value = dist
        possible_targets.sort()

        chosen_target = possible_targets[0]
        next_position, _ = backtrace(distance_field, chosen_target.i, chosen_target.j)

        # if the target represents a move from the current square
        if next_position.i != i or next_position.j != j:
            grid[next_position.i, next_position.j] = grid[i, j]
            grid[i, j] = 0

            grid_hp[next_position.i, next_position.j] = grid_hp[i, j]
            grid_hp[i, j] = 0

            i, j = next_position.i, next_position.j

    candidate_targets = []
    for di, dj in [[-1, 0], [+1, 0], [0, +1], [0, -1]]:
        if grid[i + di, j + dj] == enemy_type:
            candidate_targets.append(Coord(i + di, j + dj, grid_hp[i + di, j + dj]))
    candidate_targets.sort()

    if len(candidate_targets) > 0:
        target = candidate_targets[0]
        grid_hp[target.i, target.j] -= 3

        if grid_hp[target.i, target.j] < 0:
            print("#### DEATH AT", target.i, target.j, "#####")
            grid[target.i, target.j] = 0
            grid_hp[target.i, target.j] = 0

    return False


def parse_input(filename):
    file = open(filename)

    width, height = 0, 0
    for line in file:
        width = max(len(line.rstrip()), width)
        height += 1

    grid = np.zeros((height, width), dtype=int)
    grid_hp = np.zeros((height, width), dtype=int)

    file.seek(0)
    for i, line in enumerate(file):
        for j, c in enumerate(line.rstrip()):
            if c == '#':
                grid[i, j] = -1
            elif c == '.':
                grid[i, j] = 0

            # units
            elif c == "E":
                grid[i, j] = 1
                grid_hp[i, j] = 200
            elif c == "G":
                grid[i, j] = 2
                grid_hp[i, j] = 200
            else:
                assert False

    return grid, grid_hp


def draw_grid(grid_to_draw):
    for i in range(len(grid_to_draw)):
        for j in range(len(grid_to_draw[0])):

            if grid_to_draw[i, j] == 0:
                print(".", end="")
            elif grid_to_draw[i, j] == -1:
                print("#", end="")
            elif grid_to_draw[i, j] == 1:
                print("E", end="")
            elif grid_to_draw[i, j] == 2:
                print("G", end="")
            else:
                assert False
        print()
    print()
    sys.stdout.flush()


def get_enemies(grid_to_search):
    enemy_coordinates = []
    for i in range(len(grid_to_search)):
        for j in range(len(grid_to_search[0])):
            if grid_to_search[i, j] == 1:
                enemy_coordinates.append(Coord(i, j))
            elif grid_to_search[i, j] == 2:
                enemy_coordinates.append(Coord(i, j))

    enemy_coordinates.sort()
    return enemy_coordinates


def part1(filename):
    grid, grid_hp = parse_input(filename)
    draw_grid(grid)

    t = 0
    while True:
        enemy_coordinates = get_enemies(grid)

        for coordinate in enemy_coordinates:
            are_we_finished = update(coordinate.i, coordinate.j, grid, grid_hp)

            if are_we_finished:
                return t * np.sum(grid_hp)

        t = t + 1
        print("After", t, "rounds")
        draw_grid(grid)


assert part1("day15.in.test.3") == 27730
assert part1("day15.in.test.1") == 39514
assert part1("day15.in.test.4") == 36334
assert part1("day15.in.test.2") == 18740

ans = part1("day15.in")
print("part1:", ans)
