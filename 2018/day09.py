
def part1(num_players, last_marble):
    scores = dict()

    position = 0
    marbles = [0]
    for marble in range(1, last_marble + 1):
        player = marble % num_players
        position = (position + 2) % len(marbles)

        if marble % 23 == 0:
            to_remove = (position - 7 - 1) % len(marbles)
            removed_score = marbles.pop(to_remove)
            score_update = marble + removed_score


            if player not in scores:
                scores[player] = 0

            scores[player] += score_update

            position = to_remove + 2
        else:
            marbles.insert(position + 1, marble)


        print(f"[{player}] {marble}, {position}, {marbles}")

    print(scores)
    return max(scores.values())


print(part1(9, 25))
print(part1(10, 1618))
#print(part1(13, 7999))