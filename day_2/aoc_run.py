def part_1(raw_input):
    horizontal = 0
    vertical = 0
    # Simply go line by line and follow the commands
    for line in raw_input:
        # Split string for easier reading on command type, ex 'forward'
        command = line.split()
        if command[0] == 'forward':
            horizontal += int(command[1])
        elif command[0] == 'up':
            vertical -= int(command[1])
        elif command[0] == 'down':
            vertical += int(command[1])
    return vertical * horizontal


def part_2(raw_input):
    horizontal = 0
    vertical = 0
    aim = 0
    # Same as above, with a slight variation
    for line in raw_input:
        command = line.split()
        if command[0] == 'forward':
            horizontal += int(command[1])
            vertical += aim * int(command[1])
        elif command[0] == 'up':
            aim -= int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])
    return vertical * horizontal

