def str_to_bools(string):
    return [True if c == "#" else False for c in string]


def print_state(bools, time):
    print(f"{time:#03d}", end="")

    for b in bools:
        if b:
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
    current_state = []
    for j in range(2, len(state) - 2):
        current_state.append(bools_to_binary(state[j - 2:j + 2 + 1]))
    return [0] * 2 + current_state + [0] * 2


def get_state_and_rules(filename):
    input_file = open(filename)
    update_rules = dict()
    for i, line in enumerate(input_file):
        line = line.rstrip()
        if i == 0:
            leftmost_index = -20
            initial_state_bools = [False] * abs(leftmost_index) + \
                                  str_to_bools(line.split("initial state: ")[1]) + [False] * abs(leftmost_index)

        elif i > 1:
            pattern, result = line.split(" => ")
            pattern_binary, result_binary = str_to_binary(pattern), str_to_binary(result)
            print("pat", pattern, result, pattern_binary, result_binary)
            update_rules[pattern_binary] = result_binary

    return initial_state_bools, update_rules, leftmost_index

def part1(filename, tmax = 20):
    current_state, update_rules, leftmost_index = get_state_and_rules(filename)

    print(update_rules)

    print_state(current_state, 0)
    current_state = bool_state_to_int(current_state)


    for t in range(1, tmax + 1):

        bool_state = []
        for value in current_state:
            if value in update_rules:
                if update_rules[value]:
                    bool_state.append(True)
                else:
                    bool_state.append(False)
            else:
                bool_state.append(False)

        print_state(bool_state, t)
        current_state = bool_state_to_int(bool_state)


    print_state(bool_state, t)

    ans = sum(i + leftmost_index for i, state in enumerate(bool_state) if state)
    return ans

assert part1("day12.in.test") == 325

ans_part1 = part1("day12.in")
print(ans_part1)

ans_part1 = part1("day12.in", tmax=10000)
