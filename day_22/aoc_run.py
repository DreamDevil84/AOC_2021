class Cuboid:
    def __init__(self, corner_1: [int], corner_2: [int], is_on):
        min_corner = [0, 0, 0]
        max_corner = [0, 0, 0]

        for i in range(len(corner_1)):
            if corner_1[i] < corner_2[i]:
                min_corner[i] = corner_1[i]
                max_corner[i] = corner_2[i] + 1
            else:
                min_corner[i] = corner_2[i]
                max_corner[i] = corner_1[i] + 1

        self.is_positive_cube = is_on

        self.front_bottom_left = min_corner
        self.front_bottom_right = [max_corner[0], min_corner[1], min_corner[2]]
        self.front_top_left = [min_corner[0], max_corner[1], min_corner[2]]
        self.front_top_right = [max_corner[0], max_corner[1], min_corner[2]]

        self.rear_bottom_left = [min_corner[0], min_corner[1], max_corner[2]]
        self.rear_bottom_right = [max_corner[0], min_corner[1], max_corner[2]]
        self.rear_top_left = [min_corner[0], max_corner[1], max_corner[2]]
        self.rear_top_right = max_corner

        self.x_min = min_corner[0]
        self.x_max = max_corner[0]
        self.y_min = min_corner[1]
        self.y_max = max_corner[1]
        self.z_min = min_corner[2]
        self.z_max = max_corner[2]

        self.x_range = [self.x_min, self.x_max]
        self.y_range = [self.y_min, self.y_max]
        self.z_range = [self.z_min, self.z_max]

        self.corner_array = [
            self.front_bottom_left,
            self.front_bottom_right,
            self.front_top_left,
            self.front_top_right,
            self.rear_bottom_left,
            self.rear_bottom_right,
            self.rear_top_left,
            self.rear_top_right
        ]

        self.edge_array = [
            # X edges
            [
                [
                    self.front_bottom_left,
                    self.front_bottom_right
                ],
                [
                    self.front_top_left,
                    self.front_top_right
                ],
                [
                    self.rear_bottom_left,
                    self.rear_bottom_right
                ],
                [
                    self.rear_top_left,
                    self.rear_top_right
                ],
            ],
            # Y edges
            [
                [
                    self.front_bottom_left,
                    self.front_top_left
                ],
                [
                    self.front_bottom_right,
                    self.front_top_right
                ],
                [
                    self.rear_bottom_left,
                    self.rear_top_left
                ],
                [
                    self.rear_bottom_right,
                    self.rear_top_right
                ]
            ],
            # Z edges
            [
                [
                    self.front_bottom_left,
                    self.rear_bottom_left
                ],
                [
                    self.front_top_left,
                    self.rear_top_left
                ],
                [
                    self.front_bottom_right,
                    self.rear_bottom_right
                ],
                [
                    self.front_top_right,
                    self.rear_top_right
                ]
            ]
        ]

        self.side_array = [
            [
                self.front_bottom_left,
                self.front_top_left,
                self.front_top_right,
                self.front_bottom_right
            ],
            [
                self.front_bottom_left,
                self.front_top_left,
                self.rear_top_left,
                self.rear_bottom_left
            ],
            [
                self.front_bottom_left,
                self.front_bottom_right,
                self.rear_bottom_right,
                self.rear_bottom_left
            ],
            [
                self.front_top_left,
                self.front_top_right,
                self.rear_top_right,
                self.rear_top_left
            ],
            [
                self.front_top_right,
                self.front_bottom_right,
                self.rear_bottom_right,
                self.rear_top_right
            ],
            [
                self.rear_bottom_left,
                self.rear_bottom_right,
                self.rear_top_right,
                self.rear_top_left
            ]
        ]

    def generate_corner_cuboids(self, foreign_cuboid):
        # 8 corner cases
        x_checks = [
            [
                (
                        self.x_min < foreign_cuboid.x_min < self.x_max
                ),
                [
                    self.x_min,
                    foreign_cuboid.x_min
                ]
            ],
            [
                (
                        self.x_min < foreign_cuboid.x_max < self.x_max
                ),
                [
                    foreign_cuboid.x_max,
                    self.x_max
                ]
            ]
        ]

        y_checks = [
            [
                (
                        self.y_min < foreign_cuboid.y_min < self.y_max
                ),
                [
                    self.y_min,
                    foreign_cuboid.y_min
                ]
            ],
            [
                (
                        self.y_min < foreign_cuboid.y_max < self.y_max
                ),
                [
                    foreign_cuboid.y_max,
                    self.y_max
                ]
            ]
        ]

        z_checks = [
            [
                (
                        self.z_min < foreign_cuboid.z_min < self.z_max
                ),
                [
                    self.z_min,
                    foreign_cuboid.z_min
                ]
            ],
            [
                (
                        self.z_min < foreign_cuboid.z_max < self.z_max
                ),
                [
                    foreign_cuboid.z_max,
                    self.z_max
                ]
            ]
        ]

        cubes = []

        for x in x_checks:
            for y in y_checks:
                for z in z_checks:
                    if x[0] and y[0] and z[0]:
                        min_corner = [x[1][0], y[1][0], z[1][0]]
                        max_corner = [x[1][1], y[1][1], z[1][1]]
                        cubes.append(Cuboid(min_corner, max_corner, True))
        return cubes

    def generate_edge_cuboids(self, foreign_cuboid):
        # 12 edge cases
        edge_cubes = []

        def edge_present(edge_in_array, e_type):
            if e_type == 0:
                if (
                    e_type[0][1] == e_type[1][1] and e_type[0][2] == e_type[1][2] and
                    e_type[0][0] < self.x_max and self.x_min < e_type[1][0]
                ):
                    return True
            elif e_type == 1:
                if (
                    e_type[0][0] == e_type[1][0] and e_type[0][2] == e_type[1][2] and
                    e_type[0][1] < self.y_max and self.y_min < e_type[1][1]
                ):
                    return True
            elif e_type == 2:
                if (
                    e_type[0][0] == e_type[1][0] and e_type[0][1] == e_type[1][1] and
                    e_type[0][2] < self.z_max and self.z_min < e_type[1][2]
                ):
                    return True
            return False

        def edge_cube(edge_points):
            min_corner = [0, 0, 0]
            max_corner = [0, 0, 0]
            if not edge_points[0][0] == edge_points[1][0]:
                corner_1 = edge_points[0]
                if edge_points[0][0] < self.x_min:
                    corner_1[0] = self.x_min

                if edge_points[1][1] == foreign_cuboid.y_min:
                    y = self.y_min
                else:
                    y = self.y_max

                if edge_points[1][2] == foreign_cuboid.z_min:
                    z = self.z_min
                else:
                    z = self.z_max
                corner_2 = [edge_points[1][0], y, z]
                if edge_points[1][0] > self.x_max:
                    corner_2[0] = self.x_max

            elif not edge_points[0][1] == edge_points[1][1]:
                corner_1 = edge_points[0]
                if edge_points[0][1] < self.y_min:
                    corner_1[1] = self.y_min

                if edge_points[1][0] == foreign_cuboid.x_min:
                    x = self.x_min
                else:
                    x = self.x_max

                if edge_points[1][2] == foreign_cuboid.z_min:
                    z = self.z_min
                else:
                    z = self.z_max
                corner_2 = [x, edge_points[1][1], z]
                if edge_points[1][1] > self.y_max:
                    corner_2[1] = self.y_max

            else:
                corner_1 = edge_points[0]
                if edge_points[0][2] < self.z_min:
                    corner_1[2] = self.z_min

                if edge_points[1][0] == foreign_cuboid.x_min:
                    x = self.x_min
                else:
                    x = self.x_max

                if edge_points[1][1] == foreign_cuboid.y_min:
                    y = self.y_min
                else:
                    y = self.y_max
                corner_2 = [x, y, edge_points[1][2]]
                if edge_points[1][2] > self.z_max:
                    corner_2[2] = self.z_max

            for i in range(len(corner_1)):
                if corner_1[i] < corner_2[i]:
                    min_corner[i] = corner_1[i]
                    max_corner[i] = corner_2[i] - 1
                else:
                    min_corner[i] = corner_2[i]
                    max_corner[i] = corner_1[i] - 1
            cube = Cuboid(min_corner, max_corner, True)
            return cube

        for edge_type in range(len(foreign_cuboid.edge_array)):
            for edge in foreign_cuboid.edge_array[edge_type]:
                if edge_present(edge, edge_type):
                    edge_cubes.append(edge_cube(edge))

        return edge_cubes

    def calculate_volume(self):
        return (self.x_max + 1 - self.x_min) * (self.y_max + 1 - self.y_min) * (self.z_max + 1 - self.z_min)

    def corner_intersections(self, foreign_cuboid):
        corners_within_this_cube = []
        for index in range(len(foreign_cuboid.corner_array)):
            if (
                self.x_min <= foreign_cuboid.corner_array[index][0] <= self.x_max and
                self.y_min <= foreign_cuboid.corner_array[index][1] <= self.y_max and
                self.z_min <= foreign_cuboid.corner_array[index][2] <= self.z_max
            ):
                corners_within_this_cube.append(index)
        return corners_within_this_cube

    # Split self returns array of new cubes to add
    def split_self(self, foreign_cuboid) -> [object]:
        new_cubes = []

        corner_cubes = self.generate_corner_cuboids(foreign_cuboid)
        edge_cubes = self.generate_edge_cuboids(foreign_cuboid)

        for cube in corner_cubes:
            new_cubes.append(cube)

        for cube in edge_cubes:
            new_cubes.append(cube)

        return new_cubes

    def __str__(self):
        return str(self.x_min) + '..' + str(self.x_max) + ', ' + str(self.y_min) + '..' + str(self.y_max) + ', ' + str(self.z_min) + '..' + str(self.z_max)


