class Beacon:
    def __init__(self, position):
        self.position = position
        # A list of beacons positions relative to this one
        self.relative_list = []

    def generate_list_of_relative_distances(self, beacons):
        def get_relative_position(self_p, other_p):
            return [other_p[0] - self_p[0], other_p[1] - self_p[1], other_p[2] - self_p[2]]

        for beacon_position in beacons:
            if not beacon_position == self.position:
                relative_position = get_relative_position(self.position, beacon_position)
                # If statement to prevent duplicates when adding new beacons
                if relative_position not in self.relative_list:
                    self.relative_list.append(relative_position)

    def __str__(self):
        string = 'Position: ' + str(self.position) + '\nRelative List:'
        for pos in self.relative_list:
            string += '\n' + str(pos)
        return string


class Scanner:
    def __init__(self, scanner_id, beacon_array: [[int]]):
        self.id = scanner_id
        self.beacon_list: list = beacon_array
        self.absolute_position = []
        self.has_absolute_position = False

    def adjusted_beacons(self):
        adjusted = []
        for entry in self.beacon_list:
            adjusted.append([
                entry[0] + self.absolute_position[0],
                entry[1] + self.absolute_position[1],
                entry[2] + self.absolute_position[2]
            ])
        return adjusted

    # Can calculate this scanners absolute position by comparing it to a scanner with a known absolute position
    def calculate_absolute_position(self, scanner, minimum_similar):
        # this_scanners_beacons = copy.deepcopy(self.beacon_list)
        # this_scanners_beacons = self.beacon_list
        absolute_beacons = scanner.beacon_list

        def rotate_x():
            # x gets values in order: y, z
            for index in range(len(self.beacon_list)):
                beacon = self.beacon_list[index].copy()
                # Regardless of orientation, clockwise rotation always has the same effect
                self.beacon_list[index][1] = beacon[2]
                self.beacon_list[index][2] = -beacon[1]

        def rotate_y():
            # y gets values in order: z, x
            for index in range(len(self.beacon_list)):
                beacon = self.beacon_list[index].copy()
                # Regardless of orientation, clockwise rotation always has the same effect
                self.beacon_list[index][2] = beacon[0]
                self.beacon_list[index][0] = -beacon[2]

        def rotate_z():
            # z gets values in order: x, y
            for index in range(len(self.beacon_list)):
                beacon = self.beacon_list[index].copy()
                # Regardless of orientation, clockwise rotation always has the same effect
                self.beacon_list[index][0] = beacon[1]
                self.beacon_list[index][1] = -beacon[0]

        def adjust_own_absolute_position(other_position):
            self.absolute_position = [
                self.absolute_position[0] + other_position[0],
                self.absolute_position[1] + other_position[1],
                self.absolute_position[2] + other_position[2]
            ]

        def compare_beacons(own_beacons, minimum_similarity):
            def adjusted_position(absolute_position, adjustment):
                return [
                    absolute_position[0] + adjustment[0],
                    absolute_position[1] + adjustment[1],
                    absolute_position[2] + adjustment[2]
                ]

            for beacon_position in own_beacons:
                # Create a fresh beacon from its position and a list of all scanner beacons relative positions to it
                beacon = Beacon(beacon_position)
                beacon.generate_list_of_relative_distances(own_beacons)
                similarity = 0
                # Compare this beacon to the the beacon in the absolute list
                for absolute_beacon_position in absolute_beacons:
                    for relative_position in beacon.relative_list:
                        adjusted_pos = adjusted_position(absolute_beacon_position, relative_position)
                        if adjusted_pos in absolute_beacons:
                            similarity += 1
                            if similarity >= minimum_similarity - 1:
                                self.absolute_position = [
                                    absolute_beacon_position[0] - beacon_position[0],
                                    absolute_beacon_position[1] - beacon_position[1],
                                    absolute_beacon_position[2] - beacon_position[2]
                                ]
                                self.has_absolute_position = True
                                return True
            return False
        # The scanner has 6 possible facings, with 4 rotations on each
        # Alternating facings on the x and y axis will include all facings
        for n in range(6):
            # Rotate to get all 4 rotations on a facing
            # Break function if minimum similar beacons are found in a relative list
            for r in range(4):
                if compare_beacons(self.beacon_list, minimum_similar):
                    # Absolute position of scanner is always in relation to 0, 0, 0
                    adjust_own_absolute_position(scanner.absolute_position)
                    # self.beacon_list = this_scanners_beacons
                    self.has_absolute_position = True
                    return True
                rotate_z()
            if n % 2 == 0:
                rotate_y()
            else:
                rotate_x()
        return False

    def __str__(self):
        string = '--- scanner ' + str(self.id) + ' ---'
        for line in self.beacon_list:
            string += '\n' + str(line)[1:-1]
        return string


def parse(string_array):
    beacon_array = []
    sub_array = []
    for line in string_array:
        if 'scanner' in line:
            sub_array = []
        elif line == '':
            beacon_array.append(sub_array.copy())
        else:
            num_split = line.split(',')
            num_array = []
            for num in num_split:
                num_array.append(int(num))
            sub_array.append(num_array)
    # Check if last line in string array is empty, if so append last scanner
    if not string_array[-1] == '':
        beacon_array.append(sub_array)
    return beacon_array


def part_1(raw_input):
    beacon_array = parse(raw_input)
    scanners = []

    minimum_similarity = 12

    for index in range(len(beacon_array)):
        scanner = Scanner(index, beacon_array[index])
        scanners.append(scanner)

    # Scanner 0 is the norm, so we start by setting its absolute position as the center
    scanners[0].absolute_position = [0, 0, 0]
    scanners[0].has_absolute_position = True

    print('Note: This could take a few minutes')
    emergency = 0
    while True:
        emergency += 1
        for i in range(len(scanners)):
            if not scanners[i].has_absolute_position:
                for j in range(len(scanners)):
                    if scanners[j].has_absolute_position and not i == j:
                        scanners[i].calculate_absolute_position(scanners[j], minimum_similarity)
                        if scanners[i].has_absolute_position:
                            break
        count = 0
        for scanner in scanners:
            if scanner.has_absolute_position:
                count += 1
        if count == len(scanners):
            break
        if emergency > 10000:
            print('too many loops')
            break

    beacons = []
    for scanner in scanners:
        for beacon in scanner.adjusted_beacons():
            if beacon not in beacons:
                beacons.append(beacon)

    print(len(beacons))

    # Part 2
    # Get absolute values
    abs_values = []
    for scanner in scanners:
        abs_values.append(scanner.absolute_position)

    def get_manhattan_distance(start, finish):
        return abs(start[0] - finish[0]) + abs(start[1] - finish[1]) + abs(start[2] - finish[2])

    max_manhattan = 0
    for scanner_1 in abs_values:
        for scanner_2 in abs_values:
            manhattan_value = get_manhattan_distance(scanner_1, scanner_2)
            if manhattan_value > max_manhattan:
                max_manhattan = manhattan_value

    return max_manhattan
