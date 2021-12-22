import time


def part_one():
    keys = []
    with open("adventofcode_2021_d8.txt", "r") as f:
        for line in f.readlines():
            keys.append(line.split("|")[1].strip().split(" "))

    counter = 0

    for num in keys:
        for number in num:
            if len(number) in [2, 3, 4, 7]:
                counter += 1
    return str(counter)


def part_two():
    sum = 0
    with open("adventofcode_2021_d8.txt", "r") as f:
        for line in f.readlines():
            tmp_line_list = line.split("|")[0].strip().split(
                " ") + line.split("|")[1].strip().split(" ")
            output = ""

            one = set()
            two = set()
            three = set()
            four = set()
            five = set()
            six = set()
            seven = set()
            eight = set()
            nine = set()
            zero = set()

            for x in tmp_line_list:
                if len(x) == 2:
                    [one.add(y) for y in x]
                elif len(x) == 3:
                    [seven.add(y) for y in x]
                elif len(x) == 4:
                    [four.add(y) for y in x]
                elif len(x) == 7:
                    [eight.add(y) for y in x]

            for x in tmp_line_list:
                _set = set()
                [_set.add(y) for y in x]

                if len(x) == 2:
                    output += "1"
                elif len(x) == 3:
                    output += "7"
                elif len(x) == 4:
                    output += "4"
                elif len(x) == 7:
                    output += "8"

                if len(x) == 6:
                    if len(_set - four) == 2:
                        [nine.add(x) for y in x]
                        output += "9"
                    elif len(_set - one) == 5:
                        [six.add(x) for y in x]
                        output += "6"
                    else:
                        [zero.add(x) for y in x]
                        output += "0"
                elif len(x) == 5:
                    if len(_set - one) == 3:
                        [three.add(x) for y in x]
                        output += "3"
                    elif len(_set - four) == 3:
                        [two.add(x) for y in x]
                        output += "2"
                    else:
                        [five.add(x) for y in x]
                        output += "5"

            sum += int(output[-4:])
    return str(sum)


if __name__ == "__main__":
    start_time = time.perf_counter()
    solution_pt1 = part_one()
    execution_time = str((time.perf_counter() - start_time) * 1000)
    print(f"Day 8, part 1: {solution_pt1} executed in {execution_time} ms")

    start_time = time.perf_counter()
    solution_pt2 = part_two()
    execution_time = str((time.perf_counter() - start_time) * 1000)
    print(f"Day 8, part 2: {solution_pt2} executed in {execution_time} ms")