def match_bracket(start, stop):
    if start == '(' and stop == ')':
        return True
    elif start == '[' and stop == ']':
        return True
    elif start == '{' and stop == '}':
        return True
    elif start == '<' and stop == '>':
        return True
    else:
        return False


def is_starting_bracket(bracket):
    if bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<':
        return True
    else:
        return False


def bracket_type(bracket):
    if bracket == '(':
        return 0
    elif bracket == ')':
        return -1
    elif bracket == '[':
        return 1
    elif bracket == ']':
        return -2
    elif bracket == '{':
        return 2
    elif bracket == '}':
        return -3
    elif bracket == '<':
        return 3
    elif bracket == '>':
        return -4


def end_char(num):
    if num == 0:
        return ')'
    elif num == 1:
        return ']'
    elif num == 2:
        return '}'
    elif num == 3:
        return '>'


def end_char_value_part1(char):
    if char == ')':
        return 3
    elif char == ']':
        return 57
    elif char == '}':
        return 1197
    elif char == '>':
        return 25137


def end_char_value_part2(char):
    if char == '(':
        return 1
    elif char == '[':
        return 2
    elif char == '{':
        return 3
    elif char == '<':
        return 4


def remove_complete_chunks(string: str, starting_index: int):
    if starting_index == len(string):
        return string
    starting_bracket = string[starting_index]
    steps = 1
    end_index = starting_index
    # Extract proper content of chunk
    for i in range(starting_index + 1, len(string)):
        if starting_bracket == string[i]:
            steps += 1
        elif match_bracket(starting_bracket, string[i]):
            steps -= 1
            if steps == 0:
                end_index = i
                break
    new_string = string[:starting_index] + string[end_index:]
    if steps == 0:
        new_string = string[:starting_index] + string[end_index+1:]
        return remove_complete_chunks(new_string, starting_index)
    else:
        return remove_complete_chunks(new_string, starting_index + 1)


def examined_char(string):
    starting_bracket = string[0]
    steps = 1
    end_index = len(string)
    # Extract proper content of chunk
    for i in range(1, len(string)):
        if starting_bracket == string[i]:
            steps += 1
        elif match_bracket(starting_bracket, string[i]):
            steps -= 1
            if steps == 0:
                end_index = i
                break
    substring = string[1:end_index]
    # Each type of bracket has a weight to it
    # Indices of weights: ( = 0, [ = 1, { = 2 < = 3
    # Starting brackets add 1 to weight, end brackets subtract 1
    # If any bracket weight is negative, we have a corrupted line
    bracket_weights = [0, 0, 0, 0]
    for char in substring:
        char_val = bracket_type(char)
        if char_val < 0:
            bracket_weights[abs(char_val + 1)] -= 1
        else:
            bracket_weights[char_val] += 1
        for x in range(0, len(bracket_weights)):
            if bracket_weights[x] < 0:
                return end_char(x)
    return 'n'


def part_1(raw_input):
    answer = 0

    for line in raw_input:
        # Divide whole line into its chunks
        for index in range(0, len(line)):
            # Only send substrings that start with proper brackets
            if is_starting_bracket(line[index]):
                # Check chunk to see if it has a corrupted char
                corrupted_char = examined_char(line[index:len(line)])
                if not corrupted_char == 'n':
                    answer += end_char_value_part1(corrupted_char)
                    break

    return answer


def part_2(raw_input):
    # Create new array excluding corrupted lines

    strings = []
    score_list = []

    # Reuse code from part 1 with minor alteration
    for line in raw_input:
        add_line = True
        for index in range(0, len(line)):
            if is_starting_bracket(line[index]):
                corrupted_char = examined_char(line[index:len(line)])
                if not corrupted_char == 'n':
                    add_line = False
                    break
        if add_line:
            strings.append(line)

    # for x in strings:
    #     print(x)

    # Go through incomplete strings, removing complete chunks and reversing their order
    # test = '[({(<(())[]>[[{[]{<()<>>'
    # print(remove_complete_chunks(test, 0))
    for line in strings:
        leftover_brackets = remove_complete_chunks(line, 0)[::-1]
        # Calculate value and add to score
        score = 0
        for char in leftover_brackets:
            score = (score * 5) + end_char_value_part2(char)
        score_list.append(score)

    score_list = sorted(score_list)

    return score_list[int(len(score_list) / 2)]