def parse(string_array):
    instructions = []
    for line in string_array:
        string = line
        on = True
        x_start = 0
        x_end = 0
        y_start = 0
        y_end = 0
        z_start = 0
        z_end = 0
        if 'off' in line:
            on = False
        x_start_string_start = string.index('x=') + 2
        x_start_string_end = string.index('..')
        x_start = int(string[x_start_string_start:x_start_string_end])
        x_end_string_start = string.index('..') + 2
        x_end_string_end = string.index(',')
        x_end = int(string[x_end_string_start:x_end_string_end])
        string = string[x_end_string_end + 1:]

        y_start_string_start = string.index('y=') + 2
        y_start_string_end = string.index('..')
        y_start = int(string[y_start_string_start:y_start_string_end])
        y_end_string_start = string.index('..') + 2
        y_end_string_end = string.index(',')
        y_end = int(string[y_end_string_start:y_end_string_end])
        string = string[y_end_string_end + 1:]

        z_start_string_start = string.index('z=') + 2
        z_start_string_end = string.index('..')
        z_start = int(string[z_start_string_start:z_start_string_end])
        z_end_string_start = string.index('..') + 2
        z_end = int(string[z_end_string_start:])

        instructions.append([on, [x_start, x_end, y_start, y_end, z_start, z_end]])
    return instructions


