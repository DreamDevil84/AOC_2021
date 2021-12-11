# Note: Making classes made part 1 much slower, but part 2 almost instant

# For ease of use, we'll make two classes
class BingoCell:
    def __init__(self, is_active, id_num):
        self.is_active = is_active
        self.id_num = id_num

    def __str__(self):
        return str(self.is_active) + " : " + str(self.id_num)


class BingoBoard:
    has_won = False

    # int_2d_array is a 2d array of integers, representing the numbers of a bingo board
    def __init__(self, int_2d_array):
        self.board = []
        for row in int_2d_array:
            board_row = []
            # Num is an Integer
            for num in row:
                board_row.append(BingoCell(False, num))
            self.board.append(board_row)

    def has_bingo(self):
        # Check rows
        for row in self.board:
            actives = 0
            for cell in row:
                if cell.is_active:
                    actives += 1
            if actives == 5:
                return True
        # Check columns
        for col in range(0, 5):
            actives = 0
            for cell in self.board:
                if cell[col].is_active:
                    actives += 1
            if actives == 5:
                return True
        return False

    def draw_number(self, number):
        for row in self.board:
            for cell in row:
                if cell.id_num == number:
                    cell.is_active = True
                    return

    def get_inactive_value(self):
        val = 0
        for row in self.board:
            for cell in row:
                if not cell.is_active:
                    val += cell.id_num
        return val

    def __str__(self):
        string = ''
        for row in self.board:
            for cell in row:
                string += str(cell) + '\t'
            string += '\n'
        return string


# We need to parse the data into an int array with 1 starter row and several sub 2d arrays for each board
# Assume each board is 5x5
def parse(string_array):
    int_array = []
    first_line = []
    for char in string_array[0].split(','):
        first_line.append(int(char))
    int_array.append(first_line)

    sub_array = []
    count = 0
    for index in range(2, len(string_array)):
        if string_array[index] == '':
            count = 0
            sub_array = []
            continue
        num_line = []
        for char in string_array[index].split():
            num_line.append(int(char))
        sub_array.append(num_line)
        count += 1
        if count == 5:
            int_array.append(sub_array)

    return int_array


def part_1(raw_input):
    data = parse(raw_input)

    # Generate draw list
    bingo_draw = data[0]

    # Generate bingo boards
    bingo_boards = []
    for index in range(1, len(data)):
        board = BingoBoard(data[index])
        bingo_boards.append(board)

    # Go through the draw process and check for winners at the end of each draw
    for number in bingo_draw:
        for board in bingo_boards:
            board.draw_number(number)
        for board in bingo_boards:
            if board.has_bingo():
                return board.get_inactive_value() * number
    return 0


def part_2(raw_input):
    # Start the same as in part 1
    data = parse(raw_input)

    # Generate draw list
    bingo_draw = data[0]

    # Generate bingo boards
    bingo_boards = []
    for index in range(1, len(data)):
        board = BingoBoard(data[index])
        bingo_boards.append(board)

    # Generate winning boards until there is none left
    nr_of_boards = len(bingo_boards)
    for number in bingo_draw:
        for board in bingo_boards:
            board.draw_number(number)
        for board in bingo_boards:
            if not board.has_won and board.has_bingo():
                board.has_won = True
                nr_of_boards -= 1
                if nr_of_boards == 0:
                    return number * board.get_inactive_value()

    return 0
