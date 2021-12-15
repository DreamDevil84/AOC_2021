class Node:
    def __init__(self, node_id: str, weight: int, total_weight: int, neighbours: {str}):
        self.node_id = node_id
        self.weight = weight
        self.total_weight = total_weight
        self.neighbours = neighbours

    def __str__(self):
        return str(self.total_weight)


def generate_graph(data, max_value):
    # Use dictionary for quick access
    dictionary = {}
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            id_str = str(x) + '_' + str(y)
            neighbours = set()
            if y > 0:
                neighbours.add(str(x) + '_' + str(y - 1))
            if y < len(data) - 1:
                neighbours.add(str(x) + '_' + str(y + 1))
            if x > 0:
                neighbours.add(str(x - 1) + '_' + str(y))
            if x < len(data[0]) - 1:
                neighbours.add(str(x + 1) + '_' + str(y))
            
            dictionary[id_str] = Node(id_str, data[y][x], max_value, neighbours)
    return dictionary


def str_to_int_2d_array(data):
    array = []
    for line in data:
        row = []
        for char in line:
            row.append(int(char))
        array.append(row)
    return array


def expand_array(data):
    array = []
    for y_multiplier in range(5):
        for y in range(len(data)):
            row = []
            for x_multiplier in range(5):
                for x in range(len(data[0])):
                    num = data[y][x] + y_multiplier + x_multiplier
                    if num > 9:
                        num -= 9
                    row.append(num)
            array.append(row)

    return array


def part_1(raw_input):
    # Convert string array to int array
    data = str_to_int_2d_array(raw_input)
    # Get max value
    max_value = 0
    for row in data:
        for num in row:
            max_value += num

    # Create graph of Chitons
    graph = generate_graph(data, max_value)
    # Generate set of searched Chitons, initially with the starting node
    searched = {'0_0'}

    graph['0_0'].total_weight = 0

    # Loop through, code is a bit ugly
    for y in range(len(data)):
        for x in range(len(data[0])):
            node = graph[str(y) + '_' + str(x)]
            searched.add(node.node_id)
            for neighbour in node.neighbours:
                for next_neighbour in graph[neighbour].neighbours:
                    if graph[next_neighbour].total_weight + graph[neighbour].weight < graph[neighbour].total_weight:
                        graph[neighbour].total_weight = graph[next_neighbour].total_weight + graph[neighbour].weight

    destination = str(len(data) - 1) + '_' + str(len(data[0]) - 1)
    return graph[destination]


def part_2(raw_input):
    # Basically the same as part 1, just takes longer
    # Convert string array to int array
    print('One moment, this may take a few seconds...')
    data = str_to_int_2d_array(raw_input)
    # Expand array
    data = expand_array(data)

    # Get max value
    max_value = 0
    for row in data:
        for num in row:
            max_value += num

    graph = generate_graph(data, max_value)
    searched = {'0_0'}

    graph['0_0'].total_weight = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            node = graph[str(y) + '_' + str(x)]
            searched.add(node.node_id)
            for neighbour in node.neighbours:
                for next_neighbour in graph[neighbour].neighbours:
                    if graph[next_neighbour].total_weight + graph[neighbour].weight < graph[neighbour].total_weight:
                        graph[neighbour].total_weight = graph[next_neighbour].total_weight + graph[neighbour].weight

    destination = str(len(data) - 1) + '_' + str(len(data[0]) - 1)
    return graph[destination]
