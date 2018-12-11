import numpy as np


class Point():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def update(self):
        self.pos += self.vel
        return self.pos


def file_to_data(input_file):
    sequence = []
    for line in input_file:
        position, velocity = line.rstrip().split("> velocity=<")

        positions = np.array(list(map(int, position.split("<")[1].split(", "))))
        velocities = np.array(list(map(int, velocity.rstrip(">").split(", "))))

        sequence.append(Point(positions, velocities))

    return sequence


def solution(sequence):
    tmax = 12000
    min_area = None
    for t in range(tmax):

        latest = []
        for point in sequence:
            latest.append(point.update())

        latest = np.array(latest)
        minx, miny = int(latest[:, 0].min()), int(latest[:, 1].min())
        maxx, maxy = int(latest[:, 0].max()), int(latest[:, 1].max())

        do_print = False
        area = (maxy - miny) * (maxx - minx)
        if min_area:
            min_area = min(area, min_area)
            if area > min_area:
                do_print = True
        else:
            min_area = area

        if area < 1000:
            do_print = True

        if do_print:
            for j in range(miny, maxy + 1):
                for i in range(minx, maxx + 1):

                    found = False
                    for point in sequence:
                        if np.array_equal(point.pos, np.array([i, j])):
                            found = True
                            break

                    if found:
                        print("#", end="")
                    else:
                        print(".", end="")

                print()

            return t + 1


input_file = open('day10.in')
sequence = file_to_data(input_file)
part2_ans = solution(sequence)

print("part02:", part2_ans)
