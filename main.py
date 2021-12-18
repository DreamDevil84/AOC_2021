import time
import sys
import day_1.aoc_run
import day_2.aoc_run
import day_3.aoc_run
import day_4.aoc_run
import day_5.aoc_run
import day_6.aoc_run
import day_7.aoc_run
import day_8.aoc_run
import day_9.aoc_run
import day_10.aoc_run
import day_11.aoc_run
import day_12.aoc_run
import day_13.aoc_run
import day_14.aoc_run
import day_15.aoc_run
import day_16.aoc_run
import day_17.aoc_run
import day_18.aoc_run
import day_19.aoc_run
import day_20.aoc_run
import day_21.aoc_run
import day_22.aoc_run
import day_23.aoc_run
import day_24.aoc_run
import day_25.aoc_run


# Awful if trees :(
def run(day, filename):
    def get_data(date, data_type):
        datafile = open('day_' + str(date) + '/' + data_type + '.txt')
        data = []

        for line in datafile:
            entry = line.replace('\n', "")
            data.append(entry)

        datafile.close()
        return data

    if 0 < day < 26:
        # Part 1
        start_time = time.time()
        if day == 1:
            print(day_1.aoc_run.part_1(get_data(day, filename)))
        if day == 2:
            print(day_2.aoc_run.part_1(get_data(day, filename)))
        if day == 3:
            print(day_3.aoc_run.part_1(get_data(day, filename)))
        if day == 4:
            print(day_4.aoc_run.part_1(get_data(day, filename)))
        if day == 5:
            print(day_5.aoc_run.part_1(get_data(day, filename)))
        if day == 6:
            print(day_6.aoc_run.part_1(get_data(day, filename)))
        if day == 7:
            print(day_7.aoc_run.part_1(get_data(day, filename)))
        if day == 8:
            print(day_8.aoc_run.part_1(get_data(day, filename)))
        if day == 9:
            print(day_9.aoc_run.part_1(get_data(day, filename)))
        if day == 10:
            print(day_10.aoc_run.part_1(get_data(day, filename)))
        if day == 11:
            print(day_11.aoc_run.part_1(get_data(day, filename)))
        if day == 12:
            print(day_12.aoc_run.part_1(get_data(day, filename)))
        if day == 13:
            print(day_13.aoc_run.part_1(get_data(day, filename)))
        if day == 14:
            print(day_14.aoc_run.part_1(get_data(day, filename)))
        if day == 15:
            print(day_15.aoc_run.part_1(get_data(day, filename)))
        if day == 16:
            print(day_16.aoc_run.part_1(get_data(day, filename)))
        if day == 17:
            print(day_17.aoc_run.part_1(get_data(day, filename)))
        if day == 18:
            print(day_18.aoc_run.part_1(get_data(day, filename)))
        if day == 19:
            print(day_19.aoc_run.part_1(get_data(day, filename)))
        if day == 20:
            print(day_20.aoc_run.part_1(get_data(day, filename)))
        if day == 21:
            print(day_21.aoc_run.part_1(get_data(day, filename)))
        if day == 22:
            print(day_22.aoc_run.part_1(get_data(day, filename)))
        if day == 23:
            print(day_23.aoc_run.part_1(get_data(day, filename)))
        if day == 24:
            print(day_24.aoc_run.part_1(get_data(day, filename)))
        if day == 25:
            print(day_25.aoc_run.part_1(get_data(day, filename)))
        complete_time = round((time.time() - start_time) * 1000, 2)
        print(str(complete_time) + ' ms')

        # Part 2
        start_time = time.time()
        if day == 1:
            print(day_1.aoc_run.part_2(get_data(day, filename)))
        if day == 2:
            print(day_2.aoc_run.part_2(get_data(day, filename)))
        if day == 3:
            print(day_3.aoc_run.part_2(get_data(day, filename)))
        if day == 4:
            print(day_4.aoc_run.part_2(get_data(day, filename)))
        if day == 5:
            print(day_5.aoc_run.part_2(get_data(day, filename)))
        if day == 6:
            print(day_6.aoc_run.part_2(get_data(day, filename)))
        if day == 7:
            print(day_7.aoc_run.part_2(get_data(day, filename)))
        if day == 8:
            print(day_8.aoc_run.part_2(get_data(day, filename)))
        if day == 9:
            print(day_9.aoc_run.part_2(get_data(day, filename)))
        if day == 10:
            print(day_10.aoc_run.part_2(get_data(day, filename)))
        if day == 11:
            print(day_11.aoc_run.part_2(get_data(day, filename)))
        if day == 12:
            print(day_12.aoc_run.part_2(get_data(day, filename)))
        if day == 13:
            print(day_13.aoc_run.part_2(get_data(day, filename)))
        if day == 14:
            print(day_14.aoc_run.part_2(get_data(day, filename)))
        if day == 15:
            print(day_15.aoc_run.part_2(get_data(day, filename)))
        if day == 16:
            print(day_16.aoc_run.part_2(get_data(day, filename)))
        if day == 17:
            print(day_17.aoc_run.part_2(get_data(day, filename)))
        if day == 18:
            print(day_18.aoc_run.part_2(get_data(day, filename)))
        if day == 19:
            print(day_19.aoc_run.part_2(get_data(day, filename)))
        if day == 20:
            print(day_20.aoc_run.part_2(get_data(day, filename)))
        if day == 21:
            print(day_21.aoc_run.part_2(get_data(day, filename)))
        if day == 22:
            print(day_22.aoc_run.part_2(get_data(day, filename)))
        if day == 23:
            print(day_23.aoc_run.part_2(get_data(day, filename)))
        if day == 24:
            print(day_24.aoc_run.part_2(get_data(day, filename)))
        if day == 25:
            print(day_25.aoc_run.part_2(get_data(day, filename)))
        complete_time = round((time.time() - start_time) * 1000, 2)
        print(str(complete_time) + ' ms')

    else:
        print("Arg must be an integer between 1 and 25")


DATA = 'input'
SAMPLE = 'sample'

# run(18, SAMPLE)
# run(18, DATA)


if __name__ == "__main__":
    d = int(sys.argv[1])
    fn = str(sys.argv[2])
    run(d, fn)
