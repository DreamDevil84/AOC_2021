def parse(string):
    coordinates_strings = string[13:].split(', ')
    array = []
    for line in coordinates_strings:
        a = line[2:].split('..')
        row = []
        for n in a:
            row.append(int(n))
        array.append(row)
    return array


def part_1(raw_input):
    target_coordinates = parse(raw_input[0])
    # Extract boundaries
    # x doesnt matter for part 1, so we don't need it
    y_start = target_coordinates[1][0]
    y_end = target_coordinates[1][1]

    # No matter the velocity, the probe will always reach a height of 0 on the way down
    # Total velocity must be equal to the smallest y value in the step after reaching 0
    # Thus the velocity will be the absolute value of y_start + 1

    # Partial sum gives us the answer
    n = abs(y_start + 1)

    return int(((n * n) + n) / 2)


def part_2(raw_input):
    target_coordinates = parse(raw_input[0])
    # Extract boundaries
    x_start = target_coordinates[0][0]
    x_end = target_coordinates[0][1]
    y_start = target_coordinates[1][0]
    y_end = target_coordinates[1][1]

    # x velocity moves 1 towards 0 each step
    # y velocity decreases by 1 each step
    # Minimum x velocity will stop at smallest x that surpasses x_start
    # Maximum x velocity equals x_end
    # Use partial sum to find these
    x_min = 0
    x_max = x_end
    num = 1
    while True:
        if (num * num + num) / 2 >= x_start:
            x_min = num
            break
        num += 1

    # As found in part 1, maximum y velocity will be the absolute value of y_start + 1
    # Minimum y velocity equals y_start
    y_max = abs(y_start + 1)
    y_min = y_start
    # Create array for each step that x/y is within target bounds

    all_velocities_nr = 0
    all_velocities = []

    def hits_within_bounds(velocity):
        x_speed = velocity[0]
        y_speed = velocity[1]
        x_pos = 0
        y_pos = 0
        while True:
            x_pos += x_speed
            y_pos += y_speed
            if x_speed > 0:
                x_speed -= 1
            y_speed -= 1
            if x_start <= x_pos <= x_end and y_start <= y_pos <= y_end:
                return True
            if x_end < x_pos or y_pos < y_start:
                return False

    # Loop through all velocity combinations
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if hits_within_bounds([x, y]):
                all_velocities_nr += 1
                all_velocities.append([x, y])

    return all_velocities_nr
