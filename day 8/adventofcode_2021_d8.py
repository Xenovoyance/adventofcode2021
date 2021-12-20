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


if __name__ == "__main__":
    start_time = time.perf_counter()
    solution_pt1 = part_one()
    execution_time = str((time.perf_counter() - start_time) * 1000)
    print(f"Day 7, part 1: {part_one()} executed in {execution_time} ms")
