from blist import blist  # high performance for large lists


def part1(num_players, last_marble, verbose=False):
    scores = dict()

    for player in range(num_players):
        scores[player] = 0

    position = 1
    marbles = blist([0, 1])
    for marble in range(2, last_marble + 1):
        player = marble % num_players

        if marble % 23 == 0:
            to_remove = (position - 7) % len(marbles)
            removed_score = marbles.pop(to_remove)
            score_update = marble + removed_score
            scores[player] += score_update
            position = to_remove
        else:
            position = ((position + 1) % len(marbles)) + 1
            marbles.insert(position, marble)

        if verbose:
            print(f"[{player}] {marble}, {position}, {marbles}")

    if verbose:
        print(scores)
    return max(scores.values())


assert part1(9, 25, verbose=True) == 32
assert part1(10, 1618) == 8317
assert part1(13, 7999) == 146373
assert part1(30, 5807) == 37305

ans_part1 = part1(435, 71184)
print("part1:", ans_part1)

ans_part2 = part1(435, 71184 * 100)
print("part2:", ans_part2)
