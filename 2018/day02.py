from collections import Counter
import numpy as np


def part1(string_list):
    num_two, num_three = 0, 0
    for string in string_list:
        c = Counter(string)

        counts = [val for _, val in c.most_common(None)]

        if 2 in counts:
            num_two += 1
        if 3 in counts:
            num_three += 1

    return num_two * num_three


def part2(string_list):
    def to_int(string):
        return np.array([ord(s) for s in string])

    for i in range(len(string_list)):
        s1 = to_int(string_list[i])
        for j in range(i + 1, len(string_list)):
            s2 = to_int(string_list[j])

            nonzero = np.nonzero(s1 - s2)[0]

            if len(nonzero) == 1:
                pos = nonzero[0]
                return string_list[i][:pos] + string_list[i][(pos + 1):]


test_list_part1 = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
assert part1(test_list_part1) == 12

test_list_part2 = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
assert part2(test_list_part2) == "fgij"

input_file = open('day02.in')
sequence = [line.rstrip() for line in input_file]
print("part1:", part1(sequence))
print("part2:", part2(sequence))
