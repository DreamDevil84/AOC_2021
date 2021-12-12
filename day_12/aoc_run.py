# Upper case letters for reference
LOWER_CASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'


# Create cave class
class Cave:
    is_small = False

    def __init__(self, name: str):
        self.name = name
        if name[0] in LOWER_CASE_LETTERS:
            self.is_small = True


def make_dictionary(string_array):
    # Create dictionary with caves as keys and an array of connections as value
    caves = {}
    for line in string_array:
        line_split = line.split('-')
        cave_1 = line_split[0]
        cave_2 = line_split[1]
        if cave_1 not in caves.keys():
            caves[cave_1] = [cave_2]
        else:
            caves[cave_1].append(cave_2)

        # Repeat in reverse
        if cave_2 not in caves.keys():
            caves[cave_2] = [cave_1]
        else:
            caves[cave_2].append(cave_1)

    return caves


def part_1(raw_input):
    caves = make_dictionary(raw_input)
    # Create set of unique paths
    paths_set = set()

    # Recursively go through each path
    def find_paths(cave: str, ban_set: set, current_path: [str]):
        new_path = current_path.copy()
        new_path.append(cave)
        # If cave is small, add to future banned destinations
        new_ban_set = ban_set.copy()
        if cave[0] in LOWER_CASE_LETTERS and not cave == 'end':
            new_ban_set.add(cave)
        # Write path into set if end is reached
        if cave == 'end':
            path_string = ''
            for string in new_path:
                path_string += string + ','
            paths_set.add(path_string[:-1])
        else:
            destinations = caves[cave]
            for destination in destinations:
                # Check to see if this cave is a valid destination
                if destination not in new_ban_set:
                    find_paths(destination, new_ban_set, new_path)

    # Banned set is of starting cave and small caves that have already been visited this path
    banned_set = {'start'}
    path = []
    find_paths('start', banned_set, path)

    return len(paths_set)


def part_2(raw_input):
    # Gonna be lazy and copy code from part 1
    caves = make_dictionary(raw_input)
    # Create set of unique paths
    paths_set = set()

    # Create a list of small caves
    small_caves = []
    for key in caves.keys():
        if key[0] in LOWER_CASE_LETTERS and not key == 'start' and not key == 'end':
            small_caves.append(key)

    # Recursively go through each path
    def find_paths(cave: str, ban_set: set, current_path: [str], small_exception: str, exception_entries: int):
        new_path = current_path.copy()
        new_path.append(cave)
        new_entries = exception_entries
        # If cave is small, add to future banned destinations
        # But first check if it is the exception
        # If it is, check how many times that cave has been entered
        new_ban_set = ban_set.copy()
        if cave[0] in LOWER_CASE_LETTERS and not cave == 'end':
            if cave == small_exception and exception_entries < 1:
                new_entries += 1
            else:
                new_ban_set.add(cave)
        # Write path into set if end is reached
        if cave == 'end':
            path_string = ''
            for string in new_path:
                path_string += string + ','
            paths_set.add(path_string[:-1])
        else:
            destinations = caves[cave]
            for destination in destinations:
                # Check to see if this cave is a valid destination
                if destination not in new_ban_set:
                    find_paths(destination, new_ban_set, new_path, small_exception, new_entries)

    # Loop through list of small caves
    # Each instance of that cave allows it to be entered twice rather than once
    for small_cave in small_caves:
        # Banned set is of starting cave and small caves that have already been visited this path
        banned_set = {'start'}
        path = []
        find_paths('start', banned_set, path, small_cave, 0)

    return len(paths_set)
