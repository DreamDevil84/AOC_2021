class SnailFishHomework:
    def __init__(self, string):
        # self.number = self.make_array(string)
        self.number = string

    def reduce_number(self):
        start_bracket = '['
        end_bracket = ']'
        comma = ','
        numbers = '0123456789'

        string = self.number

        def explode(s):
            index = 0
            steps = 0

            new_string = s

            def add_string_numbers(num_1, num_2):
                return str(int(num_1) + int(num_2))

            def add_left(value, index_start, work_string):
                i = index_start
                while True:
                    if i < 0:
                        return work_string
                    if work_string[i] in numbers:
                        i_end = i + 1
                        while True:
                            if work_string[i] not in numbers:
                                i += 1
                                l_string = work_string[:i] + add_string_numbers(work_string[i:i_end], value) + work_string[i_end:]
                                break
                            i -= 1
                        break
                    i -= 1
                return l_string

            def add_right(value, index_start, work_string):
                i = index_start
                while True:
                    if i >= len(work_string):
                        return work_string
                    if work_string[i] in numbers:
                        i_start = i
                        while True:
                            if work_string[i] not in numbers:
                                r_string = work_string[:i_start] + add_string_numbers(work_string[i_start:i], value) + work_string[i:]
                                break
                            i += 1
                        break
                    i += 1
                return r_string

            def cut_middle(start, stop):
                return new_string[:start] + '0' + new_string[stop:]

            while True:
                # Out of bounds exit
                if index >= len(new_string):
                    break
                # Step count
                if new_string[index] == start_bracket:
                    index += 1
                    steps += 1
                    continue
                if new_string[index] == end_bracket:
                    index += 1
                    steps -= 1
                    continue
                # Find exploder
                if new_string[index] in numbers and steps > 4:
                    # Isolate values
                    cutout_start = index - 1
                    cutout_end = index + 1
                    value_end_index = index + 1
                    while True:
                        if new_string[value_end_index] == end_bracket:
                            cutout_end = value_end_index + 1
                            break
                        value_end_index += 1
                    values = new_string[index:value_end_index].split(comma)

                    # Important to do changes from right to left to avoid indexing errors
                    new_string = add_right(values[1], cutout_end, new_string)
                    new_string = cut_middle(cutout_start, cutout_end)
                    new_string = add_left(values[0], cutout_start - 1, new_string)

                    # If exploder is found, return with True and new string
                    return True, new_string
                index += 1

            # If no exploder found, return with False and original string
            return False, new_string

        def split_number(s):
            new_string = s
            # Find first result greater than 9
            index = 0

            def calculate_new_pair(number: int):
                # A bit of Python quick math
                val_1 = number // 2
                val_2 = -(number // -2)
                return start_bracket + str(val_1) + comma + str(val_2) + end_bracket

            while True:
                if index >= len(new_string) - 1:
                    break
                if new_string[index] in numbers and new_string[index + 1] in numbers:
                    number_start = index
                    index += 1
                    while True:
                        if new_string[index] not in numbers:
                            number_end = index
                            break
                        index += 1
                    new_pair = calculate_new_pair(int(new_string[number_start:number_end]))
                    new_string = new_string[:number_start] + new_pair + new_string[number_end:]
                    return True, new_string
                index += 1

            return False, new_string

        while True:
            explode_result = explode(string)
            # Run explode until it returns False
            if explode_result[0]:
                string = explode_result[1]
                continue
            # Run split once
            split_result = split_number(string)
            if split_result[0]:
                string = split_result[1]
                continue
            # If both explode and split yield False, break loop, reduction done
            if not explode_result[0] and not split_result[0]:
                break
        self.number = string

    def add_snail_number(self, string):
        self.number = '[' + self.number + ',' + string + ']'

    def get_magnitude(self):
        start_bracket = '['
        end_bracket = ']'
        comma = ','
        numbers = '0123456789'

        index = 0
        steps = 0

        string = self.number

        # Do the layers from the deepest to shallowest
        for layer in range(0, 4):
            index = 0
            steps = 0
            while True:
                # Out of bounds exit
                if index >= len(string):
                    break
                # Step count
                if string[index] == start_bracket:
                    index += 1
                    steps += 1
                    continue
                if string[index] == end_bracket:
                    index += 1
                    steps -= 1
                    continue
                if string[index] in numbers and steps > 3 - layer:
                    # Isolate values
                    cutout_start = index - 1
                    cutout_end = index + 1
                    value_end_index = index + 1
                    while True:
                        if string[value_end_index] == end_bracket:
                            cutout_end = value_end_index + 1
                            break
                        value_end_index += 1
                    values = string[index:value_end_index].split(comma)
                    val_1 = int(values[0]) * 3
                    val_2 = int(values[1]) * 2
                    string = string[:cutout_start] + str(val_1 + val_2) + string[cutout_end:]
                    # Reset layer search
                    index = 0
                    steps = 0
                    continue
                index += 1
        return string


def part_1(raw_input):
    homework = SnailFishHomework(raw_input[0])
    homework.reduce_number()

    for i in range(1, len(raw_input)):
        homework.add_snail_number(raw_input[i])
        homework.reduce_number()

    return homework.get_magnitude()


def part_2(raw_input):
    max_val = 0
    for i in range(len(raw_input)):
        for j in range(len(raw_input)):
            if not i == j:
                homework = SnailFishHomework(raw_input[i])
                homework.reduce_number()

                homework.add_snail_number(raw_input[j])
                homework.reduce_number()

                num_sum = int(homework.get_magnitude())
                if num_sum > max_val:
                    max_val = num_sum
    return max_val
