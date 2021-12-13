class TransparentPaper:
    def __init__(self, board: [[bool]]):
        self.dots = board

    def fold_horizontal(self, index):
        # Split the paper horizontally
        upper_piece = []
        lower_piece = []
        for i in range(0, index):
            upper_piece.append(self.dots[i])
        for i in range(index + 1, len(self.dots)):
            lower_piece.append(self.dots[i])
        # Iterate lines in lower_piece and add dots to upper piece
        for y in range(0, len(lower_piece)):
            for x in range(0, len(lower_piece[0])):
                if lower_piece[y][x]:
                    # Since the paper is folded, invert the order which rows are read/written
                    upper_piece[index - y - 1][x] = True
        self.dots = upper_piece

    def fold_vertical(self, index):
        # Similar to fold_horizontal except done on columns
        new_paper = []
        for line in self.dots:
            left_row = []
            right_row = []
            for i in range(0, index):
                left_row.append(line[i])
            for i in range(index + 1, len(line)):
                right_row.append(line[i])
            # Iterate through right_row to find dots
            for i in range(0, len(right_row)):
                if right_row[i]:
                    left_row[index - i - 1] = True
            new_paper.append(left_row)
        self.dots = new_paper

    def count_dots(self):
        count = 0
        for line in self.dots:
            for cell in line:
                if cell:
                    count += 1
        return count

    def __str__(self):
        string = ''
        for line in self.dots:
            row = ''
            for cell in line:
                if cell:
                    row += '#'
                else:
                    row += '.'
            string += row + '\n'
        # Remove final newline for neater result on printout
        return string[:-1]


def get_paper(string_array: [str]):
    # Parse input to get an array where True is dots and False is empty
    board = []
    int_array = []
    max_x = 0
    max_y = 0
    for line in string_array:
        if ',' in line:
            split_line = line.split(',')
            line_x = int(split_line[0])
            line_y = int(split_line[1])
            if line_x > max_x:
                max_x = line_x
            if line_y > max_y:
                max_y = line_y
            int_array.append([line_x, line_y])
    for _ in range(0, max_y + 1):
        row = []
        for _ in range(0, max_x + 1):
            row.append(False)
        board.append(row)
    for coord in int_array:
        x = coord[0]
        y = coord[1]
        board[y][x] = True

    return TransparentPaper(board)


def get_instructions(string_array: [str]):
    # Parse input to get instructions
    instructions = []
    for line in string_array:
        if 'fold' in line:
            instruction = []
            line_string = line.replace('fold along ', '')
            instruction.append(line_string[:1])
            instruction.append(line_string[2:])
            instructions.append(instruction)
    return instructions


def part_1(raw_input):
    paper = get_paper(raw_input)
    instructions = get_instructions(raw_input)
    direction = instructions[0][0]
    index = int(instructions[0][1])
    if direction == 'y':
        paper.fold_horizontal(index)
    if direction == 'x':
        paper.fold_vertical(index)
    return paper.count_dots()


def part_2(raw_input):
    # Same as part 1, but with all instructions
    paper = get_paper(raw_input)
    instructions = get_instructions(raw_input)
    for instruction in instructions:
        direction = instruction[0]
        index = int(instruction[1])
        if direction == 'y':
            paper.fold_horizontal(index)
        if direction == 'x':
            paper.fold_vertical(index)
    # TODO: Could add something here that interprets the result and returns a string for easier copy-paste answer
    return paper
