def create_dict(data):
    dictionary = {}
    for line in data:
        if '->' in line:
            pair = line[:2]
            insert = line[-1:]
            dictionary[pair] = insert
    return dictionary


def part_1(raw_input):
    # Create dictionary for elements and their insertions
    elements = create_dict(raw_input)
    polymer_string = raw_input[0]

    # NOTE: This is not going to scale well
    for _ in range(0, 10):
        new_polymer = ''
        # Iterate through polymer_string to build new_polymer
        for index in range(0, len(polymer_string) - 1):
            new_polymer += polymer_string[index]
            # Extract pair for comparison
            pair = polymer_string[index: index + 2]
            if pair in elements.keys():
                new_polymer += elements[pair]
        # Add final character and replace polymer string
        polymer_string = new_polymer + polymer_string[-1]

    # Create second dictionary for counting instances of elements (letters)
    letter_dictionary = {}
    for char in polymer_string:
        if char in letter_dictionary.keys():
            letter_dictionary[char] += 1
        else:
            letter_dictionary[char] = 1

    # Find smallest and largest
    smallest = len(polymer_string)
    largest = 0
    for key in letter_dictionary.keys():
        val = letter_dictionary[key]
        if val < smallest:
            smallest = val
        if val > largest:
            largest = val

    return largest - smallest


def part_2(raw_input):
    # Can not use part 1 code, would take decades to compute and fry your hardware
    rules = create_dict(raw_input)
    pairs_dictionary = {}
    starting_string = raw_input[0]
    steps = 40
    letter_count = {}

    # Could just count pairs
    for key in rules.keys():
        pairs_dictionary[key] = 0

    for index in range(0, len(starting_string) - 1):
        pair = starting_string[index:index+2]
        pairs_dictionary[pair] += 1

    for _ in range(0, steps):
        new_pairs = pairs_dictionary.copy()
        for key in new_pairs.keys():
            val = new_pairs[key]
            new_pair_1 = key[0] + rules[key]
            new_pair_2 = rules[key] + key[1]
            pairs_dictionary[new_pair_1] += val
            pairs_dictionary[new_pair_2] += val
            # Don't forget to remove pairs that no longer exist
            pairs_dictionary[key] -= val

    # Count letters
    for key in pairs_dictionary.keys():
        letter = key[0]
        if letter in letter_count.keys():
            letter_count[letter] += pairs_dictionary[key]
        else:
            letter_count[letter] = pairs_dictionary[key]
    # Remember to add last final letter in starter string
    letter_count[starting_string[-1]] += 1

    # Find max and minimum
    letters_min = 0
    for key in letter_count.keys():
        letters_min += letter_count[key]
    letters_max = 0

    for key in letter_count.keys():
        val = letter_count[key]
        if val < letters_min:
            letters_min = val
        if val > letters_max:
            letters_max = val

    return letters_max - letters_min
