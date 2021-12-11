def part_1(raw_input):
    gamma = ''
    epsilon = ''
    data_length = len(raw_input)
    line_length = len(raw_input[0])

    # Simply run through the list, one bit letter at a time
    for letter in range(0, line_length):
        ones = 0
        for line in range(0, data_length):
            if raw_input[line][letter] == '1':
                ones += 1

        if ones > data_length/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def part_2(raw_input):
    line_length = len(raw_input[0])
    is_oxygen = 'oxygen'
    is_co2 = 'co2'

    def get_bits(data_type):
        # Same as above, but we'll use a second array as a checklist
        checklist = []
        for line in raw_input:
            checklist.append(True)

        for letter in range(0, line_length):
            # Data length is dependant on number of True in checklist
            # Check ones
            data_length = 0
            ones = 0
            for i in range(0, len(checklist)):
                if checklist[i]:
                    data_length += 1
                    if raw_input[i][letter] == '1':
                        ones += 1

            # Return value if data length is 1
            if data_length == 1:
                for i in range(0, len(checklist)):
                    if checklist[i]:
                        return raw_input[i]

            # Aim to get the majority bit
            get_ones = True
            if ones < data_length/2:
                get_ones = not get_ones
            # CO2 Scrubbers want minority bit
            if data_type == is_co2:
                get_ones = not get_ones

            for i in range(0, len(raw_input)):
                if checklist[i]:
                    indexed_letter = raw_input[i][letter]
                    if indexed_letter == '0':
                        if get_ones:
                            checklist[i] = False
                    elif indexed_letter == '1':
                        if get_ones is False:
                            checklist[i] = False

        # Code below is in case the proper number found occurs after for loop completes
        true_num = 0
        for x in checklist:
            if x:
                true_num += 1
        if true_num:
            for i in range(0, len(checklist)):
                if checklist[i]:
                    return raw_input[i]

    return int(get_bits(is_co2), 2) * int(get_bits(is_oxygen), 2)
