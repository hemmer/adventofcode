def solution(data):
    def index(i, depth):
        num_children, num_metadata = data[i], data[i + 1]

        position = i + 2
        scores = {}
        metadata_sum = 0
        for j in range(1, num_children + 1):
            position, child_metadata_sum, node_value = index(position, depth + 1)
            metadata_sum += child_metadata_sum
            scores[j] = node_value

        metadata = data[position:position + num_metadata]

        if num_children == 0:
            node_value = sum(metadata)
        else:
            node_value = 0
            for m in metadata:
                if m in scores:
                    node_value += scores[m]

        metadata_sum += sum(metadata)
        position += + num_metadata
        return position, metadata_sum, node_value

    pos, total, score = index(0, 1)

    return total, score


test_data = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

assert solution(test_data) == (138, 66)

input_file = open('day08.in')
sequence = []
for line in input_file:
    for value in line.rstrip().split(" "):
        sequence.append(int(value))

part1, part2 = solution(sequence)
print("part1:", part1)
print("part2:", part2)
