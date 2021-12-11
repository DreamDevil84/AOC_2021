class DumboOctopus:
    def __init__(self, energy):
        self.has_flashed = False
        self.energy: int = energy

    def __str__(self):
        return str(self.energy)


class Octopuses:
    def __init__(self, octopuses: [[DumboOctopus]]):
        self.board = octopuses
        self.flashes = 0
        self.steps = 0
        self.first_synchronous_flash = 0
        self.first_synchronous_flash_found = False

    def advance_step(self):
        # First increase all cells energy by 1
        for line in self.board:
            for cell in line:
                cell.energy += 1

        # Now check for flashes
        new_flashes = True
        # While loop continues as long as there is a new flash
        while new_flashes:
            new_flashes = False
            for y in range(0, len(self.board)):
                for x in range(0, len(self.board[y])):
                    # Check if energy level is high enough and it has not flashed yet
                    if self.board[y][x].energy > 9 and not self.board[y][x].has_flashed:
                        self.board[y][x].has_flashed = True
                        new_flashes = True
                        # Each new flash adds 1 to total flashes
                        self.flashes += 1
                        # Increase energy level in neighbors
                        # Need to add if statements to handle out of bounds errors
                        # Top-left
                        if 0 < y and 0 < x:
                            self.board[y - 1][x - 1].energy += 1
                        # Top
                        if 0 < y:
                            self.board[y - 1][x].energy += 1
                        # Top-right
                        if 0 < y and x < len(self.board[0]) - 1:
                            self.board[y - 1][x + 1].energy += 1
                        # Left
                        if 0 < x:
                            self.board[y][x - 1].energy += 1
                        # Right
                        if x < len(self.board[0]) - 1:
                            self.board[y][x + 1].energy += 1
                        # Bottom-left
                        if y < len(self.board) - 1 and 0 < x:
                            self.board[y + 1][x - 1].energy += 1
                        # Bottom
                        if y < len(self.board) - 1:
                            self.board[y + 1][x].energy += 1
                        # Bottom-right
                        if y < len(self.board) - 1 and x < len(self.board[0]) - 1:
                            self.board[y + 1][x + 1].energy += 1
        # Step has completed
        self.steps += 1
        # After flashes are done, reset flashed cells
        for line in self.board:
            for cell in line:
                if cell.has_flashed:
                    cell.has_flashed = False
                    cell.energy = 0

        # For part 2, we make a quick check to find first synchronous flash
        if not self.first_synchronous_flash_found:
            all_zeroes = True
            for line in self.board:
                for cell in line:
                    if not cell.energy == 0:
                        all_zeroes = False
            if all_zeroes:
                self.first_synchronous_flash = self.steps
                self.first_synchronous_flash_found = True

    def __str__(self):
        string = ''
        for line in self.board:
            new_line = ''
            for num in line:
                new_line += str(num.energy)

            string += new_line + '\n'
        return string


def part_1(raw_input):
    # Generate 2d array of octopuses
    octopuses_array = []
    for line in raw_input:
        row = []
        for char in line:
            row.append(DumboOctopus(int(char)))
        octopuses_array.append(row)

    octopuses = Octopuses(octopuses_array)
    for _ in range(0, 100):
        octopuses.advance_step()
        # print(octopuses)
        # print('-------------')

    return octopuses.flashes


def part_2(raw_input):
    # Generate 2d array of octopuses
    octopuses_array = []
    for line in raw_input:
        row = []
        for char in line:
            row.append(DumboOctopus(int(char)))
        octopuses_array.append(row)

    octopuses = Octopuses(octopuses_array)
    # We run through the steps until we get a synchronous flash
    looking_for_sync = True
    while looking_for_sync:
        octopuses.advance_step()
        if octopuses.first_synchronous_flash_found:
            looking_for_sync = False

        # Safety end
        if octopuses.steps > 100000:
            looking_for_sync = False
            print('ERROR: Loop takes too long')
        # print(octopuses)
        # print('-------------')

    return octopuses.first_synchronous_flash
