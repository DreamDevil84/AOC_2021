def parse(data):
    int_array = []
    for line in data:
        new_line = []
        for char in line:
            new_line.append(int(char))
        int_array.append(new_line)
    return int_array


def part_1(raw_input):
    # Convert to 2d int array
    heat_map = parse(raw_input)
    risk_level = 0
    # Simply check each cell and their neighbors
    for y in range(0, len(heat_map)):
        for x in range(0, len(heat_map[0])):
            val = heat_map[y][x]
            is_low_point = True
            neighbors = []
            if y > 0:
                neighbors.append(heat_map[y - 1][x])
            if y < len(heat_map) - 1:
                neighbors.append(heat_map[y + 1][x])
            if x > 0:
                neighbors.append(heat_map[y][x - 1])
            if x < len(heat_map[0]) - 1:
                neighbors.append(heat_map[y][x + 1])
            for num in neighbors:
                if num <= val:
                    is_low_point = False
            if is_low_point:
                risk_level += val + 1

    return risk_level


def part_2(raw_input):
    heat_map = parse(raw_input)
    # Find a low point

    set_list = []

    def string_convert(height, width):
        return str(height) + '_' + str(width)

    def position_convert(string_position: str):
        string_split = string_position.split('_')
        return [int(string_split[0]), int(string_split[1])]

    def recurse(y_pos, x_pos, basin_set: set):
        new_set = basin_set
        if y_pos > 0:
            if not heat_map[y_pos - 1][x_pos] == 9:
                # Check to see if it is in the set already, if not, add it and continue
                string_val = string_convert(y_pos - 1, x_pos)
                if string_val not in new_set:
                    new_set.add(string_val)
                    new_set = recurse(y_pos - 1, x_pos, new_set)
        if y_pos < len(heat_map) - 1:
            if not heat_map[y_pos + 1][x_pos] == 9:
                # Check to see if it is in the set already, if not, add it and continue
                string_val = string_convert(y_pos + 1, x_pos)
                if string_val not in new_set:
                    new_set.add(string_val)
                    new_set = recurse(y_pos + 1, x_pos, new_set)
        if x_pos > 0:
            if not heat_map[y_pos][x_pos - 1] == 9:
                # Check to see if it is in the set already, if not, add it and continue
                string_val = string_convert(y_pos, x_pos - 1)
                if string_val not in new_set:
                    new_set.add(string_val)
                    new_set = recurse(y_pos, x_pos - 1, new_set)
        if x_pos < len(heat_map[0]) - 1:
            if not heat_map[y_pos][x_pos + 1] == 9:
                # Check to see if it is in the set already, if not, add it and continue
                string_val = string_convert(y_pos, x_pos + 1)
                if string_val not in new_set:
                    new_set.add(string_val)
                    new_set = recurse(y_pos, x_pos + 1, new_set)
        return new_set

    for y in range(0, len(heat_map)):
        for x in range(0, len(heat_map[0])):
            val = heat_map[y][x]
            is_low_point = True
            neighbors = []
            this_basin_set = set(())
            if y > 0:
                neighbors.append(heat_map[y - 1][x])
            if y < len(heat_map) - 1:
                neighbors.append(heat_map[y + 1][x])
            if x > 0:
                neighbors.append(heat_map[y][x - 1])
            if x < len(heat_map[0]) - 1:
                neighbors.append(heat_map[y][x + 1])
            for num in neighbors:
                if num <= val:
                    is_low_point = False
            # Recursively add all cells that are part of the basin into a set
            if is_low_point:
                this_basin_set.add(string_convert(y, x))
                this_basin_set = recurse(y, x, this_basin_set)
            if len(this_basin_set) > 0:
                set_list.append(this_basin_set)

    # Find the three largest sets
    # Sort the list by largest length to smallest
    set_list.sort(key=len, reverse=True)
    # Multiply three largest
    answer = len(set_list[0])
    for i in range(1, 3):
        answer *= len(set_list[i])
    return answer
