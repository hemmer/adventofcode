def part1(string):
    string_to_int = []
    for c in string:
        sign = 1
        if c.isupper(): sign = -1

        int_val = sign * (ord(c.lower()) - 96)
        string_to_int.append(int_val)

    finished = False
    while not finished:
        finished = True

        i = 1
        while i < len(string_to_int):
            c1, c2 = string_to_int[i - 1], string_to_int[i]
            if c1 + c2 == 0:
                del string_to_int[i - 1]
                del string_to_int[i - 1]

                finished = False
                continue
            else:
                i += 1

    return len(string_to_int)


def part2(string, verbose=False):
    best = len(string)
    for char in "abcdefghijklmnopqrstuvwxyz":
        string_mod = string.replace(char, "")
        string_mod = string_mod.replace(char.upper(), "")

        ans = part1(string_mod)

        best = min(best, ans)
        if verbose:
            print("   ", char, ans, best)
    return best


assert part1("dabAcCaCBAcCcaDA") == 10
assert part2("dabAcCaCBAcCcaDA") == 4

input_file = open('day05.in')
sequence = [line.rstrip() for line in input_file][0]

print("part1:", part1(sequence))
print("part2:", part2(sequence, verbose=True))
