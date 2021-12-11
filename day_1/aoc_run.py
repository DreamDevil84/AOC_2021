def part_1(raw_input):
    # Compare lines to see if the current one is greater than the previous one
    previous = 0
    # Count starts at -1 to simplify loop
    count = -1
    for line in raw_input:
        depth = int(line)
        if depth > previous:
            count += 1
        previous = depth

    return count


def part_2(raw_input):
    # Parse string array into an int array for easier management
    data = []
    for line in raw_input:
        data.append(int(line))

    previous = 0
    count = -1
    for i in range(0, len(data) - 2):
        depth = data[i] + data[i+1] + data[i+2]
        if depth > previous:
            count += 1
        previous = depth
    return count
