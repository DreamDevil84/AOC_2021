class ThermalVentDiagram:
    def __init__(self, array):
        x_max = 0
        y_max = 0
        for line in array:
            for coord in line:
                if coord[0] > x_max:
                    x_max = coord[0]
                if coord[1] > y_max:
                    y_max = coord[1]
        self.diagram = []
        for y in range(0, y_max+1):
            entry = []
            for x in range (0, x_max+1):
                entry.append(0)
            self.diagram.append(entry)

    def find_straight_vents(self, array):
        for coord in array:
            x1 = coord[0][0]
            x2 = coord[1][0]
            y1 = coord[0][1]
            y2 = coord[1][1]

            # Vertical Line
            if x1 == x2:
                if y1 < y2:
                    for y in range(y1, y2+1):
                        self.diagram[y][x1] += 1
                else:
                    for y in range(y2, y1+1):
                        self.diagram[y][x1] += 1
            # Horizontal Line
            if y1 == y2:
                if x1 < x2:
                    for x in range(x1, x2+1):
                        self.diagram[y1][x] += 1
                else:
                    for x in range(x2, x1+1):
                        self.diagram[y1][x] += 1

    def find_diagonal_lines(self, array):
        for coord in array:
            x1 = coord[0][0]
            x2 = coord[1][0]
            y1 = coord[0][1]
            y2 = coord[1][1]

            if not x1 == x2 and not y1 == y2:
                left_to_right = True
                y_start = y1
                y_end = y2
                if y1 < y2:
                    x = x1
                    if x1 > x2:
                        left_to_right = False

                if y1 > y2:
                    y_start = y2
                    y_end = y1
                    x = x2
                    if x2 > x1:
                        left_to_right = False

                for y in range(y_start, y_end+1):
                    if left_to_right:
                        self.diagram[y][x] += 1
                        x += 1
                    else:
                        self.diagram[y][x] += 1
                        x -= 1

    def danger_points_nr(self):
        count = 0
        for line in self.diagram:
            for cell in line:
                if cell > 1:
                    count += 1
        return count

    def __str__(self):
        diagram_string = ""
        for line in self.diagram:
            row = ""
            for cell in line:
                if cell == 0:
                    row += '.'
                else:
                    row += str(cell)
            row += '\n'
            diagram_string += row
        return diagram_string


def create_coordinate_array(string_array):
    coord_array = []
    for line in string_array:
        # Split string into start and finish
        coord = line.split(' -> ')
        # Convert to int
        start = coord[0].split(',')
        end = coord[1].split(',')
        int_coord = [
            [
                int(start[0]),
                int(start[1])
            ],
            [
                int(end[0]),
                int(end[1])
            ]
        ]
        coord_array.append(int_coord)
    return coord_array


def part_1(raw_input):
    coordinates = create_coordinate_array(raw_input)
    diagram = ThermalVentDiagram(coordinates)
    diagram.find_straight_vents(coordinates)
    return diagram.danger_points_nr()


def part_2(raw_input):
    coordinates = create_coordinate_array(raw_input)
    diagram = ThermalVentDiagram(coordinates)
    diagram.find_straight_vents(coordinates)
    diagram.find_diagonal_lines(coordinates)
    return diagram.danger_points_nr()
