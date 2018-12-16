import numpy as np


def sign(a):
    return (a > 0) - (a < 0)


class Car(object):
    def __init__(self, x, y, orientation):
        """
        :param orientation: 1 |, 2 /, 3, -, 4, \ (sign +ve clockwise, -ve anticlockwise)
        """
        self.x = x
        self.y = y
        self.orientation = orientation
        self.has_been_updated = False

        self.turn_state = 0  # 0 left, 1, right, 2 straight

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        else:
            return self.y < other.y

    def __repr__(self):
        return f"<car: x: {self.x}, y: {self.y}, o: {self.orientation}>"

    def update(self, grid):
        inc_x, inc_y = int(self.orientation.real), int(self.orientation.imag)
        self.x += inc_x
        self.y += inc_y

        if inc_y:
            sgn = -1
        else:
            sgn = +1

        next_state = grid[self.y, self.x]
        if next_state == 2:
            if self.turn_state == 0:
                self.orientation *= 0 - 1j
            elif self.turn_state == 1:
                pass
            elif self.turn_state == 2:
                self.orientation *= 0 + 1j
            self.turn_state = (self.turn_state + 1) % 3
        else:
            self.orientation *= next_state * sgn

        self.has_been_updated = True


def draw_grid(grid_to_draw, cars_to_draw):
    for i in range(len(grid_to_draw)):
        for j in range(len(grid_to_draw[0])):

            car_printed = False
            for car in cars_to_draw:
                if car.x == j and car.y == i:
                    if car.orientation == +1:
                        print(">", end="")
                    elif car.orientation == -1:
                        print("<", end="")
                    elif car.orientation == 0 - 1j:
                        print("^", end="")
                    elif car.orientation == 0 + 1j:
                        print("v", end="")
                    car_printed = True
                    break

            if car_printed:
                continue

            if grid_to_draw[i, j] == 0:
                print(" ", end="")
            elif grid_to_draw[i, j] == -1:
                print("|", end="")
            elif grid_to_draw[i, j] == +1:
                print("-", end="")
            elif grid_to_draw[i, j] == 0 + 1j:
                print("\\", end="")
            elif grid_to_draw[i, j] == 0 - 1j:
                print("/", end="")
            elif grid_to_draw[i, j] == 2:
                print("+", end="")

        print()
    print()


def check_collisions(carts):
    num_cars = len(carts)
    for i in range(num_cars):
        for j in range(i + 1, num_cars):
            if carts[i].x == carts[j].x and carts[i].y == carts[j].y:
                crash_coordinates = carts[i].x, carts[i].y
                del carts[j]
                del carts[i]
                return crash_coordinates
    return None


def parse_input(filename):
    file = open(filename)

    width, height = 0, 0
    for line in file:
        width = max(len(line.rstrip()), width)
        height += 1

    grid = np.zeros((height, width), dtype=complex)

    file.seek(0)
    carts = []
    for row, line in enumerate(file):
        for col, c in enumerate(line.rstrip()):
            if c == '|':
                grid[row, col] = -1
            elif c == '/':
                grid[row, col] = complex(0, -1)
            elif c == '-':
                grid[row, col] = 1
            elif c == '\\':
                grid[row, col] = complex(0, +1)
            elif c == '+':
                grid[row, col] = 2

            # cars
            elif c == ">":
                grid[row, col] = 1
                carts.append(Car(col, row, +1 + 0j))
            elif c == "<":
                grid[row, col] = 1
                carts.append(Car(col, row, -1 + 0j))
            elif c == "^":
                grid[row, col] = -1
                carts.append(Car(col, row, 0 - 1j))
            elif c == "v":
                grid[row, col] = -1
                carts.append(Car(col, row, 0 + 1j))

    carts.sort()
    return grid, carts


def all_updated(cars):
    for car in cars:
        if not car.has_been_updated:
            return False
    return True


def solution(filename, quit_on_first_crash, verbose=False):
    grid, carts = parse_input(filename)

    if verbose:
        draw_grid(grid, carts)

    while True:

        for car in carts:
            car.has_been_updated = False

        while not all_updated(carts):
            for car in carts:
                if car.has_been_updated:
                    continue

                car.update(grid)
                result = check_collisions(carts)

                if result:
                    if quit_on_first_crash:
                        return result
                    else:
                        # need to break as carts has been modified
                        break

        carts.sort()

        if verbose:
            draw_grid(grid, carts)

        if len(carts) == 1:
            return carts[0].x, carts[0].y


assert solution("day13.in.test", True, verbose=True) == (7, 3)

ans = solution("day13.in", True)
print("part1:", ans)

assert solution("day13.in.test2", False) == (6, 4)

ans_part2 = solution("day13.in", False)
print("part2:", ans_part2)
