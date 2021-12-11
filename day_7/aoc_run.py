def parse(data):
    string_array = data[0].split(',')
    int_array = []
    for x in string_array:
        int_array.append(int(x))
    return int_array


def part_1(raw_input):
    # Simple brute forcing a solution
    starting_positions = parse(raw_input)
    fuel_costs = []
    for position in range(0, len(starting_positions)):
        fuel = 0
        for spot in starting_positions:
            fuel += abs(spot - position)
        fuel_costs.append(fuel)

    spot_min = fuel_costs[0]
    spot_index = 0
    for index in range(1, len(fuel_costs)):
        if fuel_costs[index] < spot_min:
            spot_min = fuel_costs[index]
            spot_index = index

    return fuel_costs[spot_index]


def part_2(raw_input):
    # Same as above but with an added modifier
    starting_positions = parse(raw_input)
    fuel_costs = []
    for position in range(0, len(starting_positions)):
        fuel = 0
        for spot in starting_positions:
            steps = abs(spot - position)
            # Added modifier here to properly account for added fuel
            # Originally brute forcing addition took to long, a quick google and I found the formula for
            # partial sums: (n * (n + 1)) / 2
            # This cut time from 11 seconds to 175 ms
            fuel += int((steps * (steps + 1)) / 2)

        fuel_costs.append(fuel)

    spot_min = fuel_costs[0]
    spot_index = 0
    for index in range(1, len(fuel_costs)):
        if fuel_costs[index] < spot_min:
            spot_min = fuel_costs[index]
            spot_index = index

    return fuel_costs[spot_index]
