# Part 2 requires a class
class Digit:
    # Digit display has 7 unique positions
    #           top
    # left_top      right_top
    #           middle
    # left_bottom   right_bottom
    #           bottom
    # Each of these positions are an array of possible values of a -> g
    def __init__(self):
        self.top = 'abcdefg'
        self.left_top = 'abcdefg'
        self.right_top = 'abcdefg'
        self.middle = 'abcdefg'
        self.left_bottom = 'abcdefg'
        self.right_bottom = 'abcdefg'
        self.bottom = 'abcdefg'

    def __str__(self):
        return 'Top:' + self.top + '\n' + 'Top Left:' + self.left_top + '\n' + 'Top Right:' + self.right_top + '\n' + 'Middle:' + self.middle + '\n' + 'Bottom Left:' + self.left_bottom + '\n' + 'Bottom Right:' + self.right_bottom + '\n' + 'Bottom:' + self.bottom

    # Determining what the current digit configuration is like is dependant on the values 1, 7 and 4
    # 2, 3 and 5 use 5 positions, we'll call this five_pos
    # 0, 6 and 9 use 6 positions, we'll call this six_pos
    # 8 uses all, so we ignore it
    def determine_uniques(self, one: str, seven: str, four: str, five_pos: [str], six_pos: [str]):
        def eliminate_already_known_values(position: str, signals: str):
            string = position
            for char in position:
                if char in signals:
                    string = string.replace(char, '')
            return string

        def eliminate_uncommon_value(position: str, signals: [str]):
            string = position
            for char in position:
                for signal in signals:
                    if char not in signal:
                        string = string.replace(char, '')
            return string

        # We start by eliminating possibilities in uniques
        # 1 is a simple replacement
        self.right_top = one
        self.right_bottom = one
        # 7 can replace top
        self.top = seven
        # Then remove values from 1 from top
        self.top = eliminate_already_known_values(self.top, one)
        # 4 can replace middle and left_top
        self.left_top = four
        self.middle = four
        # Then remove values from 1 in both
        self.left_top = eliminate_already_known_values(self.left_top, one)
        self.middle = eliminate_already_known_values(self.middle, one)
        # Likewise, from bottom and left_bottom, we can remove 4 and 7, these should now be limited to 2 values
        self.left_bottom = eliminate_already_known_values(self.left_bottom, seven)
        self.left_bottom = eliminate_already_known_values(self.left_bottom, four)
        self.bottom = eliminate_already_known_values(self.bottom, seven)
        self.bottom = eliminate_already_known_values(self.bottom, four)

        # At this point, top will have only 1 possible signal, and all others are limited to 2
        # 2, 3 and 5 (five_pos) all share top, middle and bottom
        # Top is already known so middle and bottom will be processed
        self.middle = eliminate_uncommon_value(self.middle, five_pos)
        self.bottom = eliminate_uncommon_value(self.left_bottom, five_pos)
        # Since middle and bottom are known, we can remove their values from left_top and left_bottom
        self.left_top = self.left_top.replace(self.middle, '')
        self.left_bottom = self.left_bottom.replace(self.bottom, '')

        # Similar to above, right_bottom is shared amongst 6, 9 and 0, aka six_pos
        self.right_bottom = eliminate_uncommon_value(self.right_bottom, six_pos)
        # Finally remove right_bottoms value from right_top
        self.right_top = self.right_top.replace(self.right_bottom, '')

    # Ugh, painful data entry :(
    def build_signal_dictionary(self):
        signal_dictionary = {}
        zero = self.top + self.left_top + self.right_top + self.left_bottom + self.right_bottom + self.bottom
        one = self.right_top + self.right_bottom
        two = self.top + self.right_top + self.middle + self.left_bottom + self.bottom
        three = self.top + self.middle + self.bottom + self.right_bottom + self.right_top
        four = self.left_top + self.right_top + self.middle + self.right_bottom
        five = self.top + self.left_top + self.middle + self.right_bottom + self.bottom
        six = self.top + self.left_top + self.middle + self.left_bottom + self.right_bottom + self.bottom
        seven = self.top + self.right_top + self.right_bottom
        eight = 'abcdefg'
        nine = self.top + self.left_top + self.right_top + self.middle + self.right_bottom + self.bottom

        signal_dictionary[''.join(sorted(zero))] = '0'
        signal_dictionary[''.join(sorted(one))] = '1'
        signal_dictionary[''.join(sorted(two))] = '2'
        signal_dictionary[''.join(sorted(three))] = '3'
        signal_dictionary[''.join(sorted(four))] = '4'
        signal_dictionary[''.join(sorted(five))] = '5'
        signal_dictionary[''.join(sorted(six))] = '6'
        signal_dictionary[''.join(sorted(seven))] = '7'
        signal_dictionary[''.join(sorted(eight))] = '8'
        signal_dictionary[''.join(sorted(nine))] = '9'

        return signal_dictionary


def parse(data):
    string_array = []
    for line in data:
        segments = line.split(' | ')
        first = segments[0].split(' ')
        second = segments[1].split(' ')
        string_array.append([first, second])
    return string_array


def part_1(raw_input):
    data = parse(raw_input)
    # Count number of matching unique lengths in data
    # Unique lengths are 2, 3, 4, 7
    count = 0
    for line in data:
        for entry in line[1]:
            if len(entry) == 2 or len(entry) == 3 or len(entry) == 4 or len(entry) == 7:
                count += 1

    return count


def part_2(raw_input):
    data = parse(raw_input)

    answer = 0

    for line in data:
        # Extract unique lengths of digits 1, 4 and 7
        one = ''
        four = ''
        seven = ''
        five_length = []
        six_length = []

        for segment in line:
            for entry in segment:
                # Sort the string here to prevent duplicate entries
                sorted_string = sorted(entry)
                a_string = ''.join(sorted_string)

                # Place them in proper values for digit analysis, 8 is ignored
                if len(a_string) == 2:
                    one = a_string
                elif len(a_string) == 4:
                    four = a_string
                elif len(a_string) == 3:
                    seven = a_string
                elif len(a_string) == 5:
                    five_length.append(a_string)
                elif len(a_string) == 6:
                    six_length.append(a_string)
        # Create digit for analysis
        digit = Digit()
        digit.determine_uniques(one, seven, four, five_length, six_length)
        digit_dictionary = digit.build_signal_dictionary()

        # Read actual values
        value_as_string = ''
        for entry in line[1]:
            entry_sorted = ''.join(sorted(entry))
            value_as_string += digit_dictionary[entry_sorted]
        answer += int(value_as_string)

    return answer
