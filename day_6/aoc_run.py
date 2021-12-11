def parse(data):
    int_data = []
    parsed = data[0].split(',')
    for line in parsed:
        int_data.append(int(line))
    return int_data


def get_answer(days, data):
    # Dynamic arrays don't scale well
    # Recursion is also slow
    # Working with a fixed array seems the best solution
    # Make 7 length array holding number of fish birthing that day
    total = 0
    cycles = []
    born_this_week = []
    for i in range(0, 7):
        cycles.append(0)
        born_this_week.append(0)
    # Initiate process from data
    for f in data:
        cycles[f] += 1

    index = 0
    for i in range(0, days):
        # Nr of fish born
        # Add the properly scheduled births
        births = cycles[index]
        # Add births for next week, and reset
        cycles[index] += born_this_week[index]
        born_this_week[index] = 0
        # Schedule proper births for next week
        cursor = (index + 2) % 7
        born_this_week[cursor] = births
        # Ensure index stays in range
        if index == 6:
            index = 0
        else:
            index += 1
    # Get total amount of fish
    for num in cycles:
        total += num
    for num in born_this_week:
        total += num
    return total


def part_1(raw_input):
    data = parse(raw_input)
    return get_answer(80, data)


def part_2(raw_input):
    data = parse(raw_input)
    return get_answer(256, data)