def part_1(raw_input):
    instructions = parse(raw_input)

    # Part 1 max range is -50 ... 50
    # Can be done with a 3d array of bools

    cubes = []

    for x in range(-50, 51):
        slides = []
        for y in range(-50, 51):
            rows = []
            for z in range(-50, 51):
                rows.append(False)
            slides.append(rows)
        cubes.append(slides)

    for instruction in instructions:
        run_instruction = True
        for index in instruction[1]:
            if index < -50 or index > 50:
                run_instruction = False
        if run_instruction:
            x_min = instruction[1][0]
            x_max = instruction[1][1]
            y_min = instruction[1][2]
            y_max = instruction[1][3]
            z_min = instruction[1][4]
            z_max = instruction[1][5]
            for x in range(x_min, x_max + 1):
                for y in range(y_min, y_max + 1):
                    for z in range(z_min, z_max + 1):
                        cubes[x][y][z] = instruction[0]

    cubes_active = 0

    for x in cubes:
        for y in x:
            for z in y:
                if z:
                    cubes_active += 1

    return cubes_active


def part_2(raw_input):

    # Cuboids are kept in a dictionary
    cubes = {}
    instructions = parse(raw_input)

    def run_instructions():
        # Ever-changing cuboid dictionary requires new names, always increments
        cube_id = 0
        for instruction in instructions:
            cube_start_point = [instruction[1][0], instruction[1][2], instruction[1][4]]
            cube_end_point = [instruction[1][1], instruction[1][3], instruction[1][5]]
            cube = Cuboid(cube_start_point, cube_end_point, instruction[0])
            cubes_to_change = []

            for key in cubes.keys():
                new_cubes = cubes[key].split_self(cube)
                if len(new_cubes) > 0:
                    cubes_to_change.append([False, key])
                    for new_cube in new_cubes:
                        cubes_to_change.append([True, cube_id, new_cube])
                        cube_id += 1

            for new_cube in cubes_to_change:
                if new_cube[0]:
                    cubes[new_cube[1]] = new_cube[2]
                else:
                    cubes.pop(new_cube[1])

            if cube.is_positive_cube:
                cubes[cube_id] = cube
                cube_id += 1

    def make_cubes():  # DEV FUNCTION
        cube_id = 0
        for instruction in instructions:
            cube_start_point = [instruction[1][0], instruction[1][2], instruction[1][4]]
            cube_end_point = [instruction[1][1], instruction[1][3], instruction[1][5]]
            cube = Cuboid(cube_start_point, cube_end_point, instruction[0])
            cubes[cube_id] = cube
            cube_id += 1

    # make_cubes()
    run_instructions()

    total_volume = 0

    for x in instructions:
        print(x)

    for key_cube in cubes.keys():
        print(cubes[key_cube])
        print(cubes[key_cube].calculate_volume())
        total_volume += cubes[key_cube].calculate_volume()

    return total_volume
