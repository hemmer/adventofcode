from collections import defaultdict


class KeyDict(defaultdict):
    def __missing__(self, key):
        return False


test_dict = KeyDict()
test_dict[1] = True
assert test_dict[1] and not test_dict[0]


def str_to_bools(string):
    return [True if c == "#" else False for c in string]


def print_state(state: KeyDict, time, start=-2, end=150):
    print(f"{time:#03d}", end="")

    for j in range(start, end):
        if state[j]:
            print("#", end="")
        else:
            print(".", end="")
    print()


def str_to_binary(string):
    binary_string = ""
    for c in string[::-1]:
        if c == "#":
            binary_string = "1" + binary_string
        else:
            binary_string = "0" + binary_string
    return int(binary_string, 2)


assert str_to_binary("#.#.#") == 21
assert str_to_binary("..###") == 7


def bools_to_binary(bools):
    binary_string = ""
    for b in bools[::-1]:
        if b:
            binary_string = "1" + binary_string
        else:
            binary_string = "0" + binary_string

    return int(binary_string, 2)


assert bools_to_binary([True, False, True, True]) == 11


def bool_state_to_int(state):
    start, end = min(state.keys()) - 2, max(state.keys()) + 2

    current_state = KeyDict()
    for j in range(start, end + 1):
        bools = [state[j - 2], state[j - 1], state[j], state[j + 1], state[j + 2]]
        current_state[j] = bools_to_binary(bools)

    return current_state


def bools_to_dict(bools, leftmost_index) -> KeyDict:
    result = KeyDict()
    for j, b in enumerate(bools):
        if b:
            result[leftmost_index + j] = True

    return result


def get_state_and_rules(filename):
    input_file = open(filename)
    initial_state, update_rules = None, dict()

    for i, line in enumerate(input_file):
        line = line.rstrip()
        if i == 0:

            initial_state_bools = str_to_bools(line.split("initial state: ")[1])

            leftmost_index = 0
            initial_state = bools_to_dict(initial_state_bools, leftmost_index)

        elif i > 1:
            pattern, result = line.split(" => ")
            pattern_binary, result_binary = str_to_binary(pattern), str_to_binary(result)
            update_rules[pattern_binary] = result_binary

    return initial_state, update_rules


def part1(filename, tmax=20, do_print=False):
    current_state, update_rules = get_state_and_rules(filename)
    current_state = bool_state_to_int(current_state)

    for t in range(1, tmax + 1):

        bool_state = KeyDict()
        for key, value in current_state.items():
            if value in update_rules:
                if update_rules[value]:
                    bool_state[key] = True

        current_state = bool_state_to_int(bool_state)

        if do_print:
            print_state(bool_state, t)

    pot_sum = sum(pot for pot in bool_state.keys())

    return pot_sum, bool_state


assert part1("day12.in.test")[0] == 325

ans_part1, _ = part1("day12.in", do_print=True)
print("part1:", ans_part1)

ans_part2, bool_state_part2 = part1("day12.in", tmax=1000)

# state repeats, so convert from known state at time 1000 to that required
start_point = 50000000000 - 58
new_dict = KeyDict()
for key, value in bool_state_part2.items():
    new_key = key - 942 + start_point
    new_dict[new_key] = value

part2_ans = sum(pot for pot, state in new_dict.items() if state)
print("part2:", part2_ans)
