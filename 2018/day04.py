import datetime
from collections import Counter


def parts_1_and_2(logs):
    logs.sort()
    guards = dict()

    for log in logs:
        timestamp = log[1:17]
        message = log[19:]

        stamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M")

        if "Guard" in message:
            guard = int(message.split(" ")[1][1:])
            if guard not in guards:
                guards[guard] = Counter()
        elif "falls" in message:
            start = stamp
        elif "wakes" in message:
            length = ((stamp - start).seconds // 60) % 60
            guards[guard].update([start.minute + minute for minute in range(length)])
            start = None

    worst_guard, worst_sleep = None, 0
    for guard in guards:
        total_sleep = sum(guards[guard].values())
        if total_sleep > worst_sleep:
            worst_sleep, worst_guard = total_sleep, guard

    part1 = worst_guard * guards[worst_guard].most_common(1)[0][0]

    worst_guard, worst_sleep, worst_minute = None, 0, None
    for guard in guards:
        most_common = guards[guard].most_common(1)
        if most_common:
            guards_worst_minute, max_times_asleep = most_common[0]
            if max_times_asleep > worst_sleep:
                worst_sleep = max_times_asleep
                worst_guard = guard
                worst_minute = guards_worst_minute

    part2 = worst_guard * worst_minute

    return part1, part2


input_file = open('day04.in.test')
sequence_test = [line.rstrip() for line in input_file]
assert parts_1_and_2(sequence_test) == (240, 4455)

input_file = open('day04.in')
sequence = [line.rstrip() for line in input_file]
ans_part1, ans_part2 = parts_1_and_2(sequence)
print("part1:", ans_part1)
print("part2:", ans_part2)
