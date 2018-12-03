from collections import Counter
from itertools import accumulate


def part1(sequence):
    return list(accumulate(sequence))[-1]


assert part1([+1, +1, +1]) == 3
assert part1([+1, +1, -2]) == 0
assert part1([-1, -2, -3]) == -6


def part2(sequence, start=0, c=None):
    accum = list(accumulate([start] + sequence))

    if c is None:
        c = Counter(accum)
    else:
        c.update(accum[1:])

    candidates = []
    for key, val in c.most_common(None):
        if val > 1:
            candidates.append(key)

    if len(candidates) == 0:
        return part2(sequence, start=accum[-1], c=c)
    else:
        for elem in accum:
            if elem in candidates:
                return elem
        assert False


assert part2([1, -1]) == 0
assert part2([+3, +3, +4, -2, -4]) == 10
assert part2([-6, +3, +8, +5, -6]) == 5
assert part2([+7, +7, -2, -7, -4]) == 14

input_file = open('day01.in')
sequence = [int(line) for line in input_file]

print("part1:", part1(sequence))
print("part2:", part2(sequence))
