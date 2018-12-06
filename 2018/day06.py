import numpy as np

def manhattan(p1, p2):
    return np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1])


points = np.array([(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])


print(manhattan(points[0], points[1]))


def debug(points):

    min_x, max_x = points[:, 0].min(), points[:, 0].max()
    min_y, max_y = points[:, 1].min(), points[:, 1].max()

    for i, point in enumerate(points):
        print(chr(i+97), point)

    for y in range(min_y-5, max_y+5):
        for x in range(min_x-5, max_x+5):

            distances = np.array([manhattan(point, (x, y)) for i, point in enumerate(points)])
            winners = np.where(distances == distances.min())[0]

            if len(winners) > 1:
                print(".", end="")
            else:
                print(chr(winners[0]+97), end="")

        print()



debug(points)