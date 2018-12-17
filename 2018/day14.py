def solution(puzzle_input, part):
    scores = [3, 7]
    elf1, elf2 = 0, 1
    start = 0
    while True:

        score1 = scores[elf1]
        score2 = scores[elf2]

        scores += [int(c) for c in str(score1 + score2)]

        elf1 = (elf1 + 1 + score1) % len(scores)
        elf2 = (elf2 + 1 + score2) % len(scores)

        if part == 1:
            offset = puzzle_input
            if len(scores) >= offset + 10:
                return "".join(map(str, scores[offset:offset + 10]))
        elif part == 2:
            string_to_find = puzzle_input
            string_version = "".join(map(str, scores[start:]))

            if string_to_find in string_version:
                location = string_version.find(string_to_find)
                return start + location

            if len(scores) > len(string_to_find):
                start = len(scores) - len(string_to_find)
        else:
            assert False


assert solution(9, part=1) == "5158916779"
assert solution(5, part=1) == "0124515891"
assert solution(18, part=1) == "9251071085"
assert solution(2018, part=1) == "5941429882"

print("part1:", solution(702831, part=1))

assert solution("51589", part=2) == 9
assert solution("01245", part=2) == 5
assert solution("92510", part=2) == 18
assert solution("59414", part=2) == 2018

print("part2:", solution("702831", part=2))
