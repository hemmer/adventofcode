import networkx as nx


def char_to_int(c):
    return ord(c) - 64


def int_to_char(i):
    return chr(i + 64)


def string_to_pair(string):
    string = string.split(" ")
    return char_to_int(string[1]), char_to_int(string[7])


def part1(edges):
    graph = nx.DiGraph()
    graph.add_edges_from(edges)

    starting_nodes = []
    ending_nodes = []
    for node in graph.nodes():

        if not graph.predecessors(node):
            starting_nodes.append(node)

        if not graph.successors(node):
            ending_nodes.append(node)

    starting_nodes = sorted(starting_nodes, reverse=True)
    print("starts:", starting_nodes)
    print("ends:", ending_nodes)
    assert len(ending_nodes) == 1

    current = starting_nodes.pop()
    stack = starting_nodes
    answer = int_to_char(current)
    while True:
        children = graph.successors(current)
        graph.remove_node(current)

        stack = sorted(set(children + stack))

        for node in stack:
            if not graph.predecessors(node):
                current = node
                stack.remove(node)
                break

        answer += int_to_char(current)

        if not stack:
            break

    return answer


test_input_file = open('day07.in.test')
test_sequence = [string_to_pair(line) for line in test_input_file]

assert part1(test_sequence) == "CABDFE"
print()

input_file = open('day07.in')
sequence = [string_to_pair(line) for line in input_file]
ans1 = part1(sequence)
print("part1:", ans1)
