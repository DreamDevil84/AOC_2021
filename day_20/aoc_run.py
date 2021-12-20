class Image:
    def __init__(self, enhancement, raw_image):
        self.image = set()
        self.enhancement = enhancement
        self.even_generation = False
        for y in range(len(raw_image)):
            for x in range(len(raw_image[0])):
                if raw_image[y][x] == '#':
                    self.image.add(str(y) + '_' + str(x))

    def check_pixel(self, y, x, bounds):
        binary_string = ''
        # Deal with edge/corner cases
        # if self.enhancement[0] == '#' and self.enhancement[-1] == '.':
        #     if y in bounds:
        #         if self.even_generation:
        #             return '.'
        #         else:
        #             return '#'
        #     if x in bounds:
        #         if self.even_generation:
        #             return '.'
        #         else:
        #             return '#'
        for y_range in range(y - 1, y + 2):
            for x_range in range(x - 1, x + 2):
                coordinate = str(y_range) + '_' + str(x_range)
                if coordinate in self.image:
                    binary_string += '1'
                else:
                    binary_string += '0'
        binary_index = int(binary_string, 2)
        return self.enhancement[binary_index]

    def remove_edges(self, bounds):
        min_y = bounds[0] + 5
        max_y = bounds[1] - 5
        min_x = bounds[2] + 5
        max_x = bounds[3] - 5

        to_remove = set()

        for entry in self.image:
            coordinates = entry.split('_')
            y = int(coordinates[0])
            x = int(coordinates[1])
            if x < min_x or x > max_x or y < min_y or y > max_y:
                to_remove.add(entry)

        for entry in to_remove:
            self.image.remove(entry)


    def enhance(self):
        image_pixels_to_alter = {}

        # Determine bounds
        min_y = 0
        max_y = 0
        min_x = 0
        max_x = 0
        for entry in self.image:
            coordinates = entry.split('_')
            if int(coordinates[0]) > max_y:
                max_y = int(coordinates[0])
            elif int(coordinates[0]) < min_y:
                min_y = int(coordinates[0])

            if int(coordinates[1]) > max_x:
                max_x = int(coordinates[1])
            elif int(coordinates[1]) < min_x:
                min_x = int(coordinates[1])

        # Increase bounds to handle ever expanding size of image, but only on even generations
        if self.even_generation:
            min_y = min_y - 3
            max_y = max_y + 3
            min_x = min_x - 3
            max_x = max_x + 3
        else:
            min_y = min_y - 10
            max_y = max_y + 10
            min_x = min_x - 10
            max_x = max_x + 10

        bounds = [min_y, max_y, min_x, max_x]

        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                coordinate = str(y) + '_' + str(x)
                if self.check_pixel(y, x, bounds) == '#':
                    image_pixels_to_alter[coordinate] = '#'
                else:
                    image_pixels_to_alter[coordinate] = '.'

        for key in image_pixels_to_alter.keys():
            if image_pixels_to_alter[key] == '#':
                self.image.add(key)
            else:
                if key in self.image:
                    self.image.remove(key)

        if self.even_generation:
            if self.enhancement[0] == '#' and self.enhancement[-1] == '.':
                self.remove_edges(bounds)
        self.even_generation = not self.even_generation

    def __str__(self):
        # Find max
        max_y = 0
        min_y = 0
        max_x = 0
        min_x = 0
        for entry in self.image:
            coordinates = entry.split('_')
            if int(coordinates[0]) > max_y:
                max_y = int(coordinates[0])
            elif int(coordinates[0]) < min_y:
                min_y = int(coordinates[0])
            if int(coordinates[1]) > max_x:
                max_x = int(coordinates[1])
            elif int(coordinates[1]) < min_x:
                min_x = int(coordinates[1])

        y_offset = abs(min_y)
        x_offset = abs(min_x)

        image = []
        for y in range(max_y + 1 + y_offset):
            row = []
            for x in range(max_x + 1 + x_offset):
                row.append('.')
            image.append(row)

        for entry in self.image:
            coordinates = entry.split('_')
            y = int(coordinates[0]) + y_offset
            x = int(coordinates[1]) + x_offset
            image[y][x] = '#'

        string = ''
        for line in image:
            row = ''
            for char in line:
                row += char
            string += row + '\n'
        return string


def parse(string_array):
    image = []
    for i in range(2, len(string_array)):
        image.append(string_array[i])
    return image


def part_1(raw_input):
    enhancement_string = raw_input[0]
    image_string_array = parse(raw_input)

    image = Image(enhancement_string, image_string_array)

    for _ in range(2):
        image.enhance()

    return len(image.image)


def part_2(raw_input):
    print('Please wait, this could take a while...')
    enhancement_string = raw_input[0]
    image_string_array = parse(raw_input)

    image = Image(enhancement_string, image_string_array)

    for _ in range(50):
        image.enhance()

    return len(image.image)
